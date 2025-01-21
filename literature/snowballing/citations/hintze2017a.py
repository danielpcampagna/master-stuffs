# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2017 import hintze2017a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, hintze2017a, ref="Hintze, Mike, and Gary LaFever. 2017. “Meeting Upcoming GDPR Requirements While Maximizing the Full Value of Data Analytics.” SSRN. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2927540.",
    contexts=[],
))

