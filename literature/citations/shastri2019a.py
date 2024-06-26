# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import shastri2019a
from ..work.y2020 import campagna2020a


DB(Citation(
    campagna2020a, shastri2019a, ref="Shastri, S., Banakar, V., Wasserman, M., Kumar, A., and Chidambaram, V. (2019). Understanding and benchmarking the impact of gdpr on database systems. arXiv preprint arXiv:1910.00728.",
    contexts=[],
))

