# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2007 import guez2007a
from ..work.y2019 import besik2019a


DB(Citation(
    besik2019a, guez2007a, ref="6. Alfonso Rodr´ıguez, Eduardo Fern´andez-Medina, and Mario Piattini. A BPMNextension for the modeling of security requirements in business processes. IEICEtransactions on information and systems, 90(4):745–752, 2007.",
    contexts=[],
))

