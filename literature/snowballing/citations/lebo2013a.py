# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2013 import lebo2013a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, lebo2013a, ref="Lebo, Timothy, Satya Sahoo, Deborah McGuinness, Khalid Belhajjame, James Cheney, David Corsar, Daniel Garijo, Stian Soiland-Reyes, Stephan Zednik, and Jun Zhao. 2013. “PROV-O: The PROV Ontology.” 2013.",
    contexts=[],
))

