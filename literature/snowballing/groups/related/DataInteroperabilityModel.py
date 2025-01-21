from snowballing.approaches import Group

from ..constants import *
from ...work.y2018 import pandit2018i
from ...work.y2018 import pandit2018j
from ...work.y2018 import pandit2018k
from ...work.y9999 import pandit9999b

approach = Group(
    pandit2018i, pandit2018j, pandit2018k, pandit9999b,
    display="GDPR Data Interoperability Model",
    approach_name="GDPR Data Interoperability Model",
    due="This paper models the data exchange between different entities related to the GDPR. It does not directly relate to the purposes of our work; hence, we have considered it out of our scope. However, it may provide some insights at the time of extending our model.",
    category="unrelated",
    useful=True,
    not_directly_related_to_provenance=True,
)
