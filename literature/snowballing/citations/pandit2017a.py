# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2017 import pandit2017a
from ..work.y2018 import ujcich2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, pandit2017a, ref="Pandit, Harshvardhan J., and Dave Lewis. 2017. “Modelling Provenance for GDPR Compliance Using Linked Open Data Vocabularies.” In Proceedings of the 5th Workshop on Society, Privacy and the Semantic Web - Policy and Technology (PrivOn2017) (PrivOn). http://ceur-ws.org/Vol-1951/PrivOn2017_paper_6.pdf.",
    contexts=[],
))



DB(Citation(
    ujcich2018a, pandit2017a, ref="8. H. J. Pandit and D. Lewis, “Modelling provenance for GDPR compliance using linked open data vocabularies,” in Proceedings of Society, Privacy and the Semantic Web - Policy and Technology ’17, 2017.",
    contexts=[],
))

