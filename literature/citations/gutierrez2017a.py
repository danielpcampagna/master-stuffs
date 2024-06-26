# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2017 import gutierrez2017a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, gutierrez2017a, ref="“D3.1 PoSeID-on Blockchain - Interim Implementation.” 2019. POSEIDON. https://www.poseidon-h2020.eu/wp-content/uploads/2019/08/D3.1_final-version_POSEIDON_v10.pdf.",
    contexts=[],
))

