# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import geko2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, geko2018a, ref="Geko, Melisa, and Simon Tjoa. 2018. “An Ontology Capturing the Interdependence of the General Data Protection Regulation (GDPR) and Information Security.” In Proceedings of the Central European Cybersecurity Conference 2018 on - CECC 2018, 1–6. Ljubljana, Slovenia: ACM Press. https://doi.org/10/gfxqw4.",
    contexts=[],
))

