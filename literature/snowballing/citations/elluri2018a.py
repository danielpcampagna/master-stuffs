# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import elluri2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, elluri2018a, ref="Elluri, L., A. Nagar, and K. P. Joshi. 2018. “An Integrated Knowledge Graph to Automate GDPR and PCI DSS Compliance.” In 2018 IEEE International Conference on Big Data (Big Data), 1266–71. https://doi.org/10/gf3cx9.",
    contexts=[],
))

