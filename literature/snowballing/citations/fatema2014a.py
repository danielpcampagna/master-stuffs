# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2014 import fatema2014a
from ..work.y2017 import fatema2017a


DB(Citation(
    fatema2017a, fatema2014a, ref="[23] Fatema, K. and Chadwick, D.: Resolving Policy Conflicts - Integrating Policies from Multiple Authors. In. CAiSE International Workshops, Thessaloniki, Greece, (2014).",
    contexts=[],
))

