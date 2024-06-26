# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import tambou2019a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, tambou2019a, ref="McCullagh, Karen, Olivia Tambou, and Sam Bourton. 2019. “National Adaptations of the GDPR.” Blog Droit Europeen. https://wp.me/p6OBGR-3dP.",
    contexts=[],
))

