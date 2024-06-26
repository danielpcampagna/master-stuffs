# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import bonatti2018d
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, bonatti2018d, ref="Bonatti, Piero A, Wouter Dullaert, Javier D Fernandez, Sabrina Kirrane, Uros Milosevic, and Axel Polleres. 2018. “The SPECIAL Policy Log Vocabulary V0.5.” https://aic.ai.wu.ac.at/qadlod/policyLog/.",
    contexts=[],
))

