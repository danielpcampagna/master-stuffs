# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import vos2019a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, vos2019a, ref="Vos, Marina De, Sabrina Kirrane, Julian Padget, and Ken Satoh. 2019. “ODRL Policy Modelling and Compliance",
    contexts=[],
))

