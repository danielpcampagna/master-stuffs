# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2012 import kuner2012a
from ..work.y2020 import campagna2020a


DB(Citation(
    campagna2020a, kuner2012a, ref="Kuner, C. (2012). The european commission’s proposed data protection regulation: A copernican revolution in european data protection law. Bloomberg BNA Privacy and Security Law Report (2012) February, 6(2012):1–15.",
    contexts=[],
))

