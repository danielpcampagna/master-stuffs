# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import linden2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, linden2018a, ref="Linden, Thomas, Rishabh Khandelwal, Hamza Harkous, and Kassem Fawaz. 2018. “The Privacy Policy Landscape After the GDPR,” September. http://arxiv.org/abs/1809.08396.",
    contexts=[],
))

