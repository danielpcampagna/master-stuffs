"""Merge all refined files"""
import os
import glob

import tqdm


if __name__ == "__main__":
    target = "data/02-refined/MERGED_WORK.md"
    for file in tqdm.tqdm(glob.glob("data/02-refined/*.md")):
        with open(file) as f:
            if f.read() == "Category is not 'ok'. No summary generated.":
                os.remove(file)