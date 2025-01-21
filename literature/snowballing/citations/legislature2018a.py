# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import legislature2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, legislature2018a, ref="“Assembly Bill No. 375 Chapter 55: An Act to Add Title 1.81.5 (Commencing with Section 1798.100) to Part 4 of Division 3 of the Civil Code, Relating to Privacy.” 2018. California State Legislature, June. https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=201720180AB375.",
    contexts=[],
))

