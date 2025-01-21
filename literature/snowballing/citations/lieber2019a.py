# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import lieber2019a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, lieber2019a, ref="Lieber, Sven. 2019. “Policy-Compliant Data Processing: RDF-Based Restrictions for Data-Protection.” In Doctoral Track - 18th International Semantic Web Conference (ISWC), 12. Auckland, New Zealand.",
    contexts=[],
))

