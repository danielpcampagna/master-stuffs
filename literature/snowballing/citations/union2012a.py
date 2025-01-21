# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2012 import union2012a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, union2012a, ref="“Council Conclusions Inviting the Introduction of the European Legislation Identifier (ELI).” 2012. Official Journal of the European Union 325 (3): 3–11. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:52012XG1026(01).",
    contexts=[],
))

