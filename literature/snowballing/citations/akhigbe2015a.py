# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2015 import akhigbe2015a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, akhigbe2015a, ref="Akhigbe, Okhaide, Daniel Amyot, and Gregory Richards. 2015. “Information Technology Artifacts in the Regulatory Compliance of Business Processes: A Meta-Analysis.” In E-Technologies, edited by Morad Benyoucef, Michael Weiss, and Hafedh Mili, 209:89–104. Cham: Springer International Publishing. https://doi.org/10.1007/978-3-319-17957-5_6.",
    contexts=[],
))

