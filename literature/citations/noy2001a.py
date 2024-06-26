# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2001 import noy2001a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, noy2001a, ref="Noy, Natalya F, Deborah L McGuinness, and others. 2001. “Ontology Development 101: A Guide to Creating Your First Ontology.” Stanford knowledge systems laboratory technical report KSL-01-05 and ….",
    contexts=[],
))

