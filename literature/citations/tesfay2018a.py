# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import tesfay2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, tesfay2018a, ref="Tesfay, Welderufael B., Peter Hofmann, Toru Nakamura, Shinsaku Kiyomoto, and Jetzabel Serna. 2018. “PrivacyGuide: Towards an Implementation of the EU GDPR on Internet Privacy Policy Evaluation.” In Proceedings of the Fourth ACM International Workshop on Security and Privacy Analytics, 15–21. IWSPA ’18. New York, NY, USA: ACM. https://doi.org/10/gfxvsx.",
    contexts=[],
))

