# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import pandit2018c
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, pandit2018c, ref="Pandit, Harshvardhan J., Declan O’Sullivan, and Dave Lewis. 2018a. “An Ontology Design Pattern for Describing Personal Data in Privacy Policies.” In Proceedings of the 9th Workshop on Ontology Design and Patterns (WOP 2018) Co-Located with 17th International Semantic Web Conference (ISWC 2018). Monterey, California, USA. http://ceur-ws.org/Vol-2195/pattern_paper_3.pdf.",
    contexts=[],
))

