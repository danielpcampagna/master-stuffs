import sys
import glob
import os
import logging
import requests

import fitz
from tqdm import tqdm
from openai import OpenAI
from dotenv import load_dotenv

from src.snowballing_extractor import WorkExtractor
from src.obsidian_file_builder import ObsidianFileBuilder


load_dotenv()
logger = logging.getLogger(__name__)

def get_publication_summary(publication_dict):
    client = OpenAI()
    # Construct publication details
    publication_details = ""
    fields = ['name', 'authors', 'year', 'journal', 'volume', 'number', 'pages', 'place']
    for key in fields:
        if key in publication_dict:
            publication_details += f"{key.capitalize()}: {publication_dict[key]}\n"

    # Create the prompt for the GPT assistant
    title = publication_dict["name"]
    # prompt = f"""Please provide a comprehensive summary of the following scientific publication, including:
    with open("data/01-raw/prompt.md") as f:
        prompt = f.read().format(publication_details=publication_details)

    # Fetch the summary from the GPT assistant
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL"),
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=int(os.getenv("OPENAI_MAX_TOKENS")),
        temperature=float(os.getenv("OPENAI_TEMPERATURE")),
    )

    # summary = response['choices'][0]['message']['content']
    summary = response.choices[0].message.content
    return summary

# Example usage:
if __name__ == "__main__":
    # openai.api_key = os.environ.get

    work_extractor = WorkExtractor(glob.glob("../../literature/snowballing/work/*.py"))
    work_extractor.parse_all()
    publications = work_extractor.work

    for pub in tqdm(publications):
        if pub.get('category').lower() == 'ok':
            summary = get_publication_summary(pub)
            # print(summary)
            
            pub_id = pub.get("target")
            with open(f"data/02-refined/{pub_id}.md", "w") as f:
                f.write(summary)
        else:
            logging.info(f"skip {pub}")

    
    
