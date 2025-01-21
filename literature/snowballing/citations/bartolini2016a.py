# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2016 import bartolini2016a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, bartolini2016a, ref="Bartolini, Cesare, Gabriele Lenzini, and Livio Robaldo. 2016. “Towards Legal Compliance by Correlating Standards and Laws with a Semi-Automated Methodology.” In Proceedings of the 28 Benelux Conference on Artificial Intelligence (BNAIC). http://orbilu.uni.lu/handle/10993/28957.",
    contexts=[],
))

