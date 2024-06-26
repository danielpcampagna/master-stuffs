# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import bartolini2019a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, bartolini2019a, ref="Bartolini, Cesare, Antonello Calabró, and Eda Marchetti. 2019. “Enhancing Business Process Modelling with Data Protection Compliance: An Ontology-Based Proposal:” In Proceedings of the 5th International Conference on Information Systems Security and Privacy, 421–28. Prague, Czech Republic: SCITEPRESS - Science and Technology Publications. https://doi.org/10/gf3czj.",
    contexts=[],
))

