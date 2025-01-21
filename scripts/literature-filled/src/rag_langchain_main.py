"""
Este modulo busca melhorar os resultados analisando apenas o conteúdo dos pdf
listados no atributo `link` de cada trabalho.
"""

import glob
from functools import cache
import logging

from tqdm import tqdm
from vendor.snowballing_extractor import WorkExtractor
from vendor.obsidian_file_builder import ObsidianFileBuilder

from services.llm import generate_completion, generate_vector_store_from_link


logger = logging.getLogger(__name__)

@cache
def load_prompt():
    with open("data/01-raw/prompt.md") as f:
        prompt = f.read()
    return prompt

def get_publication_summary(publication_dict):
    # Construct publication details
    publication_details = ""
    fields = ['name', 'authors', 'year', 'journal', 'volume', 'number', 'pages', 'place']
    for key in fields:
        if key in publication_dict:
            publication_details += f"{key.capitalize()}: {publication_dict[key]}\n"

    prompt = load_prompt().format(publication_details=publication_details)
    link = publication_dict.get("link", None)
    
    vector_store = None if link is None else generate_vector_store_from_link(link)
    summary = generate_completion(prompt=prompt, vector_store=vector_store)
    
    answer, context = summary["answer"], summary["is_contextualized"]
    answer = answer.replace("```md", "").replace("```", "")
    
    return f"""---\ncontext: {context}\n---\n\n{answer}"""

# Example usage:
if __name__ == "__main__":
    # work_extractor = WorkExtractor(glob.glob("../../literature/snowballing/work/*.py"))
    # work_extractor.parse_all()
    # publications = work_extractor.work
    
    publications = [
    #     # {
    #     #     "target": "campagna2020a",
    #     #     "year": 2020,
    #     #     "name": "Achieving GDPR Compliance through Provenance: An Extended Model.",
    #     #     "due": "This contribution extends prior data provenance model in the literature by providing new concepts that capable this model to represent new requisites stipulated by GDPR",
    #     #     "display": "campagna",
    #     #     "authors": "Campagna, Daniel Prett and da Silva, Altigran Soares and Braganholo, Vanessa",
    #     #     "place": "SBBD",
    #     #     "ID": "campagna2020achieving",
    #     #     "category": "ok",
    #     #     "cluster_id": "15772782772141981403",
    #     #     "entrytype": "inproceedings",
    #     #     "link": "https://sbbd.org.br/2020/wp-content/uploads/sites/13/2020/09/Archieving-GDPR-ST1.pdf",
    #     #     "pp": "13--24",
    #     #     "scholar": "https://scholar.google.com.br/scholar?cites=15772782772141981403&as_sdt=2005&sciodt=0,5&hl=en",
    #     #     "scholar_id": "237sDF0u5NoJ",
    #     #     "scholar_ok": True,
    #     #     "start_set": True
    #     # },
    #     # {
    #     #     "target": "pandit2020a",
    #     #     "year": 2020,
    #     #     "name": "Representing Activities associated with Processing of Personal Data and Consent using Semantic Web for GDPR Compliance",
    #     #     "due": "Related to GDPR. [TODO] This thesis presents a large and useful review of the state of the art about approaches related to GDPR. Additionally, this Pandit's contribution includes:\n\n(1) 120 questions, encompassed into 15 use-cases, elaborated from 7 reliable resources, in addition to the text of GDPR, to assist the endeavor of achieving GDPR compliance; (1a) he also elicits assumptions and constraints associated to those questions (p. 110)\n\n(2) 3 ontologies for representing: (2a) the GDPR text into a glossary of GDPR compliance concepts as a linked data (GDPRtext); (2b) the provenance of activities associated with personal data and consent in ex-ante and ex-post phases (GDPRov); (2c) information regarding consent (GConsent).\n\n# The State of the Art\n\n## 3.2 APPROACHES FOR GDPR COMPLIANCE UTILISING SEMANTIC WEB\n\n1. SPECIAL (Scalable Policy-aware Linked Data Architecture For Privacy, Transparency and Compliance)\n\n2. SERAMIS\n\n3. Vos et al.\n\n4. CitySPIN\n\n5. MIREL\n\n6. DAPRECO\n\n7. BPR4GDPR\n\n8. Elluri et al.\n\n9. Ujcich et al\n\n10. Personal Information Controller Service (PICS)\n\n11. ADvoCATE\n\n12. Ontology by Geko & Tjoa\n\n## APPROACHES ADDRESSING GDPR COMPLIANCE\n\n13. Layered Privacy Language (LPL)\n\n14. Lodge et al.\n\n15. Consent and Data Management Model by Peras\n\n16. Tom et al.\n\n17. Coletti et al.\n\n18. Corrales et al.\n\n19. LUCE\n\n20. Decision Provenance by Singh et al.\n\n21. Sion et al.\n\n22. privacyTracker\n\n23. Metrics for Transparency by Spagnuelo et al.\n\n24. meta-model for PLA by Diamantopoulou et al.\n\n25. Robol et al.\n\n26. Basin et al.\n\n27. RestAssured\n\n28. OPERANDO\n\n29. My Health My Data (MHMD)\n\n## 3.4 APPROACHES INVOLVING PRIVACY POLICIES\n\n30. Usable Privacy Project\n\n31. Polisis and other approaches based on Usable Privacy Project\n\n32. PrivacyGuide\n\n## 3.5 APPROACHES RELATED TO CONSENT\n\n33. Grando et al.\n\n34. Consent Receipt Specification\n\n## 3.6 UPCOMING RESEARCH PROJECTS ADDRESSING GDPR\n\n35. PDP4E\n\n36. DEFeND\n\n37. PAPAYA\n\n38. SMOOTH\n\n39. SODA\n\n40. DECODE\n\n41. MOSAICrOWN\n\n42. PoSEID-on\n\n# Contribution\n\n",
    #     #     "display": "pandit [TODO DUE]",
    #     #     "authors": "PANDIT, HARSHVARDHAN JITENDRA",
    #     #     "place": "arXiv",
    #     #     "ID": "pandit2020representing",
    #     #     "category": "ok",
    #     #     "cluster_id": "7232081120271493220",
    #     #     "entrytype": "phdthesis",
    #     #     "link": "https://harshp.com/research/publications/035-representing-activities-processing-personal-data-consent-semweb-gdpr-compliance",
    #     #     # "link": "https://zenodo.org/records/3795514/files/PhD_Thesis_submitted_hardbound.pdf",
    #     #     "scholar": "https://scholar.google.com.br/scholar?cites=7232081120271493220&as_sdt=2005&sciodt=0,5&hl=en",
    #     #     "scholar_id": "ZGiXMHaDXWQJ",
    #     #     "scholar_ok": True,
    #     #     "start_set": True
    #     # }
    #     # {
    #     #     "target": "matulevicius2020a",
    #     #     "year": 2020,
    #     #     "name": "A Method for Managing GDPR Compliance in Business Processes",
    #     #     "due": "The document propose a extendend model to acheive compliance with GDPR",
    #     #     "display": "matulevicius",
    #     #     "authors": "Matulevicius, Raimundas and Tom, Jake and Kala, Kaspar and Sing, Eduard",
    #     #     "place": "CAiSE",
    #     #     "ID": "matulevivcius2020method",
    #     #     "category": "ok",
    #     #     "cluster_id": "14432861032546387089",
    #     #     "entrytype": "inproceedings",
    #     #     "link": "https://www.researchgate.net/profile/Raimundas-Matulevicius/publication/343930785_A_Method_for_Managing_GDPR_Compliance_in_Business_Processes/links/605b19a592851cd8ce623228/A-Method-for-Managing-GDPR-Compliance-in-Business-Processes.pdf",
    #     #     "organization": "Springer",
    #     #     "pp": "100--112",
    #     #     "scholar": "https://scholar.google.com/scholar?cites=14432861032546387089&as_sdt=2005&sciodt=0,5&hl=en",
    #     #     "scholar_id": "kUSB-aPSS8gJ",
    #     #     "scholar_ok": True,
    #     #     "forward_steps": 1
    #     # }
       {
            "target": "matulevicius2020a",
            "year": 2020,
            "name": "A Method for Managing GDPR Compliance in Business Processes",
            "due": "The document propose a extendend model to acheive compliance with GDPR",
            "display": "matulevicius",
            "authors": "Matulevicius, Raimundas and Tom, Jake and Kala, Kaspar and Sing, Eduard",
            "place": "CAiSE",
            "ID": "matulevivcius2020method",
            "category": "ok",
            "cluster_id": "14432861032546387089",
            "entrytype": "inproceedings",
            "link": "https://pdfs.semanticscholar.org/0d51/bc5037b8bee12eecdc40042d5688fc96f98d.pdf",
            "organization": "Springer",
            "pp": "100--112",
            "scholar": "https://scholar.google.com/scholar?cites=14432861032546387089&as_sdt=2005&sciodt=0,5&hl=en",
            "scholar_id": "kUSB-aPSS8gJ",
            "scholar_ok": True,
            "forward_steps": 1
        },
        {
            "target": "bonatti2018b",
            "year": 2018,
            "name": "Data privacy vocabularies and controls: Semantic web for transparency and privacy",
            "due": "This document proposes a privacy ontology to represent the concepts around an application (i.e.,  Innovation Ethics) that can contain personal data. It thus has no relation to GDPR and has been discarded.",
            "display": "bonatti",
            "authors": "Bonatti, Piero A and Bos, Bert and Decker, Stefan and Fern\u00e1ndez, Javier D and Kirrane, Sabrina and Peristeras, Vassilios and Polleres, Axel and Wenning, Rigo",
            "place": "SW4SG",
            "ID": "bonatti2018data",
            "category": "unrelated",
            "cluster_id": "14663434318177827862",
            "entrytype": "inproceedings",
            "link": "https://research.wu.ac.at/files/21761326/SW4SG_2018.pdf",
            "scholar": "https://scholar.google.com/scholar?cites=14663434318177827862&as_sdt=2005&sciodt=0,5&hl=en",
            "scholar_id": "FvxCetL7fssJ",
            "scholar_ok": True,
            "backward_steps": 1
        },
        {
            "target": "bonatti2018d",
            "year": 2018,
            "name": "The SPECIAL Policy Log Vocabulary",
            "due": "Discarded due to this document was not made publicly available.",
            "display": "bonatti",
            "authors": " Piero Bonatti, Wouter Dullaert, Javier D. Fern\u00e1ndez, Sabrina Kirrane, Milosevic, Axel Polleres ",
            "place": "Web",
            "ID": "TheSPECI5:online",
            "entrytype": "misc",
            "howpublished": "ttps://ai.wu.ac.at/policies/policylog/",
            "month": "3",
            "category": "ok",
            "backward_steps": 1
        },
        {
            "target": "kirrane2018a",
            "year": 2018,
            "name": "A scalable consent, transparency and compliance architecture",
            "due": "Although the approach this document introduces presents a model where components are capable of representing the provenance of the activities related to GDPR, in this document, specifically, this model is not introduced. Thus, we consider this document unrelated.",
            "display": "kirrane",
            "authors": "Kirrane, Sabrina and Fern\u00e1ndez, Javier D and Dullaert, Wouter and Milosevic, Uros and Polleres, Axel and Bonatti, Piero A and Wenning, Rigo and Drozd, Olha and Raschke, Philip",
            "place": "ESWC",
            "ID": "kirrane2018scalable",
            "category": "ok",
            "entrytype": "inproceedings",
            "organization": "Springer",
            "pp": "131--136",
            "scholar": "https://scholar.google.com/scholar?cites=13808115522786291090&as_sdt=2005&sciodt=0,5&hl=pt-BR",
            "scholar_ok": "@inproceedings{kirrane2018scalable,\n  title={A scalable consent, transparency and compliance architecture},\n  author={Kirrane, Sabrina and Fern{\\'a}ndez, Javier D and Dullaert, Wouter and Milosevic, Uros and Polleres, Axel and Bonatti, Piero A and Wenning, Rigo and Drozd, Olha and Raschke, Philip},\n  booktitle={European Semantic Web Conference},\n  pages={131--136},\n  year={2018},\n  organization={Springer}\n}",
            "link": "https://research.wu.ac.at/files/19833040/ESWC2018.pdf",
            "backward_steps": 1
        },
        {
            "target": "tom2018a",
            "year": 2018,
            "name": "Conceptual representation of the GDPR: model and application directions",
            "due": "Although this approach proposes concepts for resenting the GDPR, it is not related to provenance.",
            "display": "tom",
            "authors": "Tom, Jake and Sing, Eduard and Matulevicius, Raimundas",
            "place": "BIR",
            "ID": "tom2018conceptual",
            "cluster_id": "11236335810691020005",
            "entrytype": "inproceedings",
            "link": "https://sci-hub.st/10.1007/978-3-319-99951-7_2",
            "organization": "Springer",
            "pp": "18--28",
            "scholar": "https://scholar.google.com/scholar?cites=11236335810691020005&as_sdt=2005&sciodt=0,5&hl=en",
            "scholar_id": "5TQ9HeN775sJ",
            "scholar_ok": True,
            "related": "Representation",
            "category": "ok",
            "backward_steps": 1
        },
        {
            "target": "besik2019a",
            "year": 2019,
            "name": "Ontology-Based Privacy Compliance Checking for Clinical Workflows.",
            "due": "This paper has proposed a compliance-check architecture based on Java technologies. This system was built under three ontologies: the first proposes terms for the privacy layer, suggesting classes to GDPR (in particular, purpose specifications, data minimization, processing compliant-checking, and limit of retention period), privacy policies, and privacy preferences (when the data subjects to determine who can access their data and for what purposes). To represent the activities, this approach has inherited Business Process Model and Notation (BPMN). Finally, the last ontology contains terms of the specific clinical domain.\n\nThe authors demonstrate that this approach can check compliance through the ministration of a Java-based open source business rule management system. They show the usability of this approach in the running process, which also illustrates how these three ontologies should work together.\n\nAlthough the compliance checker was built over a specific technology (that we probably will not utilize), we have considered the privacy ontology can contribute to the objective of our study. Indeed, this privacy ontology provides concepts to represent privacy policy constraints. Such information is required to answer the obligations we have aimed to achieve.\n\nIn face of this, we have included this article to see whether the proposed model was extended to meet further obligations.",
            "display": "besik",
            "authors": "Besik, Saliha Irem and Freytag, Johann-Christoph",
            "place": "LWDA",
            "ID": "besik2019ontology",
            "category": "ok",
            "cluster_id": "9953792441592462448",
            "entrytype": "inproceedings",
            "link": "https://ceur-ws.org/Vol-2454/paper_55.pdf",
            "pp": "218--229",
            "scholar": "https://scholar.google.com.br/scholar?cites=9953792441592462448&as_sdt=2005&sciodt=0,5&hl=en",
            "scholar_id": "cDwW-Xz5IooJ",
            "scholar_ok": True,
            "start_set": True,
            "useful": True,
            "not_directly_related_to_provenance": True
        }
    ]

    for pub in tqdm(publications):
        if pub.get('category').lower() == 'ok':
            summary = get_publication_summary(pub)
            pub_id = pub.get("target")
            
            with open(f"data/02-refined/{pub_id}.md", "w") as f:
                f.write(summary)
        else:
            logging.info(f"skip {pub}")
