import re

from sql_metadata.token import SQLToken


camel_pat = re.compile(r"([A-Z])")
under_pat = re.compile(r"_([a-z])")


def camel_to_snake(name):
    return camel_pat.sub(lambda x: "_" + x.group(1).lower(), name)


def snake_to_camel(name):
    return under_pat.sub(lambda x: x.group(1).upper(), name)

def title(name: str):
    return name[0].upper() + name[1:]

def print_tokens(tokens: list[SQLToken]):
    result = []
    for i, t in enumerate(tokens):
        result.append(f"{i} {t}")
    return "\n".join(result)