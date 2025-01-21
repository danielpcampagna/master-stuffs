---
context: False
---


# Besik, Saliha Irem and Freytag, Johann-Christoph. Ontology-Based Privacy Compliance Checking for Clinical Workflows. 2019.

## Approach and Motivations

The publication "Ontology-Based Privacy Compliance Checking for Clinical Workflows" by Saliha Irem Besik and Johann-Christoph Freytag introduces an innovative approach to ensure privacy compliance within clinical workflows through the use of ontology-based models. The authors aim to address the stringent requirements of the General Data Protection Regulation (GDPR) by leveraging ontological representations to model and track data processing activities. The motivation behind this approach is to provide a systematic and automated way to verify compliance, reducing the burden on data controllers and minimizing human errors.

The paper details the structure of the proposed model, which includes components to represent clinical workflows, data categories, processing activities, and compliance rules. By formalizing these elements within an ontology, the authors enable automated reasoning engines to check for compliance violations dynamically. This method is particularly relevant for clinical environments where complex data processing activities are prevalent, and adherence to privacy regulations is critical.

The components introduced by the publication include ontologies for data categories, processing activities, and compliance rules, each of which plays a crucial role in modeling the intricacies of clinical workflows. The authors also demonstrate how these ontologies can be integrated into existing clinical systems to provide real-time compliance checking.

## Approach Contribution For The Compliance Questions

### Question 8

The approach can partially address this question through its ontology for data categories, which can include attributes for data retention periods. By modeling each category of personal data and associating it with predefined retention periods, the system can track and verify if the data is retained for no longer than necessary.

### Question 28

The ontology-based model includes components for processing activities, which can be extended to incorporate procedures for ensuring data accuracy and up-to-dateness. By modeling these activities, the system can verify if procedures are in place and if necessary corrections are made without delay.

### Question 29

The ontology includes compliance rules that can be tailored to ensure data retention policies are in place. By defining these rules within the ontology, the system can automatically check if data is held for no longer than the necessary period and flag any violations.

### Question 51

The compliance rules within the ontology can be extended to include procedures for data destruction, erasure, or anonymization. By modeling these rules, the system can verify if personal data is systematically handled when it is no longer legally required.

### Question 63

The approach can model the nature of the data, purpose of processing, and data transfers within its ontology. By doing so, it can list all transfers and provide detailed information about the data flow, including exporting and receiving countries and recipients.

### Question 64

The ontology can include components to represent the legal basis for data transfers, such as EU Commission adequacy decisions or standard contractual clauses. By documenting these bases within the model, the system can verify if the legal requirements for data transfers are met.

## Approach Insuficiecies For Fulfill The Compliance Questions

### Question 8

While the ontology can model retention periods, it may lack the dynamic capability to enforce these periods automatically without additional integration with data management systems.

### Question 28

The model can represent procedures for data accuracy, but it may not have the mechanisms to enforce real-time data correction without integration with operational data systems.

### Question 29

The ontology can define retention policies, but ensuring these policies are enforced in practice requires integration with data storage and management systems, which may not be covered by the model alone.

### Question 51

The model can specify procedures for data destruction or anonymization, but it may not have the execution capability to perform these actions without additional system integration.

### Question 64

Documenting the legal basis for data transfers within the ontology is feasible, but the model may not be able to verify the legal compliance autonomously without access to external legal databases or documents.

## Key Contributions

- **Ontology-Based Model**: Utilizing ontologies to represent data categories, processing activities, and compliance rules.
  - **Data Categories Ontology**: Models various categories of personal data and associated attributes.
  - **Processing Activities Ontology**: Represents different processing activities and their compliance requirements.
  - **Compliance Rules Ontology**: Defines rules for verifying GDPR compliance dynamically.
- **Automated Compliance Checking**: Enabling automated reasoning to verify compliance with GDPR requirements.
- **Clinical Workflow Integration**: Tailoring the model for clinical environments with complex data processing activities.
- **Reduction of Human Error**: Minimizing manual compliance checks through automation.
- **Flexibility and Extensibility**: Allowing the model to be extended and adapted to different compliance requirements and environments.

## State-of-the-Art

The "Ontology-Based Privacy Compliance Checking for Clinical Workflows" approach advances the state-of-the-art by integrating ontological models with compliance verification processes. Traditional compliance methods often rely on manual checks and static documentation, which are prone to errors and inefficiencies. By leveraging ontologies, this approach allows for dynamic, automated compliance checking, significantly reducing the burden on data controllers.

This work relates to other research efforts in privacy compliance and ontology-based systems, such as those focusing on semantic web technologies and data protection frameworks. It competes with approaches that use rule-based systems and machine learning models for compliance verification but stands out due to its focus on clinical workflows and its comprehensive ontological representation.

Overall, the approach provides a robust framework for ensuring GDPR compliance in clinical settings, contributing to the broader field of privacy-preserving data management and compliance automation.
