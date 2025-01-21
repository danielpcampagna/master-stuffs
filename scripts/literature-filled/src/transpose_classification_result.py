import json
import yaml

if __name__ == "__main__":
    result = dict()
    
    with open("data/03-final-answer/classification.json") as f:
        classification = json.load(f)
    
    for work in classification:
        for cq in classification[work]:
            if cq not in result:
                result[cq] = dict()
            result[cq][work] = classification[work][cq]
    
    with open("data/01-raw/transposed_classification.json", "w") as f:
        json.dump(result, f)
        