# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2011 import nissenbaum2011a
from ..work.y2017 import fatema2017a


DB(Citation(
    fatema2017a, nissenbaum2011a, ref="[6] Nissenbaum, H.: A Contextual Approach to Privacy Online. Daedalus 140 (4), 32-48 (2011).",
    contexts=[],
))

