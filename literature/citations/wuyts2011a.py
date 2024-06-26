# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2011 import wuyts2011a
from ..work.y2017 import fatema2017a


DB(Citation(
    fatema2017a, wuyts2011a, ref="[8] Wuyts, K., Scandariato, R., Verhenneman, G., Joosen, W.: Integrating patient consent in e-health access control. In. Developing and Evaluating Security-Aware Software Systems, IGI Global, pp. 285-308. (2013).",
    contexts=[],
))

