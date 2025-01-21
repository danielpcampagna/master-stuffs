# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2006 import moor2006a
from ..work.y2017 import fatema2017a


DB(Citation(
    fatema2017a, moor2006a, ref="[19] de Moor, A., Leenheer, P. D., and Meersman, R.: DOGMA-MESS: A Meaning Evolution Support System for Interorganizational Ontology Engineering. In. Conceptual Structures: Inspiration and Application, 14th International Conference on Conceptual Structures",
    contexts=[],
))

