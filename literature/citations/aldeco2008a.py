# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2008 import aldeco2008a
from ..work.y2018 import ujcich2018a
from ..work.y2020 import campagna2020a


DB(Citation(
    ujcich2018a, aldeco2008a, ref="13. R. Aldeco-P´erez and L. Moreau, “Provenance-based auditing of private data use,” in Proceedings of Visions of Computer Science ’08, 2008, pp. 141–152.",
    contexts=[],
))


DB(Citation(
    campagna2020a, aldeco2008a, ref="Aldeco Perez, R. and Moreau, L. (2008). Provenance-based auditing of private data use. In BCS International Academic Conference.",
    contexts=[],
))

