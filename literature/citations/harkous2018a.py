# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import harkous2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, harkous2018a, ref="Harkous, Hamza, Kassem Fawaz, Rémi Lebret, Florian Schaub, Kang G Shin, and Karl Aberer. 2018. “Polisis: Automated Analysis and Presentation of Privacy Policies Using Deep Learning.” In 27th USENIX Security Symposium (USENIX Security 18), 531–48.",
    contexts=[],
))

