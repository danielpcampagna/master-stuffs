# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2015 import belaazi2015a
from ..work.y2019 import besik2019a


DB(Citation(
    besik2019a, belaazi2015a, ref="11. Maherzia Belaazi, Hanen Boussi Rahmouni, and Adel Bouhoula. An OntologyRegulating Privacy Oriented Access Controls. In Int. Conf. on Risks and Securityof Internet and Systems, pages 17–35. Springer, 2015",
    contexts=[],
))

