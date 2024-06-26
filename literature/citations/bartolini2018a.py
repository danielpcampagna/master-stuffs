# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import bartolini2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, bartolini2018a, ref="Bartolini, Cesare, Gabriele Lenzini, and Cristiana Santos. 2018. “A Legal Validation of a Formal Representation of GDPR Articles.” In Proceedings of the 2nd Workshop on Technologies for Regulatory Compliance Co-Located with the 31st International Conference on Legal Knowledge and Information Systems (JURIX 2018), 14. Groningen, Netherlands.",
    contexts=[],
))

