"""
Este modulo resume os resultados dos estudos analisando gerados a partir do script `rag_langchain_main.py`
"""

import glob

import yaml
    
from services.llm import summarize_markdown_files


if __name__ == "__main__":
    markdown_files = list(file for file in glob.glob("data/02-refined/*.md"))

    user_prompt = """The markdown content below describes an approach in the literature addressing the problems introduced by GDPR (data protection law) through the use of some conceptual model. This descrition includes the relation with the six question below.

Based exclusively on this provided approach description, give a score from 0 (zero) to 100 (one hundred) for each question below. The score should be close to 100, if this approach contributes positively to answer the question. The score should be close to 0, if this approach cannot contribute positively to answer the question. Restrict your answer exclusively to the content presented the markdown content. If it is not possible to provide some score, then do not provide it.

Your answer should be a json, as the following template:

# ANSWER TEMPLATE:

{
    "Question 8": {
        "score": {{The approach score for the Question 8}},
        "justification": {{Up to two paragraphs explaining why this score}}
    }
    "Question 28": {
        "score": {{The approach score for the Question 28}},
        "justification": {{Up to two paragraphs explaining why this score}}
    },
    "Question 29": {
        "score": {{The approach score for the Question 29}},
        "justification": {{Up to two paragraphs explaining why this score}}
    },
    "Question 51": {
        "score": {{The approach score for the Question 51}},
        "justification": {{Up to two paragraphs explaining why this score}}
    },
    "Question 63": {
        "score": {{The approach score for the Question 63}},
        "justification": {{Up to two paragraphs explaining why this score}}
    },
    "Question 64": {
        "score": {{The approach score for the Question 64}},
        "justification": {{Up to two paragraphs explaining why this score}}
    },
}

# QUESTIONS:

- **Question 8**: For each category of personal data, list the period for which the data will be retained e.g. one month? one year? As a general rule data must be retained for no longer than is necessary for the purpose for which it was collected in the first place.

- **Question 28**: Are procedures in place to ensure personal data is kept up to date and accurate and where a correction is required, the necessary changes are made without delay?

- **Question 29**: Are retention policies and procedures in place to ensure data are held for no longer than is necessary for the purposes for which they were collected?

- **Question 51**: Are personal data systematically destroyed, erased, or anonymized when they are no longer legally required to be retained.

- **Question 63**: Are all transfers listed - including answers to the previous questions (e.g. the nature of the data, the purpose of the processing, from which country the data is exported and which country receives the data and who the recipient of the transfer is?)

- **Question 64**: Is there a legal basis for the transfer, e.g. EU Commission adequacy decision; standard contractual clauses. Are these bases documented?
    
    """

    summary = summarize_markdown_files(markdown_files, user_prompt)
    # with open("data/03-final-answer/classification.md", "w") as f:
    #     f.write(summary)
    import json
    with open("data/03-final-answer/classification.json", "w") as f:
        json.dump(summary, f)
        
        
        
        
##############################