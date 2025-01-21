# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import pandit2018f
from ..work.y2018 import debattista2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, pandit2018f, ref="Pandit, Harshvardhan J, Declan O’Sullivan, and Dave Lewis. 2018. “GDPR-Driven Change Detection in Consent and Activity Metadata.” In Joint Proceedings of the 4th Workshop on Managing the Evolution and Preservation of the Data Web (MEPDaW), the 2nd Workshop on Semantic Web Solutions for Large-Scale Biomedical Data Analytics (SeWeBMeDA), and the Workshop on Semantic Web of Things for Industry 4.0 (SWeTI) Co-Located with 15th European Semantic Web Conference (ESWC 2018), 5. Heraklion, Crete, Greece. http://ceur-ws.org/Vol-2112/mepdaw_paper_2.pdf.",
    contexts=[],
))



DB(Citation(
    debattista2018a, pandit2018f, ref="",
    contexts=[],
))

