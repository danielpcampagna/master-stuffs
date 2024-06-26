# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import fernández2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, fernández2018a, ref="Milošević, Uroš, Philip Raschke, Olha Drozd, Sabrina Kirrane, Freddy De Meersman, and Rudy Jacob. 2019. “D4.4 Usability Testing Report V2.” Scalable Policy-awarE Linked Data arChitecture for prIvacy, trAnsparency and compLiance (SPECIAL).",
    contexts=[],
))

