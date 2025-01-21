# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import pandit2019b
from ..work.y2020 import campagna2020a
from ..work.y2020 import pandit2020a


DB(Citation(
    campagna2020a, pandit2019b, ref="Pandit, H. J., O’Sullivan, D., and Lewis, D. (2019). Test-driven approach towards gdpr compliance. In Acosta, M., Cudré-Mauroux, P., Maleshkova, M., Pellegrini, T., Sack, H., and Sure-Vetter, Y., editors, Semantic Systems. The Power of AI and Knowledge ",
    contexts=[],
))



DB(Citation(
    pandit2020a, pandit2019b, ref="Pandit, Harshvardhan J, Declan O’Sullivan, and Dave Lewis. 2019. “Test-Driven Approach Towards GDPR Compliance.” In 15th International Conference on Semantic Systems (SEMANTiCS2019). Karlsruhe, Germany.",
    contexts=[],
))

