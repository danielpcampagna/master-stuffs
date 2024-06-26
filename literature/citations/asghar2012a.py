# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2012 import asghar2012a
from ..work.y2017 import fatema2017a


DB(Citation(
    fatema2017a, asghar2012a, ref="[13] Asghar, M. R., and Russello, G.: Actors: A goal-driven approach for capturing and managing consent in e-health systems. In. Policies for Distributed Systems and Networks",
    contexts=[],
))

