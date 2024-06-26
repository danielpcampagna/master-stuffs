# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2020 import pandit2020a

from ..work.y9999 import privacy9999a


DB(Citation(
    pandit2020a, privacy9999a, ref="“Scalable Policy-Aware Linked Data Architecture for Privacy, Transparency and Compliance (SPECIAL).” 2019. 2019. https://www.specialprivacy.eu/.",
    contexts=[],
))

