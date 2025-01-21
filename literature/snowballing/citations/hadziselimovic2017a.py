# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2017 import hadziselimovic2017a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, hadziselimovic2017a, ref="Hadziselimovic, Ensar, Kaniz Fatema, Harshvardhan J. Pandit, and Dave Lewis. 2017. “Linked Data Contracts to Support Data Protection and Data Ethics in the Sharing of Scientific Data.” In Proceedings of the First Workshop on Enabling Open Semantic Science (SemSci), 55–62. http://ceur-ws.org/Vol-1931/paper-08.pdf.",
    contexts=[],
))

