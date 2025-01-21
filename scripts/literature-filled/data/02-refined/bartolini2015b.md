---
context: True
---


# Bartolini, Cesare and Muthuri, Robert and Santos, Cristiana. Using ontologies to model data protection requirements in workflows. 2015.

## Approach and Motivations

In this work, the authors present an ontology to model data protection requirements and an approach for integrating it into workflows to express GDPR requirements within business processes. The ontology aims to assist data controllers in achieving compliance with GDPR regulations. The paper illustrates the design and development of the ontology following an initial stage described in previous work. As a proof of concept, an approach is introduced that uses the ontology to enrich workflow models, such as business processes, with annotations that express data protection requirements.

The ontology was modeled by a legal expert, selectively identifying provisions that contain duties for the data controller and rights for data subjects, and building these into the ontology. Despite its coarse granularity, the ontology serves as a foundational structure necessary for long-term goals, such as verifying compliance with GDPR. The approach also aims to benefit various stakeholders, including data controllers, auditors, and Data Protection Authorities (DPAs), by providing a structured means of assessing compliance and detecting potential violations.

The ontology is designed to be adaptable to changes in the legal text, with an improved version under development to cover more provisions and provide a broader perspective on GDPR. The integration with security standards, like ISO 27001:2013, is also explored to facilitate a smoother transition to the new legislation.

## Approach Contribution For The Compliance Questions

### Question 28: Procedures to Ensure Data is Up-to-date and Accurate
The current model can contribute partially to Question 28 through its structured ontology, which helps data controllers understand their obligations. The ontology can be queried by data controllers to clarify their functions and ensure data accuracy and timely updates by referencing specific duties and rights.

## Approach Insufficiencies For Fulfill The Compliance Questions

### Question 8: Data Retention Periods
The current approach does not specifically address the categorization of personal data and the retention periods required for compliance. The ontology's granularity is too coarse, and it lacks specific provisions to list data retention periods explicitly.

### Question 28: Procedures to Ensure Data is Up-to-date and Accurate
While the ontology helps in understanding obligations, it does not provide a direct mechanism to ensure that personal data is kept up to date and accurately corrected without delay. It lacks procedural components that could automate or enforce these requirements.

### Question 29: Retention Policies and Procedures
The ontology does not include specific retention policies or procedures to ensure data is held no longer than necessary. It focuses more on identifying duties and rights rather than implementing retention strategies.

### Question 51: Data Destruction, Erasure, or Anonymisation
The model does not cover the systematic destruction, erasure, or anonymisation of personal data when no longer required. It lacks the components to manage data lifecycle and enforce such actions.

### Question 63: Listing All Data Transfers
The ontology does not specifically list all data transfers, including the nature of the data, processing purposes, and details of the transfers. It also does not document the legal basis for these transfers.

### Question 64: Legal Basis for Data Transfers
Although the model helps identify compliance with GDPR, it does not explicitly document the legal basis for data transfers, such as EU Commission adequacy decisions or standard contractual clauses.

## Key Contributions

- Development of an ontology to model data protection requirements.
- Integration of the ontology into business process workflows.
- Aids data controllers, auditors, and DPAs in understanding and assessing GDPR compliance.
- Identified duties for data controllers and rights for data subjects.
- Initial coarse granularity of the ontology, with plans for more detailed future versions.
- Exploration of the relationship between GDPR and security standards like ISO 27001:2013.

## State-of-the-Art

This approach advances the state-of-the-art by providing a structured ontology to model data protection requirements, which can be integrated into business process workflows. It addresses a critical need for compliance with the evolving GDPR regulations, offering a foundational structure for further refinement and broader coverage. The integration with security standards is also a novel aspect that facilitates a smoother transition to new legislation.

The related work includes other domain legal ontologies within data protection and privacy, but this approach stands out by focusing on GDPR compliance and integrating the ontology into business processes. Future improvements aim at broader coverage and more detailed granularity, enhancing its utility for real-world scenarios.
