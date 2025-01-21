# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2020 import pandit2020a

from ..work.y2020 import cox2020a


DB(Citation(
    pandit2020a, cox2020a, ref="Cox, S, and C Little. 2017. “Time Ontology in OWL.” World Wide Web Consortium. Retrieved from Https://Www. W3. Org/TR/Owl-Time.",
    contexts=[],
))

