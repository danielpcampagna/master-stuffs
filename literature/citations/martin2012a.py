# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2012 import martin2012a
from ..work.y2018 import ujcich2018a
from ..work.y2020 import campagna2020a


DB(Citation(
    ujcich2018a, martin2012a, ref="6. A. Martin, J. Lyle, and C. Namilkuo, “Provenance as a security control,” in Proceedings of the Theory and Practice of Provenance ’12. USENIX, 2012.",
    contexts=[],
))



DB(Citation(
    campagna2020a, martin2012a, ref="Martin, A. P., Lyle, J., and Namiluko, C. (2012). Provenance as a security control. In TaPP.",
    contexts=[],
))

