# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import palmirani2018c
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, palmirani2018c, ref="Palmirani, Monica, Michele Martoni, Arianna Rossi, Cesare Bartolini, and Livio Robaldo. 2018a. “PrOnto: Privacy Ontology for Legal Compliance.” In Proceedings of the 18th European Conference on Digital Government ECDG 2018, 10.",
    contexts=[],
))

