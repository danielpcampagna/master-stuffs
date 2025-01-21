# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import winckler2019a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, winckler2019a, ref="Winckler, Marco, Laurent Goncalves, Olivier Nicolas, Frédérique Biennier, Hind Benfenatki, Thierry Despeyroux, Nourhène Alaya, et al. 2019. “Personal Information Controller Service (PICS).” In Web Engineering, edited by Maxim Bakaev, Flavius Frasincar, and In-Young Ko, 530–33. Lecture Notes in Computer Science. Springer International Publishing.",
    contexts=[],
))

