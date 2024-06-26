# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import pandit2018e
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, pandit2018e, ref="Pandit, Harshvardhan J., Kaniz Fatema, Declan O’Sullivan, and Dave Lewis. 2018. “GDPRtEXT - GDPR as a Linked Data Resource.” In The Semantic Web - European Semantic Web Conference, 481–95. Lecture Notes in Computer Science. Springer, Cham. https://doi.org/10/c3n4.",
    contexts=[],
))

