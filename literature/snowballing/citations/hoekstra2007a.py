# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2007 import hoekstra2007a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, hoekstra2007a, ref="Hoekstra, Rinke, Joost Breuker, Marcello Di Bello, Alexander Boer, and others. 2007. “The LKIF Core Ontology of Basic Legal Concepts.” LOAIT 321: 43–63.",
    contexts=[],
))

