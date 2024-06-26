# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import besik2019a
from ..work.y2020 import besik2020a


DB(Citation(
    besik2020a, besik2019a, ref="",
    contexts=[],
))

