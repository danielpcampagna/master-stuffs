# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import bayle2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, bayle2018a, ref="Bayle, Aurelie, Mirko Koscina, David Manset, and Octavio Perez-Kempner. 2018. “When Blockchain Meets the Right to Be Forgotten: Technology Versus Law in the Healthcare Industry.” In 2018 IEEE/WIC/ACM International Conference on Web Intelligence (WI), 788–92. Santiago: IEEE. https://doi.org/10/gf9jn7.",
    contexts=[],
))

