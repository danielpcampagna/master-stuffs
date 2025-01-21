# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2017 import teodoro2017a
from ..work.y2020 import pandit2020a


DB(Citation(
    pandit2020a, teodoro2017a, ref="“D1.1 Initial List of Main Requirements.” 2017. My Health My Data (MHMD). http://www.myhealthmydata.eu/wp-content/themes/Parallax-One/deliverables/D1.1_Initial-List-of-Main-Requirements.pdf.",
    contexts=[],
))

