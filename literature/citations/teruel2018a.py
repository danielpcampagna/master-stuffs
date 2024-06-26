# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import teruel2018a
from ..work.y2019 import stoykov2019a
from ..work.y2020 import pandit2020a
from ..work.y2019 import yeung2019a
from ..work.y2020 import gomes2020a
from ..work.y2020 import tang2020a
from ..work.y2020 import gomes2020b


DB(Citation(
    pandit2020a, teruel2018a, ref="Teruel, Milagro, Cristian Cardellino, Fernando Cardellino, Laura Alonso Alemany, and Serena Villata. 2018. “Legal Text Processing Within the MIREL Project.” In Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018).",
    contexts=[],
))

DB(Citation(
    yeung2019a, teruel2018a, ref="",
    contexts=[],
))



DB(Citation(
    gomes2020a, teruel2018a, ref="",
    contexts=[],
))



DB(Citation(
    tang2020a, teruel2018a, ref="",
    contexts=[],
))



DB(Citation(
    gomes2020b, teruel2018a, ref="",
    contexts=[],
))



DB(Citation(
    stoykov2019a, teruel2018a, ref="",
    contexts=[],
))

