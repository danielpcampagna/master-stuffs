# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1995 import gruber1995a
from ..work.y2017 import fatema2017a


DB(Citation(
    fatema2017a, gruber1995a, ref="[17] Gruber, T.:Toward principles for the design of ontologies used for knowledge sharing. International Journal of Human-Computer Studies, 907–928, (1993).",
    contexts=[],
))

