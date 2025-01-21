# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import agarwal2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, agarwal2018a, ref="Agarwal, Sushant, Simon Steyskal, Franjo Antunovic, and Sabrina Kirrane. 2018. “Legislative Compliance Assessment: Framework, Model and GDPR Instantiation.” In Privacy Technologies and Policy, edited by Manel Medina, Andreas Mitrakas, Kai Rannenberg, Erich Schweighofer, and Nikolaos Tsouroulas, 131–49. Lecture Notes in Computer Science. Springer International Publishing.",
    contexts=[],
))

