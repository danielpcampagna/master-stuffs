# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2017 import smes2017a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, smes2017a, ref="“GDPR Readiness Checklist Template for SMEs.” 2017. Data Protection Commissioner, Ireland.",
    contexts=[],
))

