# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2013 import sadeh2013a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, sadeh2013a, ref="Sadeh, Norman, Alessandro Acquisti, Travis D. Breaux, Lorrie Faith Cranor, Aleecia M. McDonald, Joel R. Reidenberg, Noah A. Smith, et al. 2013. “The Usable Privacy Policy Project.” Technical Report, CMU-ISR-13-119, Carnegie Mellon University. http://ra.adm.cs.cmu.edu/anon/usr0/ftp/home/anon/isr2013/CMU-ISR-13-119.pdf.",
    contexts=[],
))

