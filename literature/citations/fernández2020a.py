# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2020 import pandit2020a

from ..work.y2020 import fernández2020a


DB(Citation(
    pandit2020a, fernández2020a, ref="Fernandez, Javier D, Marta Sabou, Elmar Kiesling, Fajar J Ekaputra, Amr Azzam, and Rigo Wenning. 2019. “User Consent Modeling for Ensuring Transparency and Compliance in Smart Cities.” Personal and Ubiquitous Computing Journal, 34.",
    contexts=[],
))

