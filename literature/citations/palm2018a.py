# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import palm2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, palm2018a, ref="Palm, Alexander. 2018. “Modelling Data Protection Vulnerabilities of Cloud Systems Using Risk Patterns.” Technical Report. RestAssured.",
    contexts=[],
))

