# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1995 import directive1995a
from ..work.y2017 import fatema2017a
from ..work.y2018 import ujcich2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, directive1995a, ref="“Directive 95/46/EC of the European Parliament and of the Council on the Protection of Individuals with Regard to the Processing of Personal Data and on the Free Movement of Such Data.” 1995. Official Journal of the European Union L281 (November): 31–50. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:31995L0046.",
    contexts=[],
))



DB(Citation(
    fatema2017a, directive1995a, ref="[3] European Union Data Protection Directive, Directive 95/46/EC .",
    contexts=[],
))



DB(Citation(
    ujcich2018a, directive1995a, ref="10. Council of the European Union, “Directive 95/46/EC of the European Parliament and of the Council of 24 October 1995 (Data Protection Directive),” in Official Journal of the European Union, vol. L 281, Nov. 1995, pp. 31–50.",
    contexts=[],
))

