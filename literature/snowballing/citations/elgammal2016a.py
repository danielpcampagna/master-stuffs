# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2016 import elgammal2016a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, elgammal2016a, ref="Elgammal, Amal, Oktay Turetken, Willem-Jan van den Heuvel, and Mike Papazoglou. 2016. “Formalizing and Appling Compliance Patterns for Business Process Compliance.” Software & Systems Modeling 15 (1): 119–46. https://doi.org/10/gfzrgw.",
    contexts=[],
))

