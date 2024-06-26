# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2016 import pocs2016a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, pocs2016a, ref="“D3.1 Guidelines on Legal Aspects.” 2016. OPERANDO. http://www.operando.eu/upload/operando/moduli/D3.1-Guidelinesonlegalaspectsv2.0_77_289.pdf.",
    contexts=[],
))

