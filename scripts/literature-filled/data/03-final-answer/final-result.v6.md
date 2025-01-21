## Related Work

In our quest to extend GDPRov to answer previously uncovered compliance questions, we employed the Snowballing methodology. This iterative process starts with a set of primary studies, then identifies further relevant studies through their citations and references. This approach ensures a comprehensive coverage of the literature. By the end of our snowballing process, we examined a total of 178 documents, with 15 key studies summarized in the markdown content section.

The study by Ryan et al. [[Ryan_Pandit_Brennan]] proposes a novel semantic metadata-based approach for describing and integrating diverse data processing activities, addressing GDPR compliance requirements, particularly for creating a Register of Processing Activities (ROPA). Their approach utilizes the DCAT-AP standard extended by the Data Privacy Vocabulary (DPV) to specify retention periods, thus contributing to answering compliance question Q8. However, this approach does not fully address the comprehensive listing of all data transfers or the legal basis for such transfers.

Another significant work by Campagna et al. [[Campagna_da_Silva_Braganholo]] builds upon existing GDPR data provenance models to achieve compliance, focusing on transparency and the involvement of individuals in data treatment processes. Their model includes temporal relations to specify data retention periods, directly contributing to compliance question Q8. However, it lacks comprehensive components to ensure data accuracy and real-time updates, which are crucial for question Q28.

Ujcich et al. [[Ujcich_Bates_Sanders]] propose a data provenance model tailored to GDPR, capturing the history and lifecycle of data, including its origins, transformations, and usage. This model addresses several compliance questions, including Q8, by tracking data collection and processing timestamps. It also partially answers Q28 and Q29 by documenting data corrections and retention periods, though it doesn't fully automate these processes.

Pandit et al. [[Pandit_OSullivan_Lewis_GDPR]] focus on detecting and representing changes in consent and activities for GDPR compliance. Their approach uses P-Plan and ODRL to track the provenance of activities and consent changes, contributing to Q28 by ensuring data corrections are linked to original activities. However, they do not provide detailed mechanisms for enforcing retention policies (Q29) or systematic data destruction (Q51).

The SPECIAL Policy Log Vocabulary introduced by Bonatti et al. [[Bonatti_Dullaert_Fernandez_Kirrane]] addresses the need for transparent and accountable data processing under GDPR. This vocabulary can document data transfers and their legal basis, contributing to Q63 and Q64. However, it lacks specific components for tracking data retention periods (Q8) and procedures for ensuring data accuracy (Q28).

The work by Matulevicius et al. [[Matulevicius_Tom_Kala_Sing]] proposes a method to manage GDPR compliance in business processes using BPMN. Their approach includes a compliance repository that can list all data transfers and document the legal basis for these transfers, addressing Q63 and Q64. However, it does not explicitly address data retention periods (Q8) or the systematic destruction of data (Q51).

Besik and Freytag [[Besik_Freytag]] introduce an ontology-based model to ensure privacy compliance within clinical workflows. Their model can specify data retention periods (Q8) and document data transfers (Q63), but it lacks detailed enforcement mechanisms for data accuracy (Q28) and systematic data destruction (Q51).

Tom et al. [[Tom_Sing_Matulevicius]] propose the GDPRov model to represent GDPR guidelines systematically. This model can be leveraged to ensure personal data is kept up to date (Q28) and document data transfers (Q63). However, it does not include components to specify data retention periods (Q8) or enforce data retention policies (Q29).

Bartolini et al. [[Bartolini_Muthuri_Santos]] use ontologies to model data protection requirements in workflows, aiding data controllers in achieving GDPR compliance. Their ontology helps in understanding obligations and can partially address data accuracy (Q28), but it does not explicitly cover data retention periods (Q8) or systematic data destruction (Q51).

Bonatti et al. [[Bonatti_Kirrane_Petrova_Sauro]] introduce a machine-understandable policy language for GDPR compliance checking. This approach can encode retention periods (Q8) and document the legal basis for data transfers (Q64). However, it lacks mechanisms for ensuring data accuracy (Q28) and systematic data destruction (Q51).

Fatema et al. [[Fatema_Hadziselimovic_Pandit_Debruyne_Lewis_OSullivan]] propose a semantic model for consent and data management, incorporating the lifecycle of consent and data. Their CDMM can specify data retention periods (Q8) and document data transfers (Q63), but it may need further refinement for comprehensive retention policy enforcement (Q29).

Pandit et al. [[Pandit_OSullivan_Lewis_Provenance]] present GDPRov, designed to represent activities and consent information related to personal data processing. This model indirectly contributes to data accuracy (Q28) and can be extended to document retention policies (Q29) and legal bases for transfers (Q64).

Torre et al. [[Torre_Alferez_Soltana_Sabetzadeh_Briand]] developed a model-based representation of GDPR to support automated compliance checking. Their approach includes components to document the legal basis for data transfers (Q64) but does not explicitly address data retention periods (Q8) or systematic data destruction (Q51).

Finally, Pandit et al. [[Pandit_OSullivan_Lewis]] present an early-stage work on extracting provenance metadata from privacy policies. Their approach focuses on data collection and usage activities, not covering retention periods (Q8) or data destruction (Q51).

These studies collectively contribute to various aspects of GDPR compliance, yet highlight the need for a comprehensive model that can systematically address all compliance questions, which our proposed extension to GDPRov aims to achieve.