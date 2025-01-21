# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2020 import pandit2020a

from ..work.y2021 import pereira2021a


DB(Citation(
    pandit2020a, pereira2021a, ref="Fernández, Javier D, Fajar J Ekaputra, Peb Ruswono, Elmar Kiesling, and Amr Azzam. 2019. “Privacy-Aware Linked Widgets.” In 1st Workshop on Fairness, Accountability, Transparency, Ethics, and Society on the Web. In Conjunction with the Web Conference 2019, 8. https://doi.org/10/gf2599.",
    contexts=[],
))

