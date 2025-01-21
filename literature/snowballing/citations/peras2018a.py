# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import peras2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, peras2018a, ref="Peras, Dijana. 2018. “Guidelines for GDPR Compliant Consent and Data Management Model in ICT Businesses.” In 29th International Conference of Central European Conference on Information and Intelligent Systems, 9.",
    contexts=[],
))

