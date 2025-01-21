# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import rantos2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, rantos2018a, ref="Rantos, Konstantinos, George Drosatos, Konstantinos Demertzis, Christos Ilioudis, Alexandros Papanikolaou, and Antonios Kritsas. 2019. “ADvoCATE: A Consent Management Platform for Personal Data Processing in the IoT Using Blockchain Technology.” In Innovative Security Solutions for Information Technology and Communications, edited by Jean-Louis Lanet and Cristian Toma, 300–313. Lecture Notes in Computer Science. Springer International Publishing.",
    contexts=[],
))

