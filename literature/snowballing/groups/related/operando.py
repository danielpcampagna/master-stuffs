from snowballing.approaches import Group

from ..constants import *
from ...work.y2016 import pocs2016a
from ...work.y2017 import echevarria2017a

approach = Group(
    pocs2016a, echevarria2017a,
    display="OPERANDO",
    approach_name="OPERANDO",
    category="unrelated",
)
