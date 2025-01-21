# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import lodge2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, lodge2018a, ref="Lodge, Tom, Andy Crabtree, and Anthony Brown. 2018. “Developing GDPR Compliant Apps for the Edge.” In Data Privacy Management, Cryptocurrencies and Blockchain Technology, edited by Joaquin Garcia-Alfaro, Jordi Herrera-Joancomartí, Giovanni Livraga, and Ruben Rios, 11025:313–28. Cham: Springer International Publishing. https://doi.org/10.1007/978-3-030-00305-0_22.",
    contexts=[],
))

