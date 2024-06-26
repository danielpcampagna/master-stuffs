# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2017 import raschke2017a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, raschke2017a, ref="Raschke, Philip, Olha Drozd, Bert Bos, Rudy Jacob, and Ben Whittamsmith. 2019. “D4.3 Transparency Dashboard and Control Panel Release V2.” Scalable Policy-awarE Linked Data arChitecture for prIvacy, trAnsparency and compLiance (SPECIAL).",
    contexts=[],
))

