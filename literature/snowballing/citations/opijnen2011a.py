# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2011 import opijnen2011a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, opijnen2011a, ref="Opijnen, Marc van. 2011. “European Case Law Identifier: Indispensable Asset for Legal Information Retrieval.” From Information to Knowledge – Online Access to Legal Information: Methodologies, Trends and Perspectives, December, 12.",
    contexts=[],
))

