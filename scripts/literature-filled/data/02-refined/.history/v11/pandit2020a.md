---
context: True
---


# Pandit, Harshvardhan Jitendra. Representing Activities associated with Processing of Personal Data and Consent using Semantic Web for GDPR Compliance. 2020.

> [Link to the proposed model](https://arxiv.org/abs/2002.01001)

## Approach and Motivations

The publication by Pandit (2020) introduces GDPRov, an ontology designed to assist in the tracking and management of activities and consent information related to the processing of personal data under the General Data Protection Regulation (GDPR). The primary motivation behind GDPRov is to provide a structured and semantically rich representation of GDPR compliance processes, making it easier for data controllers to document and demonstrate compliance with GDPR requirements.

The approach leverages the principles of the Semantic Web to ensure that the representation of data processing activities and consent mechanisms is both machine-readable and interoperable across different systems. GDPRov includes concepts and relationships that are essential for capturing the provenance of data processing activities, ensuring that both ex-ante (prior planning) and ex-post (execution) phases are well-documented.

Incorporating compliance questions as competency questions, GDPRov aims to address specific information requirements necessary for GDPR compliance. By doing so, it ensures that the ontology is both relevant and practical for real-world applications, providing a basis for evaluating and improving GDPR compliance management systems.

## Approach Contribution For The Compliance Questions

- **Question 63**: GDPRov includes concepts for representing the provenance of data processing activities, which can be used to document information about data transfers. The `GDPRtEXT` component can help list the nature of the data, the purpose of the processing, and the countries involved in data transfers, as well as the recipients of the transfers.

## Approach Insuficiencies For Fulfill The Compliance Questions

- **Question 8**: GDPRov does not include specific components to capture retention periods for each category of personal data. The lack of a dedicated concept for retention policies makes it insufficient to fully answer this question.
  
- **Question 28**: While GDPRov focuses on documenting data processing activities, it lacks components to ensure that personal data is kept up to date and accurate. There is no mechanism to track corrections and updates to personal data.
  
- **Question 29**: Similar to Question 8, GDPRov does not have components to document retention policies and procedures, making it inadequate for ensuring data are held only as long as necessary.
  
- **Question 51**: GDPRov does not cover the systematic destruction, erasure, or anonymization of personal data when it is no longer legally required to be retained. This is a significant gap in the ontology.
  
- **Question 64**: While GDPRov can document the transfer of data, it does not include components to capture the legal basis for the transfer, such as EU Commission adequacy decisions or standard contractual clauses. There is also no provision for documenting these bases.

## Key Contributions

- Utilizes Semantic Web technologies to represent GDPR compliance processes.
- Includes concepts and relationships to capture the provenance of data processing activities.
  - `GDPRtEXT`: Linked data representation of GDPR text and glossary of compliance concepts.
  - `GDPRov`: Provenance of activities associated with personal data and consent.
  - `GConsent`: Representation of information regarding consent.
- Ensures documentation of both ex-ante and ex-post phases of data processing activities for comprehensive compliance tracking.
- Evaluated based on competency questions derived from GDPR compliance requirements and validated through use cases and peer-reviewed feedback.

## State-of-the-Art

The approach by Pandit (2020) advances the state-of-the-art by providing a structured and semantically rich ontology for GDPR compliance. It addresses the need for machine-readable and interoperable representations of data processing activities and consent information. By leveraging Semantic Web technologies, GDPRov ensures that compliance documentation is both standardized and extensible.

Related work in the field includes ontologies and frameworks for data protection and privacy, such as PriMa, which focuses on privacy management, and ODRL, which deals with rights and obligations. However, GDPRov distinguishes itself by specifically targeting the provenance of data processing activities and consent mechanisms under GDPR, providing a more focused and comprehensive solution for GDPR compliance.

Overall, GDPRov fills a critical gap in the compliance management landscape, offering a robust tool for data controllers to document and demonstrate their adherence to GDPR requirements effectively.
