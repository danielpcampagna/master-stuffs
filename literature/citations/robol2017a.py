# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2017 import robol2017a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, robol2017a, ref="Robol, Marco, Mattia Salnitri, and Paolo Giorgini. 2017. “Toward GDPR-Compliant Socio-Technical Systems: Modeling Language and Reasoning Framework.” In The Practice of Enterprise Modeling, 236–50. Lecture Notes in Business Information Processing. Springer, Cham. https://doi.org/10/gfxvs7.",
    contexts=[],
))

