# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2017 import knublauch2017a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, knublauch2017a, ref="Knublauch, Holger, and Dimitris Kontokostas. 2017. “Shapes Constraint Language (SHACL).” July 2017. https://www.w3.org/TR/shacl/.",
    contexts=[],
))

