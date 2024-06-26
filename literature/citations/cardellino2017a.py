# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2017 import cardellino2017a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, cardellino2017a, ref="Cardellino, Cristian, Milagro Teruel, Laura Alonso Alemany, and Serena Villata. 2017. “Legal NERC with Ontologies, Wikipedia and Curriculum Learning.” In 15th European Chapter of the Association for Computational Linguistics (EACL 2017), 254–59. Valencia, Spain. https://doi.org/10/gf6rvp.",
    contexts=[],
))

