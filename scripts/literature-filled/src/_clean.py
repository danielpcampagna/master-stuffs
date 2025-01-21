"""Clean refined files which conent is just 'Category is not 'ok'. No summary generated.'"""
import os
import glob

import tqdm


if __name__ == "__main__":
    for file in tqdm.tqdm(glob.glob("data/02-refined/*.md")):
        with open(file) as f:
            if f.read() == "Category is not 'ok'. No summary generated.":
                os.remove(file)