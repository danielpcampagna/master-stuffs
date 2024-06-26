# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2010 import rahmouni2010a
from ..work.y2019 import besik2019a


DB(Citation(
    besik2019a, rahmouni2010a, ref="10. Hanene Boussi Rahmouni, Tony Solomonides, Marco Casassa Mont, and SimonShiu. Privacy compliance and enforcement on European healthgrids: an approachthrough ontology. Philosophical Transactions of the Royal Society A: Mathemati-cal, Physical and Engineering Sciences, 368(1926):4057–4072, 2010.",
    contexts=[],
))

