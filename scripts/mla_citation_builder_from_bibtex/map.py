import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("data/map/map.csv", sep=";")
    with open("data/map/from.txt") as f:
        content = f.read()
    for _, row in df.iterrows():
        _from, _to = row
        # if _from not in content:
        #     print(f"skiping {_from}")
        #     continue
        content = content.replace(_from, _to)
    
    with open("data/map/to.txt", "w") as f:
        f.write(content)
    