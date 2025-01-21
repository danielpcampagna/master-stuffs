# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2016 import dalpiaz2016a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, dalpiaz2016a, ref="Dalpiaz, Fabiano, Elda Paja, and Paolo Giorgini. 2016. Security Requirements Engineering: Designing Secure Socio-Technical Systems. MIT Press.",
    contexts=[],
))

