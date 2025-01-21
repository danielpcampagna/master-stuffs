# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2017 import garijo2017a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, garijo2017a, ref="Garijo, Daniel. 2017. “WIDOCO: A Wizard for Documenting Ontologies.” In International Semantic Web Conference, 94–102. Springer. https://doi.org/10/gfxvtk.",
    contexts=[],
))

