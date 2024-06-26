# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import libertés2019a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, libertés2019a, ref="“The CNIL’s Restricted Committee Imposes a Financial Penalty of 50 Million Euros Against GOOGLE LLC | CNIL.” 2019. January 21, 2019. https://www.cnil.fr/en/cnils-restricted-committee-imposes-financial-penalty-50-million-euros-against-google-llc.",
    contexts=[],
))

