from snowballing.approaches import Group

from ..constants import *
from ...work.y2019 import pandit2019c
from ...work.y9999 import pandit9999a
from ...work.y9999 import pandit9999b

approach = Group(
    pandit2019c, pandit9999a, pandit9999b,
    display="DPV",
    approach_name="Data Privacy Vocabulary",
    due="This approach have not directly relation to provenance. However, it can be useful when for efforts to extends current models due to provide a plethora of terms.",
    category="unrelated",
    useful=True,
    not_directly_related_to_provenance=True,
)
