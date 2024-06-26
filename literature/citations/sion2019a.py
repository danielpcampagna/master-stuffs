# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import sion2019a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, sion2019a, ref="Sion, L., P. Dewitte, D. Van Landuyt, K. Wuyts, I. Emanuilov, P. Valcke, and W. Joosen. 2019. “An Architectural View for Data Protection by Design.” In 2019 IEEE International Conference on Software Architecture (ICSA), 11–20. https://doi.org/10/gf3czd.",
    contexts=[],
))

