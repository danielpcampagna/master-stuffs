# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2014 import labda2014a
from ..work.y2019 import besik2019a


DB(Citation(
    besik2019a, labda2014a, ref="Wadha Labda, Nikolay Mehandjiev, and Pedro Sampaio. Modeling of privacy-aware business processes in BPMN to protect personal data. In Proc. of the 29thAnnual ACM Symposium on Applied Computing, pages 1399–1405. ACM, 2014.",
    contexts=[],
))

