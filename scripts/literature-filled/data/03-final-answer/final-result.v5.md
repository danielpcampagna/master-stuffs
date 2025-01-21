## Related Work

To identify the relevant literature for our work on extending the GDPRov model, we employed the Snowballing methodology. This approach involves iteratively searching for references in initially identified papers and then exploring the references of those papers, and so on. This method allows for a comprehensive and systematic review of the literature. At the end of the process, we achieved a total of 178 documents, of which 15 were summarized and discussed within the Markdown Content section.

### Compliance Question Q8: Data Retention Periods

Ryan et al. [[Ryan2021]] introduce a metadata-based approach to describing data processing activities with the integration of DCAT-AP and DPV standards. This approach aids in listing the retention period for each category of personal data by specifying temporal periods in metadata, thus contributing to compliance with data retention requirements.

Campagna et al. [[Campagna2020]] enhance a data provenance model by introducing elements that can represent data retention periods using temporal relations like `startedAtTime` and `endedAtTime`. This helps in informing data subjects about the period their data will be stored.

Bonatti et al. [[Bonatti2020]] discuss using a machine-understandable policy language developed for the SPECIAL project that can encode time limits for data erasure, thereby addressing data retention requirements specified in Article 30 of the GDPR.

Fatema et al. [[Fatema2017]] present a Consent and Data Management Model (CDMM) that incorporates the lifecycle of consent and data, including retention periods. The model uses provenance components to track how long data is retained, ensuring compliance with data retention policies.

### Compliance Question Q28: Data Accuracy and Updates

Ryan et al. [[Ryan2021]] contribute to ensuring data accuracy by documenting procedures within catalogs that include assigning contact points and limiting scope to organizational units, thus supporting maintenance of up-to-date and accurate data.

Pandit et al. [[Pandit2018]] propose a semantic model for consent that includes lifecycle management of consent and data. This model is aimed at ensuring that personal data is kept up to date and accurate by defining processes for data correction and updates.

Bonatti and colleagues [[Bonatti2020]] also offer a potential solution by encoding policies to ensure data accuracy within their policy language, even though they do not explicitly mention mechanisms for keeping data updated.

Bartolini et al. [[Bartolini2015]] provide an ontology to model data protection requirements, which can partially help data controllers understand their obligations regarding data accuracy and timely updates by querying specific duties and rights.

### Compliance Question Q29: Retention Policies and Procedures

Ryan et al. [[Ryan2021]] and Campagna et al. [[Campagna2020]] provide foundational models that can be extended to include data retention policies and procedures by leveraging their existing frameworks for representing processes and temporal documentation.

Pandit et al. [[Pandit2020]] present the GDPRov model, which could be adapted to document retention policies and procedures. While not explicitly covered, the ontology's existing framework can be extended to track data retention and deletion activities.

Fatema et al. [[Fatema2017]] describe how the CDMM can manage retention policies using permission and provenance components to ensure data is held only as long as necessary, providing a clear audit trail for data retention decisions.

Bonatti et al. [[Bonatti2020]] mention encoding retention policies in their policy language, aiding in ensuring data is held no longer than necessary and aligning with GDPR's requirements for data retention.

### Compliance Question Q51: Data Destruction, Erasure, and Anonymisation

Ryan et al. [[Ryan2021]] discuss documenting the lifecycle of data processing activities, including the destruction, erasure, or anonymization of personal data, though not in detail.

Pandit et al. [[Pandit2020]] propose an ontology that can be extended to represent systematic destruction and anonymization of data when it is no longer legally required. However, specific components for these processes are not included in the current model.

Fatema et al. [[Fatema2017]] include obligations within the CDMM to define rules for data destruction and anonymization, ensuring compliance with GDPR requirements for data lifecycle management.

Bonatti et al. [[Bonatti2020]] and Torre et al. [[Torre2021]] do not explicitly address the systematic destruction, erasure, or anonymization of personal data, indicating a gap in their approaches.

### Compliance Question Q63: Data Transfers

Ryan et al. [[Ryan2021]] and Pandit et al. [[Pandit2020]] discuss using metadata and provenance to list data transfers, including the nature of the data, purpose of processing, and recipient information. However, they may require additional components to cover all aspects comprehensively.

Campagna et al. [[Campagna2020]] and Bonatti et al. [[Bonatti2020]] provide models that can be extended to document data transfers and their details, though not all aspects are fully covered in their current implementations.

Fatema et al. [[Fatema2017]] use the CDMM to document data transfers, including provenance components to track data flows and ensure compliance with GDPR requirements.

### Compliance Question Q64: Legal Basis for Data Transfers

Bonatti et al. [[Bonatti2020]] and Torre et al. [[Torre2021]] address the legal basis for data transfers by documenting adequacy decisions and safeguards, such as EU model clauses, within their models to ensure compliance with legal requirements.

Ryan et al. [[Ryan2021]] and Pandit et al. [[Pandit2020]] mention the need for documenting the legal basis for data transfers but do not provide explicit components for this purpose.

Fatema et al. [[Fatema2017]] include permission components in the CDMM to record the legal basis for data transfers, such as EU Commission adequacy decisions or standard contractual clauses.

By reviewing these 15 studies, we identified gaps in current models and proposed extensions to GDPRov to address uncovered compliance questions, such as incorporating the SSN ontology for representing sensor components to automatically delete data when it no longer has a legal basis. This comprehensive review lays the foundation for our contributions to the field of GDPR compliance.