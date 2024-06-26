from unicodedata import category
from snowballing.approaches import Group

from ..constants import *
from ...work.y2018 import kirrane2018a
from ...work.y2018 import bonatti2018a
from ...work.y2018 import bonatti2018b
from ...work.y2018 import bonatti2018d
from ...work.y2018 import teruel2018a

approach = Group(
    kirrane2018a, bonatti2018a, bonatti2018b, bonatti2018d, teruel2018a,
    display="SPECIAL",
    approach_name="SPECIAL",
    # due="The SPECIAL is a technical solution addressed to meet the Big Data requirements with the privacy-aware data protection concerns. The SPECIAL's umbrella was built over different research areas of interest and proposed various resources to cover conflicts that arise when we face both Big Data and privacy concerns. One of these research areas scopes ontology. The project proposes inter alias and the Usage Policy ontologiy to express the data subjects' consent and the data usage policies of data controllers in formal terms.",
    category='ok',
    useful=True,
    not_directly_related_to_provenance=True,
)
