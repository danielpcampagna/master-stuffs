# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import hoppe2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, hoppe2018a, ref="Wenning, Rigo, and Sabrina Kirrane. 2018. “Compliance Using Metadata.” In Semantic Applications: Methodology, Technology, Corporate Use, edited by Thomas Hoppe, Bernhard Humm, and Anatol Reibold, 31–45. Berlin, Heidelberg: Springer Berlin Heidelberg. https://doi.org/10.1007/978-3-662-55433-3_3.",
    contexts=[],
))

