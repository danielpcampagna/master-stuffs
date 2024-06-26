from snowballing.approaches import Group

from ..constants import *
from ...work.y2019 import lioudakis2019a

approach = Group(
    lioudakis2019a,
    display="BPR4GDPR",
    category="unrelated",
    useful=True,
    not_directly_related_to_provenance=True,
)
