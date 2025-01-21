"""This version uses the """


import json
from functools import cache

import tqdm

from services.llm import generate_completion


def get_questions():
    with open("data/01-raw/questions.json") as f:
        return json.load(f)

def open_classification():
    with open("data/03-final-answer/classification.json") as f:
        return json.load(f)

@cache
def get_study_content(workid: str):
    with open(f"data/02-refined/{workid}.md") as f:
        return f.read()

if __name__ == "__main__":
    questions = get_questions()
    classification = open_classification()
    paragraphs = list()
    for workid in tqdm.tqdm(classification):
        justifications = ""
        study_content = ""
        
        for question in classification[workid]:
            if classification[workid][question]["score"] >= 75:
                justifications += f"## {question}: {questions[question]}\n{classification[workid][question]['justification']}\n\n"
                # justifications += f"- {question}: {classification[workid][question]['justification']}\n"
                study_content += f"## {workid}\n\n{get_study_content(workid)}\n\n---\n\n"
        
        prompt = f"""You are writing the related work section of you paper, that will be submitted for a highlevel scientific journal.
Please produce a paragraph for the study below explaning the relation between this study with each questions below and (use the justifications below) discuss the insufficiency for this study to be used to address each question propertly.
As all scientifc text, every study cited in the text must be referenced. To refer to a study, use the question identifier (e.g., [{workid}]).

# STUDY::

{study_content}

----

# QUESTIONS:

The justification for the use of this study to address this question is presented in the following subsections:

{justifications}
"""
        
        answer = generate_completion(prompt).get("answer")
        paragraphs.append(answer)
    
    final_text = "\n\n---\n\n".join(paragraphs)
    with open("data/03-final-answer/final-result-v2.full.md", "w") as f:
        f.write(final_text)
    
        