from snowballing.approaches import Group

from ..constants import *
from ...work.y2017 import nicoletti2017a
from ...work.y2017 import gutierrez2017a
from ...work.y2017 import silva2017a

approach = Group(
    nicoletti2017a, gutierrez2017a, silva2017a,
    display="PoSeID-on",
    approach_name="PoSeID-on",
    category="unrelated",
)
