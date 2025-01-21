---
context: True
---


# Torre, Damiano and Alferez, Mauricio and Soltana, Ghanem and Sabetzadeh, Mehrdad and Briand, Lionel. Modeling data protection and privacy: application and experience with GDPR. 2021.

> The complete material regarding points 1-6 above can be found in the publicly available Appendices A-C [40].

## Approach and Motivations

This paper presents a holistic model-based approach to represent the General Data Protection Regulation (GDPR) in a structured and adaptable manner. The motivation behind this approach is to support automated compliance checking, which is increasingly necessary as organizations strive to comply with the complex and evolving requirements of the GDPR. The authors have identified several limitations in existing model-based approaches, such as differing focuses, manual application guidelines, and exclusive focus on specific use cases. To address these gaps, the authors developed a generic and adaptable model of the GDPR, which can be tailored to specific contexts and used for automated compliance verification.

The approach involves the creation of nine packages of the GDPR conceptual model in Enterprise Architect. It includes a table mapping the classes in these packages to the GDPR, a comprehensive glossary of terms, a plain-English description of compliance rules derived from the GDPR, an encoding of these rules in the Object Constraint Language (OCL), and a set of variation points to specialize the generic model with guidelines on how to apply them. The model was developed iteratively and incrementally with the involvement of legal experts to ensure its accuracy and relevance.

The authors aim to bridge the gap between software engineers and legal experts by developing more effective communication methods and addressing high-priority automation needs through close collaboration with legal professionals. This approach is expected to enhance the long-term research focus on model-based analysis of GDPR compliance and facilitate the development of future-proof compliance verification models.

## Approach Contribution For The Compliance Questions

### Question 8

The `GDPR conceptual model` includes compliance rules and a table mapping classes to the GDPR. These components could potentially be used to track the retention periods for different categories of personal data, as required by Question 8.

### Question 28

The `compliance rules` and `OCL encoding` can help ensure procedures are in place to keep personal data up-to-date and accurate, as well as to make necessary corrections without delay.

### Question 29

The `GDPR conceptual model` and `variation points` can be used to define and implement retention policies and procedures to ensure data is held no longer than necessary, addressing the requirements of Question 29.

### Question 51

The `compliance rules` and `OCL encoding` can potentially be used to automate the processes for systematically destroying, erasing, or anonymizing personal data when it is no longer legally required, as specified in Question 51.

### Question 63

The `glossary` and `GDPR conceptual model` can help document and list all data transfers, including the nature of the data, purpose of processing, and details about the countries involved and recipients, as required by Question 63.

### Question 64

The `GDPR conceptual model` and `compliance rules` could be used to document and ensure there is a legal basis for data transfers, such as EU Commission adequacy decisions or standard contractual clauses, as specified in Question 64.

## Approach Insuficiecies For Fulfill The Compliance Questions

### Question 8

While the model includes compliance rules and mappings, it does not explicitly address the need for tracking retention periods for each category of personal data. Additional components or extensions may be needed to fully capture and automate this aspect.

### Question 28

Although the model provides tools to ensure data accuracy and timely corrections, it may lack specific procedures or guidelines for implementing these processes in various organizational contexts, necessitating further customization or extensions.

### Question 29

The approach outlines retention policies and procedures but may not comprehensively cover all specific scenarios and requirements for ensuring data is held only as long as necessary, requiring further elaboration or extensions.

### Question 51

The model includes rules for data destruction, erasure, or anonymization, but it may not fully account for the diverse and context-specific legal requirements for data retention, necessitating additional guidelines or components.

### Question 63

While the model documents data transfers, it may not capture all specific details required for comprehensive compliance, such as the exact nature of data and specific legal bases for transfers, requiring further refinement or extensions.

### Question 64

The model addresses the legal basis for data transfers, but it may not provide complete documentation for all possible legal bases and scenarios, necessitating further elaboration or customization to ensure comprehensive compliance.

## Key Contributions

- Development of a holistic, model-based representation of the GDPR.
- Creation of nine packages of the GDPR conceptual model in Enterprise Architect.
  - Table mapping classes to the GDPR (96 entries).
  - Comprehensive glossary of 267 terms.
  - Plain-English description of 35 compliance rules.
  - Encoding of compliance rules in OCL.
  - Set of 20 variation points for model specialization.
- Iterative and incremental development process involving legal experts.
- Bridging the gap between software engineers and legal experts.
- Addressing high-priority automation needs for GDPR compliance.

## State-of-the-Art

This approach advances the state-of-the-art by providing a comprehensive and adaptable model of the GDPR, supporting automated compliance checking. It addresses limitations in existing models by offering a holistic representation that can be tailored to specific contexts and used for various compliance verification tasks. The involvement of legal experts ensures the accuracy and relevance of the model, promoting effective communication between software engineers and legal professionals.

The model's iterative development process and the inclusion of detailed compliance rules, OCL encoding, and variation points for model specialization represent significant advancements over previous approaches. This work sets the stage for future research and development in the area of model-based GDPR compliance verification, highlighting the need for ongoing collaboration between legal and technical experts.

Related works include guidelines for the manual application of GDPR, specific use case-focused models, and approaches with different focuses than GDPR. This approach distinguishes itself by offering a holistic and adaptable model that addresses a broader range of compliance verification needs.
