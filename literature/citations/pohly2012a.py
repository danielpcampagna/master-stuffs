# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2012 import pohly2012a
from ..work.y2020 import campagna2020a


DB(Citation(
    campagna2020a, pohly2012a, ref="Pohly, D. J., McLaughlin, S., McDaniel, P., and Butler, K. (2012). Hi-fi: collecting highfidelity whole-system provenance. In Proceedings of the 28th Annual Computer Security Applications Conference on, pages 259–268.",
    contexts=[],
))

