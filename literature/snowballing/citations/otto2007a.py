# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2007 import otto2007a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, otto2007a, ref="Otto, Paul N., and Annie I. Anton. 2007. “Addressing Legal Requirements in Requirements Engineering.” In 15th IEEE International Requirements Engineering Conference (RE 2007), 5–14. IEEE. https://doi.org/10/d4rpf3.",
    contexts=[],
))

