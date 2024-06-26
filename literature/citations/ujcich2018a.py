# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2018 import ujcich2018a
from ..work.y2018 import ujcich2018b
from ..work.y2018 import singh2018a
from ..work.y2019 import zhao2019a
from ..work.y2019 import riva2019a
from ..work.y2019 import ujcich2019a
from ..work.y2020 import campagna2020a
from ..work.y2020 import pandit2020a
from ..work.y2020 import riva2020a
from ..work.y2020 import ujcich2020a
from ..work.y2021 import norval2021a

DB(Citation(
    ujcich2018b, ujcich2018a, ref="",
    contexts=[],
))



DB(Citation(
    zhao2019a, ujcich2018a, ref="",
    contexts=[],
))



DB(Citation(
    riva2019a, ujcich2018a, ref="",
    contexts=[],
))




DB(Citation(
    ujcich2019a, ujcich2018a, ref="",
    contexts=[],
))



DB(Citation(
    campagna2020a, ujcich2018a, ref="",
    contexts=[],
))


DB(Citation(
    pandit2020a, ujcich2018a, ref="[50] B. E. Ujcich, A. Bates, and W. H. Sanders, “A Provenance Model for the European Union General Data Protection Regulation”, in Provenance and Annotation of Data and Processes, K. Belhajjame, A. Gehani, and P. Alper, Eds., vol. 11017, Cham: Springer International Publishing, 2018, pp. 45–57, ISBN: 978-3-319-98378-3 978-3-319-98379-0. DOI: 10.1007/978-3-319-98379-0_4. [Online]. Available: http://link.springer.com/ 10.1007/978-3-319-98379-0_4 (visited on 09/10/2018).",
    contexts=['Ujcich et al [50] present a data provenance model of GDPR utilising PROV-O [47] to represent activities and data as semantic-web representations. The data model from the publication is depicted in Figure 3.10 and provides an overview of concepts using PROV-O [47] diagrams to denote concepts. The approach uses the activity ‘Justify’ to represent rationale for processing personal data and has annotations depicting its starting and ending times, as well as a ‘Justification’ - which represents legal basis of processing. The ontology focuses on workflows involving exercising of rights under GDPR, and provides examples of provenance for data rectification and withdrawal of consent.\n\nThe approach presented in the publication uses design patterns to describe use of ontology in specific cases regarding exercising of rights. The design pattern for provenance associated with consent does not associate data directly with consent owing to data being potentially updated independent of consent. The design pattern is further extended in the publication to represent data sharing with a processor for marketing. The publication provides a discussion on verification of compliance based on provenance through questions which can be queried over the data represented using presented ontology.\n\nSpecifying purposes as defined by GDPR is not clarified in this approach as the concept of Justify is temporal in its use and limited to processing of personal data it is associated with. The approach also does not provide any information on modelling of more complex processing operations where more than one legal basis could be applied, or where processing operations need to be expressed in several steps. The approach also does not model information about consent or rights, and does not provide ex-ante representations of activities.'],
))



DB(Citation(
    riva2020a, ujcich2018a, ref="",
    contexts=[],
))



DB(Citation(
    norval2021a, ujcich2018a, ref="",
    contexts=[],
))



DB(Citation(
    ujcich2020a, ujcich2018a, ref="",
    contexts=[],
))


DB(Citation(
    singh2018a, ujcich2018a, ref="[49] B. E. Ujcich, A. Bates, and W. H. Sanders, ‘‘A provenance model for the European union general data protection regulation,’’ in Proc. Int. Provenance Annotation Workshop, 2018, pp. 45–57.",
    contexts=['Singh et al. cite Ujcich et al. as a manner to make provenance data meaningful.'],
))

