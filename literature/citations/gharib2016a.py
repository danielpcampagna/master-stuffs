# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2016 import gharib2016a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, gharib2016a, ref="Gharib, Mohamad, Paolo Giorgini, and John Mylopoulos. 2016. “Ontologies for Privacy Requirements Engineering: A Systematic Literature Review,” November. http://arxiv.org/abs/1611.10097.",
    contexts=[],
))

