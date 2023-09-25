import argparse


def extract(start_index, end_index, output, filename="sociallink.final.tql"):
    with open(filename) as fin:
        fin.seek(start_index)
        data = fin.read(end_index - start_index)
    
    with open(output, "w") as f:
        f.write(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("start", type=int)
    parser.add_argument("--end", type=int)
    parser.add_argument("--block", type=int, default=1_000_000)
    parser.add_argument("--output", default="output.ttl")
    parser.add_argument("--input", default="sociallink.final.tql")

    args = parser.parse_args()
    start, end = args.start, args.end
    if end is None: end = start + args.block
    output = args.output

    extract(start, end, output)