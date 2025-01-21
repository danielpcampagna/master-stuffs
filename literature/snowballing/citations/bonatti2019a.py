# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import bonatti2019a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, bonatti2019a, ref="Bonatti, Piero A, Iliana M Petrova, and Luigi Sauro. 2019. “A Richer Policy Language for GDPR Compliance.” In Proceedings of the 32nd International Workshop on Description Logics, 12. Oslo, Norway.",
    contexts=[],
))

