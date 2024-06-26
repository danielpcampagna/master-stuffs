from unicodedata import category
from snowballing.approaches import Group

from ..constants import *
from ...work.y2018 import palmirani2018a
from ...work.y2018 import palmirani2018b
from ...work.y2018 import palmirani2018c

approach = Group(
    palmirani2018a, palmirani2018b, palmirani2018c,
    display="PrOnto",
    approach_name="PrOnto",
    category='unrelated',
    useful=True,
    not_directly_related_to_provenance=True,
)
