# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import benfenatki2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, benfenatki2018a, ref="Benfenatki, Hind, Frédérique Biennier, Marco Winckler, Laurent Goncalves, Olivier Nicolas, and Zohra Saoud. 2018. “Towards a User Centric Personal Data Protection Framework.” In ACM CHI Conference on Human Factors in Computing Systems - GDPR Workshop, 6.",
    contexts=[],
))

