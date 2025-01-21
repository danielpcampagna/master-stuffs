# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2012 import bischof2012a
from ..work.y2017 import fatema2017a


DB(Citation(
    fatema2017a, bischof2012a, ref="[24] Bischof, S., Decker, S., Krennwallner, T., Lopes, N., Polleres, A.: Mapping between RDF and XML with XSPARQL. J. Data Semantics 1(3), 147-185 (2012)",
    contexts=[],
))

