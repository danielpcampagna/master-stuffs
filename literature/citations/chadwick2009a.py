# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2009 import chadwick2009a
from ..work.y2017 import fatema2017a


DB(Citation(
    fatema2017a, chadwick2009a, ref="[21] Chadwick, D. W., and Fatema, K.: An advanced policy based authorisation infrastructure. In. Proceedings of the 5th ACM work-shop on Digital identity management, DIM’09, pp.81-84, Chicago, Illinois, USA, (2009).",
    contexts=[],
))

