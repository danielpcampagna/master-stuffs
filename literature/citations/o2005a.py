# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2005 import o2005a
from ..work.y2017 import fatema2017a


DB(Citation(
    fatema2017a, o2005a, ref="[9] O'Keefe, C. M., Greenfield, P., and Goodchild, A.: A decentralised approach to electronic consent and health information access control. Journal of Research and Practice in Information Technology 37 (2), 161-178 (2005).",
    contexts=[],
))

