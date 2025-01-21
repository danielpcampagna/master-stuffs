# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import leone2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, leone2018a, ref="Leone, Valentina, Luigi Di Caro, and Serena Villata. 2018. “Legal Ontologies and How to Choose Them: The InvestigatiOnt Tool.” In Proceedings of the ISWC 2018 Posters & Demonstrations, Industry and Blue Sky Ideas Tracks Co-Located with 17th International Semantic Web Conference (ISWC 2018), Monterey, USA, October 8th - to - 12th, 2018. http://ceur-ws.org/Vol-2180/paper-36.pdf.",
    contexts=[],
))

