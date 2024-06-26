# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2002 import spyns2002a
from ..work.y2017 import fatema2017a


DB(Citation(
    fatema2017a, spyns2002a, ref="[20] Spyns, P., Meersman, R. and Jarrar, M.: Data Modelling versus Ontology Engineering. SIGMOD Record 31(4), 12-17 (2002).",
    contexts=[],
))

