# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2008 import russello2008a
from ..work.y2017 import fatema2017a


DB(Citation(
    fatema2017a, russello2008a, ref="[14] Russello, G., Dong, C. and Dulay, N.: Consent-based workflows for healthcare management. Policies for Distributed Systems and Networks, 2008. POLICY 2008. IEEE Workshop on. IEEE, (2008).",
    contexts=[],
))

