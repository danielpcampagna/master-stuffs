from unicodedata import category
from snowballing.approaches import Group

from ..constants import *
from ...work.y2018 import oltramari2018a

approach = Group(
    oltramari2018a,
    display="PrivOnto",
    approach_name="PrivOnto",
    category='unrelated',
)
