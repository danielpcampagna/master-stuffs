# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2016 import tankard2016a
from ..work.y2018 import ujcich2018a
from ..work.y2020 import campagna2020a


DB(Citation(
    ujcich2018a, tankard2016a, ref="2. C. Tankard, “What the GDPR means for businesses,” Network Security, vol. 2016, no. 6, pp. 5–8, 2016.",
    contexts=[],
))



DB(Citation(
    campagna2020a, tankard2016a, ref="Tankard, C. (2016). What the gdpr means for businesses. Network Security, 2016(6):5–8.",
    contexts=[],
))

