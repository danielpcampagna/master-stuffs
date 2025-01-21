# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2013 import harris2013a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, harris2013a, ref="“SPARQL 1.1 Query Language.” 2013. 2013. https://www.w3.org/TR/sparql11-query/.",
    contexts=[],
))

