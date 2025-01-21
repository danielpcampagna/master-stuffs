# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2016 import kung2016a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, kung2016a, ref="“Privacy and Security by Design Methodology Handbook.” 2015. PRIPARE. http://pripareproject.eu/wp-content/uploads/2013/11/PRIPARE-Methodology-Handbook-Final-Feb-24-2016.pdf.",
    contexts=[],
))

