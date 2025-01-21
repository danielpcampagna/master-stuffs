# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2016 import fellmann2016a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, fellmann2016a, ref="Fellmann, Michael, and Andrea Zasada. 2014. “STATE-OF-THE-ART OF BUSINESS PROCESS COMPLIANCE APPROACHES.” Tel Aviv, 18.",
    contexts=[],
))

