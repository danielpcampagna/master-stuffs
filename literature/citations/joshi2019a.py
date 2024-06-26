# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import joshi2019a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, joshi2019a, ref="Joshi, Karuna Pande, and Agniva Banerjee. 2019. “Automating Privacy Compliance Using Policy Integrated Blockchain.” Cryptography 3 (1): 7. https://doi.org/10/gf6rvc.",
    contexts=[],
))

