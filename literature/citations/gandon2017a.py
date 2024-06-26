# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2017 import gandon2017a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, gandon2017a, ref="Gandon, Fabien, Guido Governatori, and Serena Villata. 2017. “Normative Requirements as Linked Data.” In 30th International Conference on Legal Knowledge and Information Systems (JURIX), 11. Luxembourg.",
    contexts=[],
))

