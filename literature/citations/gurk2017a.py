# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2017 import gurk2017a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, gurk2017a, ref="Gurk, Silvio Mc, Charlie Abela, and Jeremy Debattista. 2017. “Towards Ontology Quality Assessment.” Joint Proceedings of the MEPDaW, 12.",
    contexts=[],
))

