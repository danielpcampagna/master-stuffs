# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import pandit2018b
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, pandit2018b, ref="Pandit, Harshvardhan J, Declan O’Sullivan, and Dave Lewis. 2018b. “Exploring GDPR Compliance over Provenance Graphs Using SHACL.” In Proceedings of the Posters and Demos Track of the 14th International Conference on Semantic Systems Co-Located with the 14th International Conference on Semantic Systems (SEMANTiCS 2018). Vienna, Austria. http://ceur-ws.org/Vol-2198/paper_120.pdf.",
    contexts=[],
))

