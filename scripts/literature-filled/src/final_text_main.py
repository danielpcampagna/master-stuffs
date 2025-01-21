import json
from functools import cache

import tqdm

from services.llm import generate_completion


def get_questions():
    with open("data/01-raw/questions.json") as f:
        return json.load(f)

def open_classification():
    with open("data/01-raw/transposed_classification.json") as f:
        return json.load(f)

@cache
def get_study_content(workid: str):
    with open(f"data/02-refined/{workid}.md") as f:
        return f.read()

if __name__ == "__main__":
    questions = get_questions()
    classification = open_classification()
    paragraphs = list()
    for question in tqdm.tqdm(classification):
        justifications = ""
        content = ""
        
        for workid in classification[question]:
            if classification[question][workid]["score"] >= 70:
                content += f"## {workid}\n\n{get_study_content(workid)}\n\n---\n\n"
                justifications += f"- {workid}: {classification[question][workid]['justification']}\n"
        
        prompt = f"""You are writing the related work section of you paper, that will be submitted for a highlevel scientific journal.
Please produce a unique paragraph for the question below : (1) explaining the relation between these studies with the question below and dicussing about the insufficiency of the study to address this question propertly.
As all scientifc text, every study referenced in the text must be referenced. To refer to a study, use the study identifier (e.g., [{workid}]).

# QUESTION:

{questions[question]}

# STUDIES

Each study and its explanation in terms of this question is presented in the following list:

{justifications}

# EXTRA CONTENT

If you think you need more information to produce this scientific text, the following subsections have a summary of each study:

{content}
"""
        
        answer = generate_completion(prompt).get("answer")
        paragraphs.append(answer)
    
    final_text = "\n\n---\n\n".join(paragraphs)
    with open("data/03-final-answer/final-result.full.md", "w") as f:
        f.write(final_text)
    
        