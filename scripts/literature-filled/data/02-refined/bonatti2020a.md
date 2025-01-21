---
context: True
---


# Bonatti, Piero A and Kirrane, Sabrina and Petrova, Iliana M and Sauro, Luigi. Machine understandable policies and GDPR compliance checking. 2020.

## Approach and Motivations

The paper titled "Machine understandable policies and GDPR compliance checking" by Bonatti, Kirrane, Petrova, and Sauro introduces an approach aimed at automating the compliance checking process for GDPR. The motivation behind this approach stems from the need for technical and organizational measures to support the implementation of the GDPR. The SPECIAL H2020 project aims to address this by providing tools that data controllers and processors can use to ensure their data processing activities comply with GDPR regulations.

The approach leverages a policy language developed in collaboration with legal professionals to express consent, business policies, and regulatory obligations. This language is designed to be machine-understandable, enabling automated compliance checking. The paper also discusses two distinct methods for automated compliance checking: one to verify that data processing aligns with the consent provided by data subjects, and another to ensure that business processes adhere to GDPR's regulatory obligations.

The structure of the paper includes an analysis of the GDPR text, the introduction of the SPECIAL policy language, a discussion on encoding business policies and regulatory obligations, an overview of the compliance checking algorithm, and the results of an initial performance evaluation.

## Approach Contribution For The Compliance Questions

### Question 8
The approach can potentially contribute to answering this question through its `SPECIAL policy language`, which allows the encoding of the `envisaged time limits for erasure of the different categories of data (P5)` as specified by Article 30. This component can be used to define the retention periods for different data categories, aiding in compliance with this requirement.

### Question 28
The approach could relate to this question by using the `SPECIAL policy language` to encode policies that ensure data accuracy and prompt corrections. However, the paper does not explicitly mention mechanisms for keeping data up-to-date or procedures for making necessary corrections without delay.

### Question 29
The `SPECIAL policy language` can encode retention policies and procedures, aiding in ensuring data is held no longer than necessary. Article 30's requirement to describe the envisaged time limits for data erasure (P5) can be used in this context.

### Question 51
The paper does not explicitly address the systematic destruction, erasure, or anonymization of personal data when it is no longer legally required. Therefore, the approach may not fully answer this question.

### Question 63
The approach can partially address this question by using the `SPECIAL policy language` to encode the categories of recipients and transfers of personal data to third countries or international organizations (P4), as required by Article 30.

### Question 64
The paper does not explicitly discuss the legal basis for data transfers or the documentation of such bases. Thus, the approach may not fully cover this question.

## Approach Insuficiencies For Fulfill The Compliance Questions

### Question 28
The approach lacks specific mechanisms or components for ensuring personal data is kept up-to-date and accurate, and for making necessary corrections without delay.

### Question 51
The approach does not provide explicit methods for systematically destroying, erasing, or anonymizing personal data when no longer required, which is necessary to answer this question completely.

### Question 64
The approach does not address the documentation of legal bases for data transfers, nor does it provide components for ensuring compliance with EU Commission adequacy decisions or standard contractual clauses.

## Key Contributions

- **Policy Language**:
  - Developed in collaboration with legal professionals.
  - Encodes consent, business policies, and regulatory obligations.
- **Automated Compliance Checking**:
  - Two methods: one for data processing compliance with consent and another for business processes compliance with GDPR obligations.
- **GDPR Analysis**:
  - Detailed analysis of GDPR requirements and their machine-understandable representation.
- **Compliance Checking Algorithm**:
  - High-level overview and initial performance evaluation.

## State-of-the-Art

The approach contributes to the state-of-the-art by introducing a machine-understandable policy language and automated compliance checking methods. This advances the field of legal informatics by providing technical means to demonstrate GDPR compliance, which is crucial for companies processing personal data.

Related work includes existing GDPR compliance tools that use predefined questionnaires to assess compliance. However, these tools lack support for automated compliance checking, which the SPECIAL project aims to address. The approach builds upon a rich history of policy language research from the Semantic Web community, demonstrating how these technologies can be applied to GDPR compliance.

This work represents a significant step forward in automating the compliance process, reducing the need for manual checks and increasing the efficiency and accuracy of compliance assessments.

