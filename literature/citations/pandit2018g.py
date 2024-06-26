# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import pandit2018g
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, pandit2018g, ref="Pandit, Harshvardhan Jitendra, Declan O’Sullivan, and Dave Lewis. 2018a. “Extracting Provenance Metadata from Privacy Policies.” In Provenance and Annotation of Data and Processes, edited by Khalid Belhajjame, Ashish Gehani, and Pinar Alper, 262–65. Lecture Notes in Computer Science. Springer International Publishing. https://doi.org/10/gfxgwm.",
    contexts=[],
))

