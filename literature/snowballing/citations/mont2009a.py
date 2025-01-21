# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2009 import mont2009a
from ..work.y2017 import fatema2017a


DB(Citation(
    fatema2017a, mont2009a, ref="[12] Mont, M. C., et al.: On the management of consent and revocation in enterprises: setting the context. HP Laboratories, Technical Report HPL-2009-49,( 2009).",
    contexts=[],
))

