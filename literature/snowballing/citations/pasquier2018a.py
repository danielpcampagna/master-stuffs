# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import pasquier2018a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, pasquier2018a, ref="Pasquier, Thomas, Jatinder Singh, Julia Powles, David Eyers, Margo Seltzer, and Jean Bacon. 2018. “Data Provenance to Audit Compliance with Privacy Policy in the Internet of Things.” Personal and Ubiquitous Computing 22 (2): 333–44. https://doi.org/10/gdcvmb.",
    contexts=[],
))

