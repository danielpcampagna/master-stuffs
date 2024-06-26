# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import ujcich2018a

from ..work.y2018 import basin2018a
from ..work.y2020 import campagna2020a
from ..work.y2020 import pandit2020a


DB(Citation(
    ujcich2018a, basin2018a, ref="11. D. Basin, S. Debois, and T. Hildebrandt, “On purpose and by necessity: Compliance under the GDPR,” in Proceedings of Financial Cryptography and Data Security ’18, Mar. 2018.",
    contexts=[],
))



DB(Citation(
    campagna2020a, basin2018a, ref="Basin, D., Debois, S., and Hildebrandt, T. (2018). On purpose and by necessity: compliance under the gdpr. In International Conference on Financial Cryptography and Data Security, pages 20–37. Springer.",
    contexts=[],
))



DB(Citation(
    pandit2020a, basin2018a, ref="Basin, David, Søren Debois, and Thomas Hildebrandt. 2018. “On Purpose and by Necessity: Compliance Under the GDPR.” In Proceedings of Financial Cryptography and Data Security 2018, 18.",
    contexts=[],
))

