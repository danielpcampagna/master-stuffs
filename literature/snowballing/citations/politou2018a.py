# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import politou2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, politou2018a, ref="Politou, Eugenia, Efthimios Alepis, and Constantinos Patsakis. 2018. “Forgetting Personal Data and Revoking Consent Under the GDPR: Challenges and Proposed Solutions.” Journal of Cybersecurity 4 (1). https://doi.org/10/gfsqrg.",
    contexts=[],
))

