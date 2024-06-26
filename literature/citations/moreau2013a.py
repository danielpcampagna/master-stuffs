# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2013 import moreau2013a
from ..work.y2018 import ujcich2018a


DB(Citation(
    ujcich2018a, moreau2013a, ref="9. World Wide Web Consortium, “PROV-DM: The PROV data model,” https://www.w3.org/TR/prov-dm/, Apr. 2013.",
    contexts=[],
))

