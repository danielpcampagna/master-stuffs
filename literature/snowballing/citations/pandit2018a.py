# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import pandit2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, pandit2018a, ref="Pandit, Harshvardhan J, Declan O’Sullivan, and Dave Lewis. 2018d. “Queryable Provenance Metadata for GDPR Compliance.” In Procedia Computer Science, 137:262–68. Proceedings of the 14th International Conference on Semantic Systems 10th – 13th of September 2018 Vienna, Austria. https://doi.org/10/gfdc6r.",
    contexts=[],
))

