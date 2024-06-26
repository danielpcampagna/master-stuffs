# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import marini2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, marini2018a, ref="Marini, Alice, Alexis Kateifides, Joel Bates, Gabriela Zanfir-Fortuna, Michelle Bae, Stacey Gray, and Gargi Sen. 2018. “GDPR CCPA Comparison Guide.” DataGuidance and Future of Privacy Forum. https://fpf.org/wp-content/uploads/2018/11/GDPR_CCPA_Comparison-Guide.pdf.",
    contexts=[],
))

