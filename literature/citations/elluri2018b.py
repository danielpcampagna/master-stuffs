# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import elluri2018b
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, elluri2018b, ref="Elluri, Lavanya, and Karuna Pande Joshi. 2018. “A Knowledge Representation of Cloud Data Controls for EU GDPR Compliance.” In 2018 IEEE World Congress on Services, SERVICES 2018, San Francisco, CA, USA, July 2-7, 2018, 45–46. https://doi.org/10/gft38j.",
    contexts=[],
))

