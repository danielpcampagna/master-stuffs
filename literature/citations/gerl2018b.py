# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import gerl2018b
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, gerl2018b, ref="Gerl, Armin, Nadia Bennani, Harald Kosch, and Lionel Brunie. 2018. “LPL, Towards a GDPR-Compliant Privacy Language: Formal Definition and Usage.” In Transactions on Large-Scale Data- and Knowledge-Centered Systems XXXVII, edited by Abdelkader Hameurlain and Roland Wagner, 41–80. Lecture Notes in Computer Science. Berlin, Heidelberg: Springer Berlin Heidelberg. https://doi.org/10.1007/978-3-662-57932-9_2.",
    contexts=[],
))

