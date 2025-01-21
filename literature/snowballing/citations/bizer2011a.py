# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2011 import bizer2011a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, bizer2011a, ref="Bizer, Christian, Tom Heath, and Tim Berners-Lee. 2011. “Linked Data: The Story so Far.” Semantic Services, Interoperability and Web Applications: Emerging Concepts, 205–27. https://doi.org/10/dh8v52.",
    contexts=[],
))

