# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2016 import fatema2016a
from ..work.y2017 import fatema2017a


DB(Citation(
    fatema2017a, fatema2016a, ref="[15] Fatema, K., Debruyne, C., Lewis, D., OSullivan, D., Morrison, J. P. and Mazed, A. A.: A Semi-Automated Methodology for Extracting Access Control Rules from the European Data Protection Directive. In. 2016 IEEE Security and Privacy Workshops (SPW), pp.",
    contexts=[],
))

