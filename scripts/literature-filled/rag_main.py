"""
Este modulo busca melhorar os resultados analisando apenas o conteúdo dos pdf
listados no atributo `link` de cada trabalho.
"""


import io
import glob
import os
import logging
import requests

from tqdm import tqdm
from openai import OpenAI
from dotenv import load_dotenv
import pypdf
from bs4 import BeautifulSoup

from src.snowballing_extractor import WorkExtractor
from src.obsidian_file_builder import ObsidianFileBuilder


load_dotenv()
logger = logging.getLogger(__name__)
client = OpenAI()
max_tokens=int(os.getenv("OPENAI_MAX_TOKENS"))
temperature=float(os.getenv("OPENAI_TEMPERATURE"))

def generate_completion(prompt, link=None):
    if link:
        try:
            # Download the content from the link
            response = requests.get(link)
            response.raise_for_status()

            # Check if the content is a PDF
            content_type = response.headers.get('Content-Type', '')

            if 'application/pdf' in content_type:
                # Read the PDF content
                pdf_file = io.BytesIO(response.content)
                pdf_reader = pypdf.PdfReader(pdf_file)
                pdf_text = ''
                for page in pdf_reader.pages:
                    pdf_text += page.extract_text()
                prompt=f"Based exclusively on the following content:\n\n{pdf_text}\n\nAnswer the following prompt:\n\n{prompt}"
            
            elif 'text/html' in content_type:
                # Process HTML content
                html_content = response.content
                soup = BeautifulSoup(html_content, 'html.parser')
                # Extract text from the HTML
                html_text = soup.get_text(separator='\n', strip=True)
                prompt=f"Based exclusively on the following content:\n\n{html_text}\n\nAnswer the following prompt:\n\n{prompt}"

            # Generate completion based exclusively on the PDF content
            completion = client.chat.completions.create(
                model=os.getenv("OPENAI_MODEL"),
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens,
                temperature=temperature,
            )
            # return completion.choices[0].text.strip()
            return completion.choices[0].message.content
        except requests.exceptions.RequestException as e:
            return f"An error occurred while downloading the content: {e}"
        except Exception as e:
            return f"An error occurred while processing the PDF file: {e}"
    else:
        # Generate completion based on general model knowledge
        completion = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL"),
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature,
        )
        # return completion.choices[0].text.strip()
        return completion.choices[0].message.content


def get_publication_summary(publication_dict):
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
    # response = client.chat.completions.create(
    #     model=os.getenv("OPENAI_MODEL"),
    #     messages=[
    #         {"role": "user", "content": prompt}
    #     ],
    #     max_tokens=max_tokens,
    #     temperature=temperature,
    # )
    # summary = response.choices[0].message.content
    
    link = publication_dict.get("link", None)
    summary = generate_completion(prompt=prompt, link=link)
    return summary

# Example usage:
if __name__ == "__main__":
    # openai.api_key = os.environ.get

    # work_extractor = WorkExtractor(glob.glob("../../literature/snowballing/work/*.py"))
    # work_extractor.parse_all()
    # publications = work_extractor.work
    
    publications = [
        # {
        #     "target": "campagna2020a",
        #     "year": 2020,
        #     "name": "Achieving GDPR Compliance through Provenance: An Extended Model.",
        #     "due": "This contribution extends prior data provenance model in the literature by providing new concepts that capable this model to represent new requisites stipulated by GDPR",
        #     "display": "campagna",
        #     "authors": "Campagna, Daniel Prett and da Silva, Altigran Soares and Braganholo, Vanessa",
        #     "place": "SBBD",
        #     "ID": "campagna2020achieving",
        #     "category": "ok",
        #     "cluster_id": "15772782772141981403",
        #     "entrytype": "inproceedings",
        #     "link": "https://sbbd.org.br/2020/wp-content/uploads/sites/13/2020/09/Archieving-GDPR-ST1.pdf",
        #     "pp": "13--24",
        #     "scholar": "https://scholar.google.com.br/scholar?cites=15772782772141981403&as_sdt=2005&sciodt=0,5&hl=en",
        #     "scholar_id": "237sDF0u5NoJ",
        #     "scholar_ok": True,
        #     "start_set": True
        # }
        {
            "target": "pandit2020a",
            "year": 2020,
            "name": "Representing Activities associated with Processing of Personal Data and Consent using Semantic Web for GDPR Compliance",
            "due": "Related to GDPR. [TODO] This thesis presents a large and useful review of the state of the art about approaches related to GDPR. Additionally, this Pandit's contribution includes:\n\n(1) 120 questions, encompassed into 15 use-cases, elaborated from 7 reliable resources, in addition to the text of GDPR, to assist the endeavor of achieving GDPR compliance; (1a) he also elicits assumptions and constraints associated to those questions (p. 110)\n\n(2) 3 ontologies for representing: (2a) the GDPR text into a glossary of GDPR compliance concepts as a linked data (GDPRtext); (2b) the provenance of activities associated with personal data and consent in ex-ante and ex-post phases (GDPRov); (2c) information regarding consent (GConsent).\n\n# The State of the Art\n\n## 3.2 APPROACHES FOR GDPR COMPLIANCE UTILISING SEMANTIC WEB\n\n1. SPECIAL (Scalable Policy-aware Linked Data Architecture For Privacy, Transparency and Compliance)\n\n2. SERAMIS\n\n3. Vos et al.\n\n4. CitySPIN\n\n5. MIREL\n\n6. DAPRECO\n\n7. BPR4GDPR\n\n8. Elluri et al.\n\n9. Ujcich et al\n\n10. Personal Information Controller Service (PICS)\n\n11. ADvoCATE\n\n12. Ontology by Geko & Tjoa\n\n## APPROACHES ADDRESSING GDPR COMPLIANCE\n\n13. Layered Privacy Language (LPL)\n\n14. Lodge et al.\n\n15. Consent and Data Management Model by Peras\n\n16. Tom et al.\n\n17. Coletti et al.\n\n18. Corrales et al.\n\n19. LUCE\n\n20. Decision Provenance by Singh et al.\n\n21. Sion et al.\n\n22. privacyTracker\n\n23. Metrics for Transparency by Spagnuelo et al.\n\n24. meta-model for PLA by Diamantopoulou et al.\n\n25. Robol et al.\n\n26. Basin et al.\n\n27. RestAssured\n\n28. OPERANDO\n\n29. My Health My Data (MHMD)\n\n## 3.4 APPROACHES INVOLVING PRIVACY POLICIES\n\n30. Usable Privacy Project\n\n31. Polisis and other approaches based on Usable Privacy Project\n\n32. PrivacyGuide\n\n## 3.5 APPROACHES RELATED TO CONSENT\n\n33. Grando et al.\n\n34. Consent Receipt Specification\n\n## 3.6 UPCOMING RESEARCH PROJECTS ADDRESSING GDPR\n\n35. PDP4E\n\n36. DEFeND\n\n37. PAPAYA\n\n38. SMOOTH\n\n39. SODA\n\n40. DECODE\n\n41. MOSAICrOWN\n\n42. PoSEID-on\n\n# Contribution\n\n",
            "display": "pandit [TODO DUE]",
            "authors": "PANDIT, HARSHVARDHAN JITENDRA",
            "place": "arXiv",
            "ID": "pandit2020representing",
            "category": "ok",
            "cluster_id": "7232081120271493220",
            "entrytype": "phdthesis",
            "link": "https://harshp.com/research/publications/035-representing-activities-processing-personal-data-consent-semweb-gdpr-compliance",
            "scholar": "https://scholar.google.com.br/scholar?cites=7232081120271493220&as_sdt=2005&sciodt=0,5&hl=en",
            "scholar_id": "ZGiXMHaDXWQJ",
            "scholar_ok": True,
            "start_set": True
        }
    ]

    for pub in tqdm(publications):
        if pub.get('category').lower() == 'ok':
            summary = get_publication_summary(pub)
            # print(summary)
            
            pub_id = pub.get("target")
            with open(f"data/02-refined/{pub_id}.md", "w") as f:
                f.write(summary)
        else:
            logging.info(f"skip {pub}")
