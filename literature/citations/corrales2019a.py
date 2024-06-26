# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import corrales2019a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, corrales2019a, ref="Corrales, Marcelo, Paulius Jurčys, and George Kousiouris. 2019. “Smart Contracts and Smart Disclosure: Coding a GDPR Compliance Framework.” In Legal Tech, Smart Contracts and Blockchain, 189–220. Springer.",
    contexts=[],
))

