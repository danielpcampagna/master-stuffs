# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2017 import robaldo2017a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, robaldo2017a, ref="Robaldo, Livio, and Xin Sun. 2017. “Reified Input/Output Logic: Combining Input/Output Logic and Reification to Represent Norms Coming from Existing Legislation.” Journal of Logic and Computation 27 (8): 2471–2503. https://doi.org/10/gf9jmn.",
    contexts=[],
))

