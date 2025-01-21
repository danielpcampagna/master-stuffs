# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2015 import w3c2015a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, w3c2015a, ref="“Semantic Web - W3C.” 2015. 2015. https://www.w3.org/standards/semanticweb/.",
    contexts=[],
))

