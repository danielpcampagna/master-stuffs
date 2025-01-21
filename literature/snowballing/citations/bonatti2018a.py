# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import bonatti2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, bonatti2018a, ref="Bonatti, Piero A, Sabrina Kirrane, Illiana M. Petrova, Luigi Sauro, and Eva Schlehahn. 2018a. “The SPECIAL Usage Policy Language V0.1.” http://purl.org/specialprivacy/policylanguage.",
    contexts=[],
))

