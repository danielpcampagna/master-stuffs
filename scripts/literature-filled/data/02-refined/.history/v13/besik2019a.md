---
context: True
---


# Besik, Saliha Irem and Freytag, Johann-Christoph. Ontology-Based Privacy Compliance Checking for Clinical Workflows. 2019.

## Approach and Motivations

In their paper, Besik and Freytag propose an ontology-based approach for privacy compliance checking in clinical workflows. The motivation behind this approach stems from the need to safeguard the data privacy of patients while ensuring compliance with binding privacy regulations such as the GDPR. Clinical workflows, which outline tasks necessary for delivering clinical services, often fail to support privacy constraints adequately. Therefore, this ontology-based method aims to detect possible privacy violations within these workflows.

The structure of the paper begins with an introduction to the GDPR and its significance in protecting data privacy within the EU. It then presents the concept of "Privacy by Design" (PbD), which obliges organizations to embed privacy proactively into their technology design. The authors introduce their Privacy-aware Clinical Workflow (PaCW) Ontology, which integrates business process modeling, data privacy, and clinical domains. This ontology is used to verify privacy compliance through semantic reasoning, using a case study of a newborn screening procedure to demonstrate its applicability.

## Approach Contribution For The Compliance Questions

### Question 8: Retention Period
The `Limited Retention Period` principle from the GDPR, detailed in the paper, directly addresses the necessity of specifying retention periods for personal data. The PaCW Ontology can potentially be used to ensure that personal data is kept only as long as necessary for the specified purpose.

### Question 29: Retention Policies and Procedures
Similarly, the `Limited Retention Period` principle is relevant here as well. The ontology-based approach can help verify whether data retention policies and procedures are in place and adhered to, ensuring that data is not held longer than necessary.

### Question 51: Data Destruction
While the paper does not explicitly address the destruction of data, the `Limited Retention Period` principle implies that data should be erased when no longer necessary. The compliance checking mechanism within the PaCW Ontology could be adapted to ensure that data is systematically destroyed, erased, or anonymized when it is no longer required.

## Approach Insuficiencies For Fulfill The Compliance Questions

### Question 8: Retention Period
The current model does not provide a detailed mechanism or component dedicated to tracking and enforcing specific retention periods for each category of personal data. Thus, it may not fully satisfy the requirement to list retention periods comprehensively.

### Question 28: Data Accuracy and Updates
The model lacks components to ensure that personal data is kept up to date and accurate, and that necessary changes are made without delay. The PaCW Ontology does not address procedures for data correction and updates.

### Question 29: Retention Policies and Procedures
Although the `Limited Retention Period` principle is addressed, the model does not provide comprehensive procedures or mechanisms for enforcing retention policies beyond the conceptual level.

### Question 51: Data Destruction
The approach does not include specific procedures or components for ensuring the systematic destruction, erasure, or anonymization of personal data when it is no longer required.

### Question 63: Transfer Listings
The model does not address the listing of data transfers, including details such as the nature of the data, the purpose of processing, and recipient information.

### Question 64: Legal Basis for Transfer
There is no component within the PaCW Ontology that documents the legal basis for data transfers, such as EU Commission adequacy decisions or standard contractual clauses.

## Key Contributions

- **Integration of Domains**: Combines business process modeling, data privacy, and clinical domains.
- **Ontology Development**: Introduces the Privacy-aware Clinical Workflow (PaCW) Ontology.
- **Semantic Reasoning**: Uses ontology-based reasoner to verify privacy compliance.
- **Case Study Implementation**: Demonstrates applicability with a newborn screening procedure.
- **GDPR Principles**: Focuses on key GDPR principles like `Purpose Specification`, `Data Minimization`, `Consent Check`, and `Limited Retention Period`.

## State-of-the-Art

The approach by Besik and Freytag advances the state-of-the-art by integrating semantic reasoning into privacy compliance checking for clinical workflows, a domain where privacy is particularly significant due to the sensitivity of health data. Unlike traditional business process models, the PaCW Ontology provides a structured way to embed privacy considerations directly into the workflow design.

This work is related to and builds upon previous research in privacy enforcement in data analysis workflows and ontology-based business process compliance checking. It extends these concepts to the clinical domain, where the stakes for data privacy are higher. The ontology-based method offers a more comprehensive and proactive approach to ensuring privacy compliance, aligning with the GDPR's `Privacy by Design` principle.

However, the model still lacks components to address all the detailed compliance questions comprehensively, particularly those related to data accuracy, specific retention periods, and data transfer documentation. Future work could focus on expanding the ontology to cover these areas more thoroughly and developing more detailed procedures for enforcing privacy policies.
