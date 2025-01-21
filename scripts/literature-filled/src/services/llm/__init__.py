from pathlib import Path
import json
import os
import requests

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader, PlaywrightURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate


load_dotenv()

OPENAI_MAX_TOKENS = int(os.getenv("OPENAI_MAX_TOKENS"))
OPENAI_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE"))
OPENAI_MODEL =os.getenv("OPENAI_MODEL")
CHUNK_SIZE=int(os.getenv("CHUNK_SIZE"))
CHUNK_OVERLAP=int(os.getenv("CHUNK_OVERLAP"))

def generate_vector_store(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n"],
        length_function=len,
        is_separator_regex=False,
    )
    docs = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(docs, embeddings)
    return vector_store

class VectorStoreBasedOnFileTypeGenerator:
    def __init__(self, link: str):
        self.link = link
    
    def run(self):
        pass
        
class BasedOnContent(VectorStoreBasedOnFileTypeGenerator):
    def run(self):
        # Download the content from the link
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36', 'Referer': 'https://example.com'}
        response = requests.get(self.link, headers=headers)
        response.raise_for_status()

        # Check if the content is a PDF
        content_type = response.headers.get('Content-Type', '')

        if ('application/pdf' in content_type or 'application/octet-stream' in content_type):
            loader = PyPDFLoader(self.link)
            documents = loader.load()
            return generate_vector_store(documents)
        
        elif 'text/html' in content_type:
            loader = PlaywrightURLLoader(urls=[self.link])
            documents = loader.load()
            return generate_vector_store(documents)

class UsingLangchain(VectorStoreBasedOnFileTypeGenerator):
    def run(self):
        if self.link.lower().endswith('.pdf'):
            # Load PDF content using PyPDFLoader
            loader = PyPDFLoader(self.link)
            documents = loader.load()
            return generate_vector_store(documents)
        else:
            # Load HTML content using UnstructuredURLLoader
            loader = PlaywrightURLLoader(urls=[self.link])
            documents = loader.load()
            return generate_vector_store(documents)


def generate_vector_store_from_link(link: str):
    try:
        return BasedOnContent(link).run()
    except:
        return None


def generate_completion(prompt, vector_store=None):
    llm = ChatOpenAI(model_name=OPENAI_MODEL)
        
    if vector_store:

        # Create a custom prompt template
        system_prompt = (
            "You are a helpful assistant who answers questions solely based on the provided context. "
            "Do not use any external information or prior knowledge. "
            "If the answer is not contained in the context, respond with 'I don't know.'"
        )
        
        prompt_template = PromptTemplate(
            input_variables=['context', 'question'],
            template=(
                f"{system_prompt}\n\n"
                "Context:\n{context}\n\n"
                "Question: {question}\nAnswer:"
            )
        )

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type='stuff',
            retriever=vector_store.as_retriever(),
            return_source_documents=False,
            chain_type_kwargs={
                'prompt': prompt_template,
                'verbose': False,
            }
        )
        
        answer = qa_chain.run(prompt)
        return {"answer": answer.strip(), "is_contextualized": True}
    
    completion = llm(prompt).content
    return {"answer": completion.strip(), "is_contextualized": False}

### Markdown summarizer

def read_markdown_files(file_paths):
    """Reads multiple markdown files and returns their content as a concatenated string."""

    all_content = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            all_content.append(file.read())
    return "\n\n".join(all_content)

def summarize_markdown_files(file_paths, prompt):
    """Summarizes multiple markdown files according to the given prompt."""
    # markdown_content = read_markdown_files(file_paths)
    
    
    summary = dict()
    for file in file_paths:
        with open(file) as f:
            markdown_content = f.read()
        filename = Path(file).stem
        summary[filename] = json.loads(summarize_markdown_content(markdown_content, prompt).replace("```json", "").replace("```", ""))
    return summary


def summarize_markdown_content(markdown_content, prompt):
    """Summarizes the markdown content based on the provided prompt using OpenAI's GPT-4 model."""
    llm = ChatOpenAI(model_name=OPENAI_MODEL)

    summary_prompt = PromptTemplate(
        input_variables=['content', 'prompt'],
        template=(
            "You are a helpful assistant. Based solely on the following markdown content, "
            "answer the user's question or summarize as requested. "
            "If the answer is not in the content, respond with 'I don't know.'\n\n"
            "Markdown Content:\n```\nmd{content}\n\n```\n"
            "User's Request: {prompt}\nAnswer:"
        )
    )


    formatted_prompt = summary_prompt.format(content=markdown_content, prompt=prompt)

    response = llm(formatted_prompt)
    return response.content.strip()