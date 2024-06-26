# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2013 import grando2013a
from ..work.y2017 import fatema2017a


DB(Citation(
    fatema2017a, grando2013a, ref="[7] Grando, A. and Schwab, R.: Building and evaluating an ontology-based tool for reasoning about consent permission. In. AMIA annual symposium proceedings. Vol. 2013. American Medical Informatics Association, (2013).",
    contexts=[],
))

