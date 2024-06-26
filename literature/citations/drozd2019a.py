# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import drozd2019a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, drozd2019a, ref="Drozd, Olha, and Sabrina Kirrane. 2019a. “Consent Comprehension Made Easy Demo.” In 19th Privacy Enhancing Technologies Symposium (PETS), 1.",
    contexts=[],
))

