# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import gallé2019a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, gallé2019a, ref="Galle, Matthias, Athena Christofi, and Hady Elsahar. 2019. “The Case for a GDPR-Specific Annotated Dataset of Privacy Policies.” In Proceedings of the PAL: Privacy-Enhancing Artificial Intelligence and Language Technologies as Part of the AAAI Spring Symposium Series (AAAI-SSS 2019), 3. http://ceur-ws.org/Vol-2335/1st_PAL_paper_5.pdf.",
    contexts=[],
))

