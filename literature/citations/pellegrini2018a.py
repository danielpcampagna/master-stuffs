# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import pellegrini2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, pellegrini2018a, ref="Pellegrini, Tassilo, Andrea Schönhofer, Sabrina Kirrane, Anna Fensel, Oleksandra Panasiuk, Victor Mireles, Thomas Thurner, Axel Polleres, and Markus Dörfler. 2018. “A Genealogy and Classification of Rights Expression Languages-Preliminary Results.” In Data Protection/LegalTech-Proceedings of the 21st International Legal Informatics Symposium IRIS, 243–50.",
    contexts=[],
))

