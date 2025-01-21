# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import debruyne2019a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, debruyne2019a, ref="Debruyne, C., H. J. Pandit, D. Lewis, and D. O’Sullivan. 2019. “Towards Generating Policy-Compliant Datasets.” In 2019 IEEE 13th International Conference on Semantic Computing (ICSC), 199–203. https://doi.org/10/gfxgwx.",
    contexts=[],
))

