# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2014 import schreiber2014a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, schreiber2014a, ref="“RDF 1.1 Primer.” 2014. June 24, 2014. https://www.w3.org/TR/rdf11-primer/.",
    contexts=[],
))

