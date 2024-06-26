# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2020 import pandit2020a

from ..work.y9999 import restassured9999a


DB(Citation(
    pandit2020a, restassured9999a, ref="“RestAssured.” 2019. 2019. https://restassuredh2020.eu/.",
    contexts=[],
))

