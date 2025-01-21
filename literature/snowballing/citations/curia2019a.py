# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2019 import curia2019a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, curia2019a, ref="“Opinion of Advocate General - Case C‑673/17.” 2019. March 21, 2019. http://curia.europa.eu/juris/document/document.jsf?docid=212023&mode=req&pageIndex=1&dir=&occ=first&part=1&text=&doclang=EN&cid=5704393.",
    contexts=[],
))

