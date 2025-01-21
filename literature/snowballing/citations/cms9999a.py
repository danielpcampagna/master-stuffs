# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2020 import pandit2020a

from ..work.y9999 import cms9999a


DB(Citation(
    pandit2020a, cms9999a, ref="“GDPR Enforcement Tracker - List of GDPR Fines.” 2019. 2019. http://www.enforcementtracker.com.",
    contexts=[],
))

