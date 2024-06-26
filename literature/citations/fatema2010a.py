# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2010 import fatema2010a
from ..work.y2017 import fatema2017a


DB(Citation(
    fatema2017a, fatema2010a, ref="[22] Fatema, K., Chadwick, D.W. and Lievens, S.: A Multi Privacy Policy Enforcement System. In. Privacy and Identity, IFIP AICT 352, pp. 297–310.(2011).",
    contexts=[],
))

