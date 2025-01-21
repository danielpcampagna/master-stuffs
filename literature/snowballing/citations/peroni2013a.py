# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2013 import peroni2013a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, peroni2013a, ref="Peroni, Silvio, David Shotton, and Fabio Vitali. 2013. “Tools for the Automatic Generation of Ontology Documentation: A Task-Based Evaluation.” International Journal on Semantic Web and Information Systems (IJSWIS) 9 (1): 21–44. https://doi.org/10/f47ncz.",
    contexts=[],
))

