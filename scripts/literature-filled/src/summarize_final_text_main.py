import json
from functools import cache

import tqdm

from services.llm import generate_completion


def get_structured_final_text():
    # with open("data/03-final-answer/final-result.v8.json") as f:
    with open("data/03-final-answer/final-result.full.md.json") as f:
        return json.load(f)

if __name__ == "__main__":
    
    final_text = get_structured_final_text()
        
    prompt = f"""You are writing the related work chapter of you scientifc paper, that will be submitted for a highlevel scientific journal.
        
Each item of the JSON below contains part of final this related work chapter (related to a question).

JSON:
{json.dumps(final_text)}

Summarize the text in the JSON keeping each question in a unique largue paragraph. Each paragraph you produce should contains the dicussion about the insufficiency of these studies to address this question propertly, present in the JSON.

Your final text should be a scientific text. This text must seem to be produced by a humam; hence, it follow the rules:

1. DO NOT BE REPETITIVE (specially introducing the same study every paragraph);
2. Use synonyms, when citing the same study again;
3. The number of words in each paragraph should be drastically different (varianting between 100 and 500);
4. If you feel a paragraph is too large, break it in to small ones.
        """
        
    summary = generate_completion(prompt).get("answer")
    with open("data/03-final-answer/final-result.summary.md", "w") as f:
        f.write(summary)
