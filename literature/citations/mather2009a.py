# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2009 import mather2009a
from ..work.y2017 import fatema2017a


DB(Citation(
    fatema2017a, mather2009a, ref="[5] Mather, T., Kumaraswamy, S. and Latif, S.: Cloud security and privacy: an enterprise perspective on risks and compliance. In. O'Reilly Media, Inc. (2009).",
    contexts=[],
))

