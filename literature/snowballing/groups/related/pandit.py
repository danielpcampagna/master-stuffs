from snowballing.approaches import Group

from ..constants import *
from ...work.y2018 import pandit2018a
from ...work.y2018 import pandit2018b
from ...work.y2018 import pandit2018c
from ...work.y2018 import pandit2018d
from ...work.y2018 import pandit2018e
from ...work.y2018 import pandit2018f
from ...work.y2018 import pandit2018g
from ...work.y2019 import pandit2019a

approach = Group(
    pandit2018a, pandit2018b, pandit2019a, pandit2018c, pandit2018d, pandit2018e, pandit2018f, pandit2018g,
    display="Pandit approach",
    approach_name="Pandit approach",
)
