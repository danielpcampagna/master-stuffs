# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2020 import pandit2020a

from ..work.y9999 import pandit9999a


DB(Citation(
    pandit2020a, pandit9999a, ref="Pandit, Harshvardhan J., and Axel Polleres. 2019. “DPV.” Data Privacy Vocabulary V0.1. July 26, 2019. https://www.w3.org/ns/dpv.",
    contexts=[],
))

