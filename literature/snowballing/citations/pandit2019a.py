# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import pandit2019a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, pandit2019a, ref="Pandit, Harshvardhan J., Christophe Debruyne, Declan O’Sullivan, and Dave Lewis. 2019. “GConsent - A Consent Ontology Based on the GDPR.” In The Semantic Web, edited by Pascal Hitzler, Miriam Fernández, Krzysztof Janowicz, Amrapali Zaveri, Alasdair J. G. Gray, Vanessa Lopez, Armin Haller, and Karl Hammar, 270–82. Lecture Notes in Computer Science. Springer International Publishing. https://w3id.org/GConsent.",
    contexts=[],
))

