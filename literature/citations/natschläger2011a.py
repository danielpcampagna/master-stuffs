# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2011 import natschläger2011a
from ..work.y2019 import besik2019a


DB(Citation(
    besik2019a, natschläger2011a, ref="3. Christine Natschl¨ager. Towards a BPMN 2.0 ontology. In International Workshopon Business Process Modeling Notation, pages 1–15. Springer, 2011.",
    contexts=[],
))

