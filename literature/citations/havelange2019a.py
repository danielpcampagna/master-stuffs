# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import havelange2019a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, havelange2019a, ref="Havelange, Nadine, Michel Dumontier, Birgit Wouters, Jona Linde, David Townend, Arno Riedl, and Visara Urovi. 2019. “LUCE: A Blockchain Solution for Monitoring Data License accoUntability and CompliancE,” August. http://arxiv.org/abs/1908.02287.",
    contexts=[],
))

