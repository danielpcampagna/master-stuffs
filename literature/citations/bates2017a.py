# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2017 import bates2017a
from ..work.y2018 import ujcich2018a


DB(Citation(
    ujcich2018a, bates2017a, ref="17. A. Bates, W. U. Hassan, K. Butler, A. Dobra, B. Reaves, P. Cable, T. Moyer, and N. Schear, “Transparent web service auditing via network provenance functions,” in Proceedings of the 26th International Conference on World Wide Web, 2017, pp. 887–8",
    contexts=[],
))

