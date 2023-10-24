import re
from dataclasses import dataclass

from sql_metadata import Parser
from sql_metadata.token import SQLToken
from pluralizer import Pluralizer

from helpers import *


pluralizer = Pluralizer()


@dataclass
class SimpleTriple:
    identifier: str
    type: str
    subclass: str
    comment: str
    label: str

    @staticmethod
    def from_sql(sql: str):
        return SimpleTripleFromSQLBuild(sql)

    def to_str(self, base_url: str):
        result = [
            f"### {base_url}#{self.identifier}",
            f":{self.identifier} rdf:type {self.type} ;",
            f"\trdfs:subClassOf {self.subclass} ;",
            f"\trdf:comment {self.comment} ;",
            f'\trdfs:label "{self.label}" .',
        ]
        return "\n".join(result)


class SimpleTripleFromSQLBuild:
    def create(sql: str) -> SimpleTriple:
        tk = Parser(sql).tokens

        result = []
        table_name = SimpleTripleFromSQLBuild.get_table_name(tk)

        for field in SimpleTripleFromSQLBuild._get_fields(tk):
            identifier = SimpleTripleFromSQLBuild._create_identifier(table_name, field.value)
            result.append(
                SimpleTriple(
                    identifier=title(snake_to_camel(identifier)),
                    type=SimpleTripleFromSQLBuild.get_type(tk),
                    subclass=SimpleTripleFromSQLBuild.get_subclass(field, tk),
                    comment=SimpleTripleFromSQLBuild.get_comment(field, tk),
                    label=identifier,
                )
            )
        return result
    
    @staticmethod
    def _create_identifier(table_name: str, field: str):
        return f"{title(snake_to_camel(pluralizer.singular(table_name)))}{title(snake_to_camel(field))}"

    @staticmethod
    def _get_fields(tokens: list[SQLToken]):
        for t in tokens:
            if SimpleTripleFromSQLBuild.is_field(t):
                yield t

    @staticmethod
    def is_field(t: SQLToken):
        return (
            t.is_name
            and t.parenthesis_level == 1
            and (t.previous_token.value == "," or t.previous_token.value == "(")
        )

    @staticmethod
    def get_table_name(tokens: list[SQLToken]):
        for t in tokens:
            if SimpleTripleFromSQLBuild.is_table_name(t):
                return t.value
        raise Exception(f"Table Name was not found in: \n{print_tokens(tokens)}")

    @staticmethod
    def is_table_name(t: SQLToken):
        return (
            t.is_name
            and t.next_token.value == "("
            and t.last_keyword.upper() == "TABLE"
            and t.parenthesis_level == 0
        )

    @staticmethod
    def get_type(*args, **kwargs):
        # Constant for awaile
        return "owl:Class"

    @staticmethod
    def get_subclass(field: SQLToken, tokens: list[SQLToken]):
        found = False
        for t in tokens:
            if t and t.value == field.value:
                found = True
            if found:
                if t.value == ",":
                    break
                if SimpleTripleFromSQLBuild.is_personal_attribute(t):
                    return ":PersonalData"
                if SimpleTripleFromSQLBuild.is_indirect_attribute(t):
                    return ":IndirectPersonalData"
        return ":NonPersonalData"

    @staticmethod
    def is_personal_attribute(t: SQLToken):
        # New syntax added to SQL
        return (
            t.value == "personal"
            and t.is_name
            and t.parenthesis_level == 1
            and t.previous_token != ","
        )

    @staticmethod
    def is_indirect_attribute(t: SQLToken):
        # New syntax added to SQL
        return (
            t.value == "indirect"
            and t.is_name
            and t.parenthesis_level == 1
            and t.previous_token != ","
        )

    @staticmethod
    def get_comment(field: str, tokens: list[SQLToken]):
        table_name = SimpleTripleFromSQLBuild.get_table_name(tokens)
        prefix = (
            "of an" if re.compile(r"^[aeiouh]").match(table_name.lower()) else "of a"
        )
        as_text = lambda s: s.replace("_", " ").lower()
        return f'"The {as_text(field.value)} {prefix} {pluralizer.singular(as_text(table_name))}"@en'


from pathlib import Path


def read_schema(path: str | Path):
    with open(path) as f:
        return f.read()


def split_schema_into_stmt(schema: str):
    return schema.split(";")


def normalize_stmt(stmt: str):
    return stmt.replace("\n", "")


def is_create_table(sql: str):
    return sql.startswith("CREATE TABLE")


def save_triples(
    ofile: str,
    triples: list[SimpleTriple],
    base_url: str = "https://www.example.org/my-triple",
):
    with open(ofile, "w") as f:
        for t in triples:
            try:
                f.write(f"\n\n{t.to_str(base_url)}\n")
            except:
                import pdb

                pdb.set_trace()


def create_triple(ifile: str, ofile: str, base_url: str):
    schema = read_schema(ifile)
    stmts = split_schema_into_stmt(schema)
    norm_stmt = [normalize_stmt(stmt) for stmt in stmts]
    create_stmt = [stmt for stmt in norm_stmt if is_create_table(stmt)]

    triples = []
    for stmt in create_stmt:
        triples.extend(SimpleTripleFromSQLBuild.create(stmt))

    save_triples(ofile, triples, base_url)


if __name__ == "__main__":
    ifile = "./data.schema.sql"
    ofile = f"./{ifile}.ttl"
    base_url = "https://example.org/TrinityCollegeDublin"
    create_triple(ifile, ofile, base_url)
