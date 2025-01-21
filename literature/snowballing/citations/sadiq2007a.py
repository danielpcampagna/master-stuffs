# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2007 import sadiq2007a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, sadiq2007a, ref="Sadiq, Shazia, Guido Governatori, and Kioumars Namiri. 2007. “Modeling Control Objectives for Business Process Compliance.” In Business Process Management, edited by Gustavo Alonso, Peter Dadam, and Michael Rosemann, 149–64. Lecture Notes in Computer Science. Springer Berlin Heidelberg.",
    contexts=[],
))

