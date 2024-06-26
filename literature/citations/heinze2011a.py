# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2011 import heinze2011a
from ..work.y2017 import fatema2017a


DB(Citation(
    fatema2017a, heinze2011a, ref="[10] Heinze, O., et al.: Architecture of a consent management suite and integration into IHEbased regional health information networks. BMC medical informatics and decision making,11- 58. (2011).",
    contexts=[],
))

