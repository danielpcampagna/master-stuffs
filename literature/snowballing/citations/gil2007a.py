# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2007 import gil2007a
from ..work.y2019 import besik2019a


DB(Citation(
    besik2019a, gil2007a, ref="7. Yolanda Gil, William K Cheung, Varun Ratnakar, and Kai-kin Chan. Privacyenforcement in data analysis workﬂows. In Proceedings of the 2007 InternationalConference on Privacy Enforcement and Accountability with Semantics-Volume320, pages 41–48. Citese",
    contexts=[],
))

