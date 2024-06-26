# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2017 import diamantopoulou2017a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, diamantopoulou2017a, ref="Diamantopoulou, Vasiliki, Konstantinos Angelopoulos, Michalis Pavlidis, and Haralambos Mouratidis. 2017. “A Metamodel for GDPR-Based Privacy Level Agreements.” In Proceedings of the ER Forum 2017 and the ER 2017 Demo Track Co-Located with the 36th International Conference on Conceptual Modelling (ER 2017), Valencia, Spain, - November 6-9, 2017., 285–91. http://ceur-ws.org/Vol-1979/paper-08.pdf.",
    contexts=[],
))

