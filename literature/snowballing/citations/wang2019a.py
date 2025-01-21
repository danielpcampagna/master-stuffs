# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import wang2019a
from ..work.y2020 import campagna2020a


DB(Citation(
    campagna2020a, wang2019a, ref="Wang, L., Near, J. P., Somani, N., Gao, P., Low, A., Dao, D., and Song, D. (2019). Data capsule: A new paradigm for automatic compliance with data privacy regulations. In Heterogeneous Data Management, Polystores, and Analytics for Healthcare, pages 3–23. Springer.",
    contexts=[],
))

