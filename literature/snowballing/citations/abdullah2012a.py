# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2012 import abdullah2012a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, abdullah2012a, ref="Syed Abdullah, Norris, Shazia Sadiq, and Marta Indulska. 2012. “A Compliance Management Ontology: Developing Shared Understanding Through Models.” In Advanced Information Systems Engineering, edited by Jolita Ralyté, Xavier Franch, Sjaak Brinkkemper, and Stanislaw Wrycza, 429–44. Lecture Notes in Computer Science. Springer Berlin Heidelberg.",
    contexts=[],
))

