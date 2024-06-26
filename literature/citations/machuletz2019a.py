# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import machuletz2019a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, machuletz2019a, ref="Machuletz, Dominique, and Rainer Böhme. 2019. “Multiple Purposes, Multiple Problems: A User Study of Consent Dialogs After GDPR,” August. http://arxiv.org/abs/1908.10048.",
    contexts=[],
))

