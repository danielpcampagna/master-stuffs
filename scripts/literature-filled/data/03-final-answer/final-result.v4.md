## Related Work

To develop our extension for the GDPRov model, we employed the Snowballing methodology. This iterative technique involves identifying an initial set of relevant papers and then expanding the search by examining the references and citations of these papers. This process continues until no new relevant documents are found. Through this methodology, we meticulously reviewed the literature, resulting in a collection of 178 documents, of which 15 were particularly pertinent and are summarized below.

### Compliance with Data Retention Periods (Q8)

The work by Ryan, Paul, and Pandit, Harshvardhan J., and Brennan, Rob, titled "Building a Data Processing Activities Catalog" [[Ryan_2021]] tackles the challenge of documenting data processing activities, including specifying retention periods using the DCAT-AP and DPV standards. This approach is crucial for ensuring that data categories have defined retention periods, thus aligning with Q8.

Similarly, Campagna, Daniel Prett, da Silva, Altigran Soares, and Braganholo, Vanessa, in "Achieving GDPR Compliance through Provenance" [[Campagna_2020]], introduce a model with temporal components that can inform data subjects about the retention period for their data, addressing the need for retention period documentation.

Ujcich, Benjamin E., Bates, Adam, and Sanders, William H., in "A provenance model for the European union general data protection regulation" [[Ujcich_2018]], offer a model that includes temporal notions and timestamps for data activities, aiding in tracking data retention periods.

Fatema, Kaniz et al. in "Compliance through Informed Consent: Semantic Based Consent Permission and Data Management Model" [[Fatema_2017]], use the Consent and Data Management Model (CDMM) to track the consent and data lifecycle, including retention periods.

### Ensuring Data Accuracy and Updates (Q28)

Ryan, Paul et al. [[Ryan_2021]] also contribute to Q28 by documenting procedures within the catalog to ensure data accuracy and updates, which is essential for keeping personal data up-to-date.

Pandit, Harshvardhan J., O’Sullivan, Declan, and Lewis, Dave, in "GDPR-driven Change Detection in Consent and Activity Metadata" [[Pandit_2018_GDPR]], utilize P-Plan to track the provenance of activities and ensure data accuracy by recording changes and corrections.

Besik, Saliha Irem and Freytag, Johann-Christoph, in "Ontology-Based Privacy Compliance Checking for Clinical Workflows" [[Besik_2019]], present an ontology-based model that can incorporate procedures for data accuracy and updates, ensuring timely corrections.

### Retention Policies and Procedures (Q29)

Ryan, Paul et al. [[Ryan_2021]] address Q29 by documenting retention policies using DCAT-AP and DPV, ensuring data is held no longer than necessary.

Ujcich, Benjamin E. et al. [[Ujcich_2018]], emphasize temporal reasoning and data retention periods, contributing to establishing and enforcing retention policies.

Fatema, Kaniz et al. [[Fatema_2017]], manage retention policies using the CDMM, ensuring data is held only as long as necessary and providing a clear audit trail.

### Systematic Data Destruction, Erasure, or Anonymisation (Q51)

Ryan, Paul et al. [[Ryan_2021]] include metadata about the destruction, erasure, or anonymization of personal data, documenting the lifecycle of data processing activities.

Ujcich, Benjamin E. et al. [[Ujcich_2018]], track data destruction activities, documenting these actions to ensure compliance with data destruction requirements.

Fatema, Kaniz et al. [[Fatema_2017]], define rules for data destruction, erasure, or anonymization within the CDMM, ensuring data is handled appropriately when no longer legally required.

### Comprehensive Listing of Data Transfers (Q63)

Bonatti, Piero et al., in "The SPECIAL Policy Log Vocabulary" [[Bonatti_2018]], facilitate logging and querying of data processing activities, including detailed information about data transfers.

Matulevicius, Raimundas et al., in "A Method for Managing GDPR Compliance in Business Processes" [[Matulevicius_2020]], provide a ComplianceRepository that lists all transfers, including details such as the nature of the data and processing specifics.

Pandit, Harshvardhan J. et al. [[Pandit_2020]], use GDPRtEXT to define the origin and relevance of concepts within GDPR, which can be employed to list all transfers comprehensively.

### Documenting the Legal Basis for Data Transfers (Q64)

Ryan, Paul et al. [[Ryan_2021]] and Bonatti, Piero et al. [[Bonatti_2018]] both incorporate components to document the legal basis for data transfers, such as EU Commission adequacy decisions or standard contractual clauses.

Campagna, Daniel Prett et al. [[Campagna_2020]], include components for tracking data transfers and the legal basis for these transfers, ensuring compliance documentation.

Pandit, Harshvardhan Jitendra et al. [[Pandit_2020]], suggest extending GDPRov to document the legal basis for data transfers, ensuring traceability and compliance with GDPR requirements.

Torre, Damiano et al., in "Modeling data protection and privacy: application and experience with GDPR" [[Torre_2021]], provide a detailed model that includes concepts like adequacy decisions and appropriate safeguards, capturing the legal basis for data transfers.

By integrating these insights and extending the GDPRov model, our work aims to fill the gaps identified in the literature, particularly by leveraging ontologies like the SSN Ontology to handle events related to the legal basis for data retention and deletion.