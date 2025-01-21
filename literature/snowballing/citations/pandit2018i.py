# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import pandit2018i
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, pandit2018i, ref="Pandit, Harshvardhan J., Christophe Debruyne, Declan O’Sullivan, and Dave Lewis. 2018. “An Exploration of Data Interoperability for GDPR.” International Journal of Standardization Research (IJSR) 16 (1): 1–21. https://doi.org/10/gfsn52.",
    contexts=[],
))

