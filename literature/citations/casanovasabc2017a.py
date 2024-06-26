# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2017 import casanovasabc2017a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, casanovasabc2017a, ref="Casanovas, Pompeu, Jorge González-Conejero, and Louis de Koker. 2017. “Legal Compliance by Design (LCbD) and Through Design (LCtD): Preliminary Survey.” In Proceedings of the 1st Workshop on Technologies for Regulatory Compliance Co-Located with the 3",
    contexts=[],
))

