# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2016 import governatori2016a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, governatori2016a, ref="Governatori, Guido, Mustafa Hashmi, Ho-Pun Lam, Serena Villata, and Monica Palmirani. 2016. “Semantic Business Process Regulatory Compliance Checking Using LegalRuleML.” In Knowledge Engineering and Knowledge Management, edited by Eva Blomqvist, Paolo Ciancarini, Francesco Poggi, and Fabio Vitali, 746–61. Lecture Notes in Computer Science. Springer International Publishing.",
    contexts=[],
))

