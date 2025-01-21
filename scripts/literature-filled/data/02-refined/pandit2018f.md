---
context: True
---


# Pandit, Harshvardhan J, O’Sullivan, Declan, and Lewis, Dave. GDPR-driven Change Detection in Consent and Activity Metadata. 2018.

## Approach and Motivations

This paper discusses an approach to detect and represent changes in the context of consent and activities for GDPR compliance. The focus is on metadata-driven change detection to assist in the management and demonstration of GDPR compliance. The authors utilize two main technologies: P-Plan (an extension of PROV) for representing the provenance of activities, and ODRL for representing consent.

The motivation stems from the evolving nature of consent under GDPR, where individuals can change or withdraw their consent, necessitating changes in the corresponding activities that process personal data. The paper explores how changes in consent impact workflows and how these changes can be recorded and queried to demonstrate compliance.

A use-case involving a fitness tracking service is utilized to illustrate the approach. In this scenario, a user withdraws consent for receiving advertisements, which leads to a change in the workflow to reflect this withdrawal. The changes are detected, recorded, and linked in a cause-effect relationship to ensure compliance with GDPR requirements.

## Approach Contribution For The Compliance Questions

### Question 28

The approach can contribute to ensuring that personal data is kept up to date and accurate by using `P-Plan` to track the provenance of activities. When a correction is made, the changes can be recorded and linked to the original activities, ensuring that updates are made without delay.

### Question 29

The approach can somewhat address this question by using `P-Plan` to model changes in workflows and `ODRL` to represent consent changes. However, it does not specifically address retention policies and procedures for ensuring data is held no longer than necessary.

### Question 51

The approach can contribute to this question by using `P-Plan` to track the provenance of data destruction activities. When personal data is no longer required, the corresponding workflow changes can be recorded and linked to demonstrate compliance with data destruction requirements.

## Approach Insuficiencies For Fulfill The Compliance Questions

### Question 8

The approach lacks components to record and query the retention period for each category of personal data. The focus is on consent changes and workflow provenance, not on retention periods.

### Question 29

While the approach tracks changes in workflows and consent, it does not provide detailed mechanisms for enforcing retention policies and procedures. Additional components or policies would be needed to fully address this question.

### Question 63

The current model does not cover the detailed tracking of data transfers, including the nature of the data, the purpose of processing, and the recipient information. The focus is primarily on consent changes and activity provenance.

### Question 64

The approach does not address the legal basis for data transfers or the documentation of such bases. Additional components would be required to track and document the legal justifications for data transfers.

## Key Contributions

- **Metadata-Driven Change Detection**:
  - Use of `P-Plan` to represent the provenance of activities.
  - Use of `ODRL` to represent consent.
- **Change Representation**:
  - Linking changes in consent to corresponding changes in workflows.
- **GDPR Compliance**:
  - Providing a method to query and demonstrate compliance based on changes in consent and activities.
- **Use-Case Illustration**:
  - Example involving a fitness tracking service to demonstrate the practical application of the approach.

## State-of-the-Art

This approach advances the state-of-the-art by integrating provenance tracking with consent management to address GDPR compliance. The use of `P-Plan` and `ODRL` provides a structured way to represent and query changes, which is crucial for demonstrating compliance in dynamic environments where consent can change over time.

Compared to existing models, this approach offers a novel way to link consent changes to workflow changes, enabling more effective compliance management. However, it is limited in scope and does not address all aspects of GDPR compliance, such as data retention and transfer documentation, indicating areas for future research.

