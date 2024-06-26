# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2015 import pasquier2015a
from ..work.y2018 import ujcich2018a
from ..work.y2020 import campagna2020a


DB(Citation(
    ujcich2018a, pasquier2015a, ref="16. T. Pasquier, J. Singh, D. Eyers, and J. Bacon, “CamFlow: Managed data-sharing for cloud services,” IEEE Transactions on Cloud Computing, vol. 5, no. 3, pp. 472–484, July 2017.",
    contexts=[],
))



DB(Citation(
    campagna2020a, pasquier2015a, ref="Pasquier, T. F.-M., Singh, J., Eyers, D., and Bacon, J. (2015). Camflow: Managed datasharing for cloud services. IEEE Transactions on Cloud Computing, 5(3):472–484.",
    contexts=[],
))

