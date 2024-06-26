from unicodedata import category
from snowballing.approaches import Group

from ..constants import *
from ...work.y2018 import teruel2018a

approach = Group(
    teruel2018a,
    display="SPECIAL",
    approach_name="SPECIAL",
    category='unrelated',
    useful=True,
    not_directly_related_to_provenance=True,
)
