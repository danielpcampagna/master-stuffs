# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import pullonen2019a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, pullonen2019a, ref="Pullonen, Pille, Jake Tom, Raimundas Matulevičius, and Aivo Toots. 2019. “Privacy-Enhanced BPMN: Enabling Data Privacy Analysis in Business Processes Models.” Software & Systems Modeling, January. https://doi.org/10/gfv5x7.",
    contexts=[],
))

