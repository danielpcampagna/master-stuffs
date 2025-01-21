# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2017 import echevarria2017a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, echevarria2017a, ref="“D6.7 Final (Product) Version of Security Aware Tools.” 2017. OPERANDO. http://www.operando.eu/upload/operando/moduli/D6.7FinalProductVersionofSecurityAwareToolsv1.0_77_378.pdf.",
    contexts=[],
))

