# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2013 import fatema2013a
from ..work.y2017 import fatema2017a


DB(Citation(
    fatema2017a, fatema2013a, ref="[16] Fatema K.: Adding Privacy Protection to Policy Based Authorisation Systems. , PhD thesis, 2013, https://kar.kent.ac.uk/47905/",
    contexts=[],
))

