# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import palmirani2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, palmirani2018a, ref="Monica, Palmirani, Martoni Michele, Rossi Arianna, Bartolini Cesare, and Robaldo Livio. 2018. “Legal Ontology for Modelling GDPR Concepts and Norms.” Frontiers in Artificial Intelligence and Applications, 91–100. https://doi.org/10/gfr9qd.",
    contexts=[],
))

