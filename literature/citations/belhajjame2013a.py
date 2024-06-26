# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2013 import belhajjame2013a
from ..work.y2020 import campagna2020a


DB(Citation(
    campagna2020a, belhajjame2013a, ref="Garijo, D. and Gil, Y. (2013). P-Plan: The P-Plan ontology. W3C recommendation, W3C. https://www.opmw.org/model/p-plan17092013/.",
    contexts=[],
))

