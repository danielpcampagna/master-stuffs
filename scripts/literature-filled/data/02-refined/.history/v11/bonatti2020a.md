---
context: True
---


# Bonatti, Piero A., Kirrane, Sabrina., Petrova, Iliana M., Sauro, Luigi. Machine understandable policies and GDPR compliance checking. 2020.

## Approach and Motivations

The paper introduces the SPECIAL H2020 project, which is designed to assist data controllers and processors in ensuring that their data processing operations comply with the General Data Protection Regulation (GDPR). The approach is motivated by the need for technical and organizational measures to support the legally mandated requirements of the GDPR. The project focuses on providing automated tools to check compliance with GDPR obligations, thus reducing the burden on companies that need to demonstrate compliance.

The SPECIAL project primarily contributes two key components: a policy language that can express consent, business policies, and regulatory obligations, and automated compliance checking mechanisms. These tools enable the verification of whether data processing activities align with the consent given by data subjects and whether business processes conform to GDPR regulations.

The approach leverages existing work in policy language research from the Semantic Web community, aiming to make policies machine-understandable. This enables automated compliance checking, which is a significant improvement over manual methods that are error-prone and time-consuming.

## Approach Contribution For The Compliance Questions

### Question 8
The SPECIAL policy language can encode the `P5` component to specify the envisaged time limits for erasure of different categories of data. This helps in addressing the retention period question.

### Question 28
The approach does not specifically mention procedures for ensuring data accuracy and timely correction. Therefore, no direct component can contribute to this compliance question.

### Question 29
The SPECIAL policy language can be partially related to `P5`, which involves retention policies. However, it doesn't fully cover procedures to ensure data are held only as long as necessary.

### Question 51
The approach includes provisions for the erasure of data (related to `P5`), but it does not cover systematic destruction, erasure, or anonymization once data is no longer legally required.

### Question 63
The SPECIAL policy language and `P3` component can help track categories of recipients and cross-border data transfers, contributing to the listing of transfers.

### Question 64
The approach does not explicitly mention the legal basis for data transfers or documentation thereof, so it doesn't directly contribute to this question.

## Approach Insuficiencies For Fulfill The Compliance Questions

### Question 28
The approach lacks specific procedures or automated mechanisms to ensure data accuracy and timely correction. This requires additional procedural components that are not covered by the current model.

### Question 29
Although the `P5` component helps in specifying retention periods, the approach does not fully address the entire scope required for retention policies and procedures, such as regular audits and reviews.

### Question 51
The model does not include specific methods for the systematic destruction, erasure, or anonymization of data once it is no longer needed, which is essential for full compliance.

### Question 64
The approach does not provide mechanisms for documenting the legal basis for data transfers, such as EU Commission adequacy decisions or standard contractual clauses, which are critical for answering this question comprehensively.

## Key Contributions

- Development of a policy language to express consent, business policies, and regulatory obligations.
- Automated compliance checking mechanisms to verify GDPR compliance.
  - `P1` to `P6` components to describe various aspects of data usage.
  - Transparency ledger to record consent.
- High-level compliance checking algorithm and initial performance evaluation.
- Collaboration with legal professionals to ensure accurate legal interpretations.

## State-of-the-Art

The SPECIAL project advances the state-of-the-art by integrating machine-understandable policies with automated compliance checking, which is a step beyond traditional manual methods. This approach leverages Semantic Web technologies, offering a more robust and scalable solution for GDPR compliance.

The project builds on a rich history of policy language research, aiming to make legal requirements machine-readable and verifiable. This not only improves the accuracy of compliance checks but also reduces the time and effort required by data controllers and processors.

The approach is related to other GDPR compliance tools that use predefined questionnaires. However, SPECIAL goes further by providing automated checks, which is a significant improvement in terms of efficiency and reliability.

Overall, the SPECIAL project sets a new standard for GDPR compliance tools by combining legal knowledge representation with advanced automated checking mechanisms.
