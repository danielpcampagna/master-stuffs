# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import palmirani2018d
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, palmirani2018d, ref="Monica, Palmirani, and Governatori Guido. 2018. “Modelling Legal Knowledge for GDPR Compliance Checking.” Frontiers in Artificial Intelligence and Applications, 101–10. https://doi.org/10/gfr9qc.",
    contexts=[],
))

