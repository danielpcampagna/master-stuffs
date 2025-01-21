# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import westphal2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, westphal2018a, ref="Westphal, Patrick, Javier D Fernandez, and Sabrina Kirrane. 2018. “SPIRIT: A Semantic Transparency and Compliance Stack.” In Proceedings of the 14th International Conference on Semantic Systems (SEMANTiCS), 4.",
    contexts=[],
))

