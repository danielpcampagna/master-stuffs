# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2014 import garijo2014a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, garijo2014a, ref="Garijo, Daniel, and Yolanda Gil. 2014. “The P-PLAN Ontology.” March 12, 2014. http://vocab.linkeddata.es/p-plan/.",
    contexts=[],
))

