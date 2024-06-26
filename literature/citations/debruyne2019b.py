# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import debruyne2019b
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, debruyne2019b, ref="Debruyne, Christophe, Jonathan Riggio, Olga De Troyey, and Declan O’Sullivan. 2019. “An Ontology for Representing and Annotating Data Flows to Facilitate Compliance Verification.” In 2019 13th International Conference on Research Challenges in Information Science (RCIS), 1–6. https://doi.org/10/ggkj8n.",
    contexts=[],
))

