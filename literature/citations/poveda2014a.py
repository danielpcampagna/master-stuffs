# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2014 import poveda2014a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, poveda2014a, ref="International Journal on Semantic Web and Information Systems (IJSWIS)",
    contexts=[],
))

