# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2012 import suárez2012a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, suárez2012a, ref="Suárez-Figueroa, Mari Carmen, Asunción Gómez-Pérez, and Mariano Fernández-López. 2012. “The NeOn Methodology for Ontology Engineering.” In Ontology Engineering in a Networked World, edited by Mari Carmen Suárez-Figueroa, Asunción Gómez-Pérez, Enrico Motta, and Aldo Gangemi, 9–34. Berlin, Heidelberg: Springer Berlin Heidelberg. https://doi.org/10.1007/978-3-642-24794-1_2.",
    contexts=[],
))

