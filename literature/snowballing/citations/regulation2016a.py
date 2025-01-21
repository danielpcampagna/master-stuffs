# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2016 import regulation2016a
from ..work.y2017 import fatema2017a
from ..work.y2019 import besik2019a
from ..work.y2020 import campagna2020a
from ..work.y2020 import pandit2020a


DB(Citation(
    besik2019a, regulation2016a, ref="1. EU General Data Protection Regulation (GDPR). Regulation (EU) 2016/679 ofthe European Parliament and of the Council of 27 April 2016 on the protectionof natural persons with regard to the processing of personal data and on the freemovement of such data, and repealing Directive 95/46/EC (General Data Protec-tion Regulation), OJ 2016 L 119.",
    contexts=[],
))



DB(Citation(
    campagna2020a, regulation2016a, ref="Council of European Union (2016). Council regulation (EU) no 2016/679. https://eur-lex.europa.eu/eli/reg/2016/679/oj.",
    contexts=[],
))



DB(Citation(
    fatema2017a, regulation2016a, ref="[1] General Data Protection Regulations (GDPR), http://ec.europa.eu/justice/dataprotection/reform/files/regulation_oj_en.pdf",
    contexts=[],
))



DB(Citation(
    pandit2020a, regulation2016a, ref="“Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the Protection of Natural Persons with Regard to the Processing of Personal Data and on the Free Movement of Such Data, and Repealing Directive 95/46/EC (General Data Protection Regulation).” 2016. Official Journal of the European Union L119 (May). http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L:2016:119:TOC.",
    contexts=[],
))

