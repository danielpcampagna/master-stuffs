# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2013 import bier2013a
from ..work.y2018 import ujcich2018a
from ..work.y2020 import campagna2020a


DB(Citation(
    ujcich2018a, bier2013a, ref="14. C. Bier, “How usage control and provenance tracking get together - A data protection perspective,” in Proceedings of IEEE 4th International Workshop on Data Usage Management, May 2013, pp. 13–17.",
    contexts=[],
))



DB(Citation(
    campagna2020a, bier2013a, ref="Bier, C. (2013). How usage control and provenance tracking get together-a data protection perspective. In 2013 IEEE Security and Privacy Workshops, pages 13–17. IEEE.",
    contexts=[],
))

