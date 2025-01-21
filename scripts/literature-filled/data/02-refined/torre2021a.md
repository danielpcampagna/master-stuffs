---
context: True
---


# Torre, Damiano and Alferez, Mauricio and Soltana, Ghanem and Sabetzadeh, Mehrdad and Briand, Lionel. Modeling data protection and privacy: application and experience with GDPR. 2021.

> The complete material regarding points 1-6 can be found in the publicly available Appendices A-C [40].

## Approach and Motivations

This paper extends previous work presented at MODEL 2019, aiming to fill the gap in model-based approaches for compliance verification with the GDPR. The authors developed a comprehensive model-based representation of the GDPR to support automated compliance checking. This approach is motivated by the need for a generic and adaptable model that can be tailored to specific contexts and address challenges in modeling the GDPR.

The paper introduces several key components: nine packages of the GDPR conceptual model developed in Enterprise Architect, a table capturing the traceability of these packages to the GDPR, a complete glossary for the conceptual model, plain-English descriptions of 35 compliance rules derived from the GDPR, an encoding of these rules in OCL, and 20 variation points to specialize the generic model. These components are designed to facilitate a detailed and structured representation of the GDPR, ensuring a clear understanding and application of compliance requirements.

## Approach Contribution For The Compliance Questions

### Question 64: Is there a legal basis for the transfer, e.g. EU Commission adequacy decision; standard contractual clauses. Are these bases documented?

The approach provides a detailed model that includes the concept of adequacy decisions and appropriate safeguards, such as binding corporate rules or EU model clauses. These aspects are captured in the GDPR conceptual model and the compliance rules, which can be tailored to document and verify the legal basis for data transfer.

## Approach Insuficiecies For Fulfill The Compliance Questions

### Question 8: For each category of personal data, list the period for which the data will be retained e.g. one month? one year? As a general rule data must be retained for no longer than is necessary for the purpose for which it was collected in the first place.

The approach does not explicitly address retention periods for personal data categories. While it provides a general framework for GDPR compliance, specific components or rules related to data retention periods are not included.

### Question 28: Are procedures in place to ensure personal data is kept up to date and accurate and where a correction is required, the necessary changes are made without delay?

The model does not include components that ensure personal data is kept up to date and accurate. The focus is more on the structural representation of GDPR requirements rather than operational procedures for data accuracy and updates.

### Question 29: Are retention policies and procedures in place to ensure data are held for no longer than is necessary for the purposes for which they were collected?

Similar to Question 8, the approach lacks specific components to address data retention policies and procedures. It provides a high-level framework but does not delve into the operational details required for managing data retention.

### Question 51: Are personal data systematically destroyed, erased, or anonymised when they are no longer legally required to be retained.

The approach does not cover the systematic destruction, erasure, or anonymization of personal data. These operational aspects are not part of the conceptual model or the compliance rules provided.

### Question 63: Are all transfers listed - including answers to the previous questions (e.g. the nature of the data, the purpose of the processing, from which country the data is exported and which country receives the data and who the recipient of the transfer is?)

The model includes components related to data transfer, such as adequacy decisions and safeguards, but it does not comprehensively list all aspects of data transfers, such as the nature of the data and specific recipients.

## Key Contributions

- Development of a generic and adaptable model-based representation of the GDPR.
- Nine packages of the GDPR conceptual model developed in Enterprise Architect.
- A table capturing the traceability of the conceptual model to the GDPR.
- A complete glossary for the conceptual model (267 entries).
- Plain-English descriptions of 35 compliance rules derived from the GDPR.
- Encoding of the compliance rules in OCL.
- 20 variation points to specialize the generic model and guidelines for their application.
- A publicly available repository with the complete material.

## State-of-the-Art

This approach advances the state-of-the-art by providing a holistic and structured model-based representation of the GDPR, which was previously lacking. It addresses the need for automated compliance checking and offers a detailed framework that can be tailored to specific contexts. The inclusion of a traceability table, a comprehensive glossary, and plain-English compliance rules enhances the clarity and applicability of the model.

Existing model-based approaches have limitations, such as different focus areas or exclusive attention to specific GDPR use cases. This work aims to bridge these gaps by offering a more comprehensive and adaptable solution. The approach also sets the stage for future research by identifying challenges and suggesting strategies for long-term advancements in GDPR compliance analysis.

While the model does not fully address all operational aspects of GDPR compliance, such as data retention and accuracy procedures, it provides a solid foundation for further development and integration with other compliance tools and methodologies.
