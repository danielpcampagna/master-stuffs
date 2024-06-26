# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import lioudakis2019a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, lioudakis2019a, ref="Lioudakis, Georgios, and Davide Cascone. 2019. “D3.1 Compliance Ontology.” BPR4GDPR.",
    contexts=[],
))

