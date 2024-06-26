# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2020 import pandit2020a

from ..work.y2020 import leone2020a


DB(Citation(
    pandit2020a, leone2020a, ref="Leone, Valentina, Luigi Di Caro, and Serena Villata. 2019. “Taking Stock of Legal Ontologies: A Feature-Based Comparative Analysis.” Artificial Intelligence and Law, June. https://doi.org/10/gf3z84.",
    contexts=[],
))

