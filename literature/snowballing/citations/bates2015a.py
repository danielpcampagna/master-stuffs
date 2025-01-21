# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2015 import bates2015a
from ..work.y2018 import ujcich2018a
from ..work.y2020 import campagna2020a


DB(Citation(
    ujcich2018a, bates2015a, ref="15. A. Bates, D. Tian, K. R. B. Butler, and T. Moyer, “Trustworthy whole-system provenance for the Linux kernel,” in Proceedings of USENIX Security ’15, 2015, pp. 319–334.",
    contexts=[],
))



DB(Citation(
    campagna2020a, bates2015a, ref="Bates, A., Tian, D. J., Butler, K. R., and Moyer, T. (2015). Trustworthy whole-system provenance for the linux kernel. In 24th {USENIX} Security Symposium ({USENIX} Security 15), pages 319–334.",
    contexts=[],
))

