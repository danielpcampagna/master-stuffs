# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import bartolini2018b
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, bartolini2018b, ref="Bartolini, Cesare, Gabriele Lenzini, and Cristiana Santos. 2019. “An Agile Approach to Validate a Formal Representation of the GDPR.” New Frontiers in Artificial Intelligence, 16.",
    contexts=[],
))

