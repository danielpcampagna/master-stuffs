# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2017 import schoenen2017a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, schoenen2017a, ref="Schoenen, Stefan, Zoltán Ádám Mann, and Andreas Metzger. 2018. “Using Risk Patterns to Identify Violations of Data Protection Policies in Cloud Systems.” In Service-Oriented Computing – ICSOC 2017 Workshops, edited by Lars Braubach, Juan M. Murillo, Nima Kaviani, Manuel Lama, Loli Burgueño, Naouel Moha, and Marc Oriol, 10797:296–307. Cham: Springer International Publishing. https://doi.org/10.1007/978-3-319-91764-1_24.",
    contexts=[],
))

