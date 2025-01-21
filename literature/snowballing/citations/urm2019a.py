# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import urm2019a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, urm2019a, ref="Dellas, Nikolaos. 2019. “D2.3 Initial Specification of BPR4GDPR Architecture.” BPR4GDPR.",
    contexts=[],
))

