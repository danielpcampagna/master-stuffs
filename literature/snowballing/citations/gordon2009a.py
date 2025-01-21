# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2009 import gordon2009a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, gordon2009a, ref="Gordon, Thomas F., Guido Governatori, and Antonino Rotolo. 2009. “Rules and Norms: Requirements for Rule Interchange Languages in the Legal Domain.” In International Workshop on Rules and Rule Markup Languages for the Semantic Web, 282–96. Springer. https://doi.org/10/fwf8xf.",
    contexts=[],
))

