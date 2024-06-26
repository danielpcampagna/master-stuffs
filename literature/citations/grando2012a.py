# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2012 import grando2012a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, grando2012a, ref="Grando, Maria Adela, Aziz Boxwala, Richard Schwab, and Neda Alipanah. 2012. “Ontological Approach for the Management of Informed Consent Permissions.” In 2nd International Conference on Healthcare Informatics, Imaging and Systems Biology, 51–60. IEEE. https://doi.org/10/gfxvsr.",
    contexts=[],
))

