# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import pandit2018d
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, pandit2018d, ref="Pandit, Harshvardhan J, Declan O’Sullivan, and Dave Lewis. 2018c. “Towards Knowledge-Based Systems for GDPR Compliance.” In Proceedings of the Joint Proceedings of the International Workshops on Contextualized Knowledge Graphs, and Semantic Statistics (CKGSemStats). Monterey, California, USA. http://ceur-ws.org/Vol-2317/article-09.pdf.",
    contexts=[],
))

