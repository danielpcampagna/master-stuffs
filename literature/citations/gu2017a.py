# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2017 import gu2017a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, gu2017a, ref="Spindler, Gerald, Anna Zsófia Horváth, and Lukas Dalby. 2017. “D3.1 General Legal Aspects.”",
    contexts=[],
))

