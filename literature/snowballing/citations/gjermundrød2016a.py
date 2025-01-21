# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2016 import gjermundrød2016a
from ..work.y2018 import ujcich2018a
from ..work.y2020 import campagna2020a
from ..work.y2020 import pandit2020a


DB(Citation(
    ujcich2018a, gjermundrød2016a, ref="12. H. Gjermundrød, I. Dionysiou, and K. Costa, “privacyTracker: A privacy-by-design GDPR-compliant framework with verifiable data traceability controls,” in Proceedings of Current Trends in Web Engineering. Springer, 2016, pp. 3–15.",
    contexts=[],
))



DB(Citation(
    campagna2020a, gjermundrød2016a, ref="Gjermundrød, H., Dionysiou, I., and Costa, K. (2016). privacytracker: a privacy-bydesign gdpr-compliant framework with verifiable data traceability controls. In International Conference on Web Engineering, pages 3–15. Springer.",
    contexts=[],
))



DB(Citation(
    pandit2020a, gjermundrød2016a, ref="Gjermundrød, Harald, Ioanna Dionysiou, and Kyriakos Costa. 2016. “privacyTracker: A Privacy-by-Design GDPR-Compliant Framework with Verifiable Data Traceability Controls.” In Current Trends in Web Engineering, 3–15. Lecture Notes in Computer Science. Springer, Cham. https://doi.org/10/gfxvs2.",
    contexts=[],
))

