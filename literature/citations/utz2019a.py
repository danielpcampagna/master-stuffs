# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import utz2019a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, utz2019a, ref="Utz, Christine, Martin Degeling, Sascha Fahl, Florian Schaub, and Thorsten Holz. 2019. “(Un)Informed Consent: Studying GDPR Consent Notices in the Field.” In ACM SIGSAC Conference on Computer and Communications Security (CCS’19), 18. London, United Kingdom.",
    contexts=[],
))

