# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1995 import ozsoyoglu1995a
from ..work.y2020 import campagna2020a


DB(Citation(
    campagna2020a, ozsoyoglu1995a, ref="Ozsoyoglu, G. and Snodgrass, R. T. (1995). Temporal and real-time databases: A survey. IEEE Transactions on Knowledge and Data Engineering, 7(4):513–532.",
    contexts=[],
))

