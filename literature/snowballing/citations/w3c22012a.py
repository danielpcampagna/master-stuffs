# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2012 import w3c22012a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, w3c22012a, ref="“OWL 2.” 2012. OWL 2 Web Ontology Language Document Overview (Second Edition). December 11, 2012. https://www.w3.org/TR/owl2-overview/.",
    contexts=[],
))

