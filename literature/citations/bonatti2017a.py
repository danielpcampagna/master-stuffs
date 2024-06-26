# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2017 import bonatti2017a
from ..work.y2018 import ujcich2018a
from ..work.y2020 import campagna2020a


DB(Citation(
    ujcich2018a, bonatti2017a, ref="7. P. Bonatti, S. Kirrane, A. Polleres, and R. Wenning, “Transparent personal data processing: The road ahead,” in Proceedings of Computer Safety, Reliability, and Security. Springer, 2017, pp. 337–349.",
    contexts=[],
))



DB(Citation(
    campagna2020a, bonatti2017a, ref="Bonatti, P., Kirrane, S., Polleres, A., and Wenning, R. (2017). Transparent personal data processing: The road ahead. In International Conference on Computer Safety, Reliability, and Security, pages 337–349. Springer.",
    contexts=[],
))

