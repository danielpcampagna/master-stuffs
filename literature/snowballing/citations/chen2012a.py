# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2012 import chen2012a
from ..work.y2017 import fatema2017a


DB(Citation(
    fatema2017a, chen2012a, ref="[4] Chen, D., Zhao, H.: Data Security and Privacy Protection Issues in Cloud Computing. In: 2012 International Conference on Computer Science and Electronics Engineering (ICCSEE), vol.1, pp. 647-651. Hangzhou, China (23-25 March 2012).",
    contexts=[],
))

