# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import gerl2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, gerl2018a, ref="Gerl, Armin, and Dirk Pohl. 2018. “Critical Analysis of LPL According to Articles 12 - 14 of the GDPR.” In Proceedings of the 13th International Conference on Availability, Reliability and Security - ARES 2018, 1–9. Hamburg, Germany: ACM Press. https",
    contexts=[],
))

