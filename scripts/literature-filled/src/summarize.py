"""
Este modulo resume os resultados dos estudos analisando gerados a partir do script `rag_langchain_main.py`
"""

import glob
import os
import logging
import requests
from functools import cache

from tqdm import tqdm
from dotenv import load_dotenv
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate

from vendor.snowballing_extractor import WorkExtractor
from vendor.obsidian_file_builder import ObsidianFileBuilder


load_dotenv()

logger = logging.getLogger(__name__)
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


def generate_completion(prompt, files):
    llm = ChatOpenAI(model_name=OPENAI_MODEL)
    vector_store = None
    if link:
        try:
            vector_store = BasedOnContent(link).run()
        except:
            pass
        
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

######################


def read_markdown_files(file_paths):
    """Reads multiple markdown files and returns their content as a concatenated string."""

    all_content = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            all_content.append(file.read())
    return "\n\n".join(all_content)

def summarize_markdown_files(file_paths, prompt):
    """Summarizes multiple markdown files according to the given prompt."""
    # Read and concatenate the content of the markdown files
    markdown_content = read_markdown_files(file_paths)

    # Generate a summary based on the prompt and markdown content
    summary = summarize_markdown_content(markdown_content, prompt)
    return summary


def summarize_markdown_content(markdown_content, prompt):
    """Summarizes the markdown content based on the provided prompt using OpenAI's GPT-4 model."""
    # Initialize the ChatOpenAI model with GPT-4
    llm = ChatOpenAI(model_name=OPENAI_MODEL)

    # Create a custom prompt template
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

    # Generate the summary or response based on the prompt
    response = llm(formatted_prompt)
    return response.content.strip()
    

if __name__ == "__main__":
    markdown_files = list(file for file in glob.glob("data/02-refined/*.md"))

    # Specify the prompt for summarization
    user_prompt = """You propose an extension for the GDPRov, a data provenance model for the General Data Protection Regulation. Your contributuion have introduced new ontologies for the model so that it turns capable to answer uncovered answers by the literature (for example, you introduce the use of SSN Ontology for representing sensor compoents to delete the data based on the event the data has no longer legal basis).
    
    Now, you are writing a scientific document, specifically the related work section, where you must present the literature related to your work. Start this section introducing the mehotodology we used to reach this work: we use the Snowballing methodology (explain it). At the end of the process, we acheive a total of 178 documents, to which the 15 was summarized within the Markdown Content section.
    
    In a subtle way, present all these 15 studies (in markdown content section) starting by those related to the compliance question Q8, then those related to question Q28, then Q29, Q51, Q63, Q64, BUT DO NOT DIVIDE IT INTO SUBSECTIONS. I expect only paragraphs! Use as many paragraph as you need. Every time you present a related work, you must use the format [[{file_name}]] (even though you are repreating). You must present all authors in the provided content. Write larger paragraphs, cite the key contributions, and the relation with the compliance question.
    
    Bellow, some examples of what I expect:
    
    First Example:
    ```
    Apesar das ferramentas de versionamento (ex.: Git [16] , Mercurial [17] ) tratarem diversos aspectos colaborativos da construção de scripts, elas são ferramentas voltadas para o desenvolvimento de software e estão preocupadas somente com a fase de composição do script. Problemas específicos da pesquisa científica, como a reprodutibilidade do experimento e a consequente necessidade da coleta de proveniência na fase de execução do experimento [5] , não podem ser tratados usando apenas ferramentas de versionamento.

    Além disso, as soluções mais tradicionais de sistemas de gerência de experimentos baseados em script [9], [18] estão focadas somente na coleta da proveniência e não tratam a realização do experimento de forma colaborativa por múltiplos usuários. Mesmo soluções que abordam aspectos colaborativos do experimento, como o ProvDB [11] e o Sumatra [10] , ainda apresentam algumas limitações. O Sumatra [10] , apesar de oferecer uma funcionalidade que permite a utilização da ferramenta por múltiplos usuários, apresenta limitações importantes como: não tratar os arquivos de entrada e saída do experimento, ficando a cargo do pesquisador sincronizar esses dados; e exigir que o servidor esteja acessível durante a execução do experimento com o risco, inclusive, do cientista perder informações caso tal servidor esteja indisponível. Já o ProvDB apresenta limitações como: dependência de ferramenta externa (Git); funcionamento apenas em sistema operacional específico (UNIX); e foco em um tipo específico de experimento (data science analysis). Dessa forma, existe uma lacuna na literatura, em relação ao suporte para colaboração em experimentos in silico executados em forma de script, que pretendemos cobrir com essa proposta.
    ```
    
    Second example:
    ```
    Since the GDPR is “intentionally vague in its technical specifications” [15], it enabled the rise of a variety of solutions. After the law approval, in 2016, a multitude of work and blog posts emerged, chronicling their experience in reaching these requirements [10, 12, 11, 13, 16, 17].
    
    T. Kraska et al. [10] propose an architectural solution, at enterprise-scale, to ensure GDPR compliance for databases, by supporting deletion and consent management. Google researchers have shared their results [11] in getting search service compliance with the Right to be Forgotten, focusing only on this feature.
    
    Other research groups have focused efforts to analyze, propose, and evaluate the impacts of the entire law. Shah et al. [18] investigate the effects of GDPR compliance on storage systems by modifying GDPR-compliant Redis [25]. Shastri et al. [12] reported seven additional metadata items for each personal data, such as purpose, time to live, user objections, records of their processing activities and automated decisions-making, also the origin and sharing information, and, finally, everyone associated with that data. They also present a benchmark analysis showing the critical impacts in space and throughput of adopting this strategy in three database storage solutions. They detect an increase in space factor of 4x and 6x, respectively, in Redis [25] and PostgreSQL [26]. However, while PostgreSQL slows down by a 2x factor when compared to its baseline performance, Redis experiences a slowdown of 5x.
    
    Beyond these approaches, dealing directly with the storage systems, there are also the ones proposing solutions using provenance [20, 21, 22, 23]. Provenance has usually been used in e-science contexts to help in tasks related to the interpretation and understanding of results [7]. This feature aids GDPR analytical and reporting requirements, which have been found, in a recent survey [3], to be necessary to evaluate if personal data were processed and stored according to the owner’s consent.
    
    Aldeco-Pérez and Moreau [4] use provenance to aid in auditing the United Kingdom’s Data Protection (1998) Act. Martin et al. [5] describe how provenance can help in tasks such as disclosing, access control, and data usage. Their context involves the earlier Data Protection Directive (DPD) [24].
    
    Ujcich, Bates and Sanders [9] propose a GDPR data provenance model, shown in Figure 2, based on the data-processing components of prior work ontologies [6, 8]. They use a subset of Bartolini et al. [6] ontology which represents knowledge about the obligations and rights that agents have among themselves. They reject using plans, according to Pandit and Lewis [8] proposal, in exchange for more flexible specifications of how data can be used (i.e. under legal consent for a particular purpose). In general, their contribution is the translation of the rough text of the law into a readable provenance language, by recycling GDPR ontologies to map GDPR concepts into the W3C PROV-DM [19]. However, there is a gap in the literature, regarding discussing this model's stretchability and its capacity to guarantee data privacy and protection. Besides, while most of the proposals we found in the literature focus on a database compliance problem, our proposal deals with a system compliance problem, by tracing back all steps in which the protected data were touched.
    ```
    """

    # Summarize the markdown files
    summary = summarize_markdown_files(markdown_files, user_prompt)
    with open("data/03-final-answer/final-result.md", "w") as f:
        f.write(summary)
    # print("Summary:")
    # print(summary)
        
        
        
        
##############################