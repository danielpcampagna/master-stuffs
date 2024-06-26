# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2017 import kirrane2017a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, kirrane2017a, ref="Kirrane, Sabrina, Alessandra Mileo, and Stefan Decker. 2016. “Access Control and the Resource Description Framework: A Survey.” Edited by Bernardo Cuenca Grau. Semantic Web 8 (2): 311–52. https://doi.org/10/gfxvr7.",
    contexts=[],
))

