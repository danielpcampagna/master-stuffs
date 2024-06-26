# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import mehr2019a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, mehr2019a, ref="Mehr, Azadeh Sadat Mozafari. 2019. “Compliance to Data Protection and Purpose Control Using Process Mining Technique.” In Proceedings of the Dissertation Award, Doctoral Consortium, and Demonstration Track at BPM 2019 Co-Located with 17th International Conference on Business Process Management (BPM 2019), 6. Vienna, Austria.",
    contexts=[],
))

