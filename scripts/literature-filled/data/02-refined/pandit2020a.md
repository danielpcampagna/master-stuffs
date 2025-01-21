---
context: True
---


# PANDIT, HARSHVARDHAN JITENDRA. Representing Activities associated with Processing of Personal Data and Consent using Semantic Web for GDPR Compliance. 2020.

> https://w3id.org/GDPRov/

## Approach and Motivations

The approach presented in this publication focuses on the GDPRov (GDPR Provenance Ontology), which is designed to represent activities and consent information related to the processing of personal data in compliance with the General Data Protection Regulation (GDPR). The primary motivation behind this approach is to provide a structured and comprehensive way to document both planned (ex-ante) and executed (ex-post) activities to demonstrate GDPR compliance.

The ontology builds on existing standards like PROV-O and P-Plan, extending them to cover specific GDPR compliance requirements. GDPRov uses GDPRtEXT to define the origin and relevance of its concepts within the GDPR, ensuring that all represented activities are traceable back to the regulation's text. The model was created, documented, and published using a rigorous methodology, and it aims to assist controllers in tracking activities and consent information associated with personal data processing.

The structure of the paper includes an introduction to the need for such an ontology, a detailed description of the GDPRov model, its components (such as `p-plan:Plan`, `p-plan:Step`, and properties like `p-plan:isStepOfPlan`), and an evaluation of its effectiveness using competency questions derived from GDPR compliance requirements.

## Approach Contribution For The Compliance Questions

### Question 28
The approach described in the publication indirectly contributes to answering this question. GDPRov's focus on documenting activities and consent information could be extended to include procedures for updating and correcting personal data. By using concepts and relationships to represent these activities, it could potentially ensure that personal data is kept up to date and accurate (e.g., using `p-plan:Step` to represent data correction actions).

### Question 29
GDPRov can be extended to document retention policies and procedures by leveraging its existing framework for representing processes. The ontology can be adapted to include specific processes for data retention and deletion, ensuring data is held only as long as necessary. However, this is not explicitly covered in the current model.

### Question 63
GDPRov's use of GDPRtEXT to define the origin and relevance of concepts within GDPR can be employed to list all transfers, including the nature of the data, purpose of processing, and transfer details. However, the model would need to be extended to fully capture and represent all aspects of data transfers comprehensively.

### Question 64
The current model's ability to document planned and executed activities could be extended to include the legal basis for data transfers. By representing these legal bases as part of the compliance processes, GDPRov could help in documenting and tracking compliance with GDPR requirements related to data transfers.

## Approach Insuficiecies For Fulfill The Compliance Questions

### Question 8
The GDPRov model does not currently include components for specifying retention periods for different categories of personal data. This would require additional properties or extensions to represent data retention schedules explicitly.

### Question 28
While GDPRov can document activities, it lacks specific components to ensure that data is kept up to date and accurate. This would require additional properties or mechanisms to track data updates and corrections systematically.

### Question 29
The model does not explicitly cover retention policies and procedures. Extending the ontology to include these aspects would be necessary to fully address this compliance question.

### Question 51
GDPRov does not include specific components for systematically destroying, erasing, or anonymizing personal data. This would require additional extensions to represent these actions within the ontology.

### Question 63
The current model does not comprehensively cover all aspects of data transfers, such as the details of the transfer process, the nature of the data, and the recipient information. These would need to be explicitly included in the ontology.

### Question 64
The legal basis for data transfers is not currently documented within GDPRov. Extending the model to represent these legal bases and their documentation would be necessary to answer this question fully.

## Key Contributions

- **Extension of PROV-O and P-Plan** to represent GDPR compliance activities.
  - **Components**: `p-plan:Plan`, `p-plan:Step`, `p-plan:isStepOfPlan`, and others.
- **Use of GDPRtEXT** to define the origin and relevance of concepts within GDPR.
- **Documentation of both ex-ante and ex-post activities** to demonstrate GDPR compliance.
- **Evaluation using competency questions** derived from GDPR compliance requirements.

## State-of-the-Art

The GDPRov model advances the state-of-the-art by providing a structured and comprehensive way to document GDPR compliance activities using semantic web technologies. Unlike other approaches that emerged later, GDPRov uniquely integrates PROV-O and P-Plan to represent both planned and executed activities, ensuring a complete documentation of compliance processes.

The model also differentiates itself by using GDPRtEXT to link concepts directly to the GDPR text, ensuring traceability and relevance. While there are other approaches, such as SPECIAL, that use provenance vocabularies for GDPR compliance, GDPRov expands on these by including representations of plans or templates to indicate the association between ex-ante and ex-post phases.

Overall, GDPRov provides a novel and robust framework for documenting GDPR compliance activities, contributing significantly to the field of GDPR compliance and semantic web technologies.
