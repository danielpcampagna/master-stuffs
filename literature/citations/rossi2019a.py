# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import rossi2019a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, rossi2019a, ref="Arianna, Rossi, and Palmirani Monica. 2019. “DaPIS: An Ontology-Based Data Protection Icon Set.” Frontiers in Artificial Intelligence and Applications, 181–95. https://doi.org/10/gf7fbn.",
    contexts=[],
))

