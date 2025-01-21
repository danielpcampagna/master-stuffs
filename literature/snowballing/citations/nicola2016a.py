# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2016 import nicola2016a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, nicola2016a, ref="De Nicola, Antonio, and Michele Missikoff. 2016. “A Lightweight Methodology for Rapid Ontology Engineering.” Communications of the ACM 59 (3): 79–86. https://doi.org/10/gftgpt.",
    contexts=[],
))

