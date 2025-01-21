# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2010 import mont2010a
from ..work.y2017 import fatema2017a


DB(Citation(
    fatema2017a, mont2010a, ref="[11] Mont, M. C., et al.: A conceptual model for privacy policies with consent and revocation requirements. In. IFIP PrimeLife International Summer School on Privacy and Identity Management for Life, Springer Berlin Heidelberg, (2010).",
    contexts=[],
))

