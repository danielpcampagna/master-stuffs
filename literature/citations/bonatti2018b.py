# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import bonatti2018b
from ..work.y2019 import pandit2019c
from ..work.y2020 import pandit2020a
from ..work.y2020 import bonatti2020b
from ..work.y2021 import grünewald2021a
from ..work.y2021 import mokhtari2021a


DB(Citation(
    pandit2020a, bonatti2018b, ref="Bonatti, Piero A, Bert Bos, Stefan Decker, Javier D Fernandez, Vassilios Peristeras, Axel Polleres, and Rigo Wenning. 2018. “Data Privacy Vocabularies and Controls: Semantic Web for Transparency and Privacy.” In Proceedings of the Workshop on Semantic Web for Social Good Co-Located with 17th International Semantic Web Conference (ISWC 2018), 4. Monterey, California, USA. http://ceur-ws.org/Vol-2182/paper_3.pdf.",
    contexts=[],
))


DB(Citation(
    pandit2019c, bonatti2018b,
    contexts=[],
))



DB(Citation(
    bonatti2020b, bonatti2018b, ref="",
    contexts=[],
))



DB(Citation(
    grünewald2021a, bonatti2018b, ref="",
    contexts=[],
))



DB(Citation(
    mokhtari2021a, bonatti2018b, ref="",
    contexts=[],
))

