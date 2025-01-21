# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2016 import christl2016a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, christl2016a, ref="Christl, Wolfie, and Sarah Spiekermann. 2016. Networks of Control: A Report on Corporate Surveillance, Digital Tracking, Big Data & Privacy. Wien: Facultas.",
    contexts=[],
))

