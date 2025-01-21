---
context: True
---


# Fatema, Kaniz and Hadziselimovic, Ensar and Pandit, Harshvardhan J and Debruyne, Christophe and Lewis, Dave and O'Sullivan, Declan. Compliance through Informed Consent: Semantic Based Consent Permission and Data Management Model. 2017. ISWC

## Approach and Motivations

The approach presented in this publication proposes a semantic model for consent that leverages existing models of provenance, processes, permission, and obligations to ensure compliance with GDPR requirements. The motivations behind this approach include the need to satisfy GDPR's requirements for specificity and unambiguity in user consent and to enable organizations to efficiently demonstrate their compliance. The model aims to make consent explicit, establish a common understanding, and enable the re-use of consent.

The paper introduces a Consent and Data Management Model (CDMM) that uses an open vocabulary for expressing consent. This model incorporates changes in the context of the relationship between data controllers and data subjects into the data processing activities. By doing so, it seeks to improve the integration of data management systems and to help controllers demonstrate compliance with GDPR.

The reference architecture proposed in the paper aims to automate the reasoning over the contextual integrity of the relationship between user consent and compliance by service providers. The implementation of the ontology in Protégé and the use of XACML for machine-enforceable consent permissions are key components of this approach.

## Approach Contribution For The Compliance Questions

### Question 8
The `Consent and Data Management Model (CDMM)` incorporates the lifecycle of consent and data. This includes the period for which the data will be retained as part of the consent information. The `Provenance` component can be used to track the retention period associated with each category of personal data, ensuring it is retained no longer than necessary.

### Question 28
The model's focus on the lifecycle of consent and data can help ensure that personal data is kept up to date and accurate. The `Processes` and `Obligations` components can be utilized to define procedures for data correction and updates, ensuring that necessary changes are made without delay.

### Question 29
Retention policies can be managed using the `Permission` and `Provenance` components of the CDMM. These components ensure that data is held only for as long as necessary and provide a clear audit trail for data retention decisions.

### Question 51
The `Obligations` component can define rules for the systematic destruction, erasure, or anonymization of personal data. The `Provenance` component tracks compliance with these rules, ensuring data is handled appropriately when no longer legally required.

### Question 63
The `Provenance` component can document all data transfers, including the nature of the data, purpose of processing, and details of the transfer. This ensures comprehensive tracking of data flows and compliance with GDPR requirements.

### Question 64
The `Permission` component can record the legal basis for data transfers, such as EU Commission adequacy decisions or standard contractual clauses. This information can be documented and managed within the CDMM to demonstrate compliance.

## Approach Insuficiecies For Fulfill The Compliance Questions

### Question 8
The current model might not fully cover the granularity required for all possible retention scenarios across different categories of personal data. It may need further refinement to address specific retention periods comprehensively.

### Question 28
While the model addresses data corrections and updates, it might lack the detailed mechanisms to automatically ensure all data remains up to date across multiple databases and systems, especially in complex environments.

### Question 29
The model's approach to retention policies may need more detailed guidelines and enforcement mechanisms to ensure that data is not retained longer than necessary in all possible scenarios.

### Question 51
The systematic destruction, erasure, or anonymization processes might require more specific implementation details to ensure they are carried out consistently across different systems and platforms.

### Question 63
Although the model tracks data transfers, it might not cover all the complexities involved in international data transfers and the specific legal requirements for each transfer case.

### Question 64
While the model records the legal basis for transfers, it might require additional components to ensure that all legal bases are documented and managed correctly across different jurisdictions and regulatory environments.

## Key Contributions

- **Open Vocabulary for Expressing Consent**:
  - Leveraging existing open ontology models.
  - Improving integration across different information systems.
- **Machine Readable and Enforceable Consent**:
  - Mapping consent into XACML for policy enforcement.
- **Consent and Data Management Model (CDMM)**:
  - Incorporating consent and data lifecycle.
  - Addressing changes in context and ensuring compliance.
- **Implementation in Protégé**:
  - Preliminary ontology version implemented.
  - Use of XACML for consent permission enforcement.

## State-of-the-Art

This approach advances the state-of-the-art by providing a semantic model for consent that addresses GDPR requirements for specificity and unambiguity. By integrating existing models of provenance, processes, permission, and obligations, it creates a comprehensive framework for managing consent and data processing activities. 

The use of XACML for machine-enforceable consent permissions provides a robust mechanism for ensuring compliance. The proposed CDMM offers a structured approach to handling the lifecycle of consent and data, improving the ability of organizations to demonstrate their compliance with GDPR.

Related works include ontology-based tools for reasoning about consent permission and integrating patient consent in e-health access control. However, this approach distinguishes itself by focusing on the comprehensive management of consent and data lifecycle, incorporating changes in context, and providing automated reasoning over contextual integrity.

