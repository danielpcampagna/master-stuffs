# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2017 import silva2017a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, silva2017a, ref="“D4.3 Risk Management Module & Personal Data Analyser - Interim Implementation.” 2019. POSEIDON. https://www.poseidon-h2020.eu/wp-content/uploads/2019/08/D4.3-RMM-and-PDA-V1.0-Final.pdf.",
    contexts=[],
))

