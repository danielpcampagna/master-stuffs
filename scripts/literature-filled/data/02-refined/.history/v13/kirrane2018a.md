---
context: True
---


# Kirrane, Sabrina and Fernández, Javier D and Dullaert, Wouter and Milosevic, Uros and Polleres, Axel and Bonatti, Piero A and Wenning, Rigo and Drozd, Olha and Raschke, Philip. A scalable consent, transparency and compliance architecture. 2018.

> https://purl.com/specialprivacy/demos/ESWC2018

## Approach and Motivations

In their 2018 paper, the authors introduce the SPECIAL consent, transparency, and compliance system. This system is designed to provide data subjects with greater control over their personal data processing and sharing, while also enabling data controllers and processors to meet the consent and transparency obligations mandated by the European General Data Protection Regulation (GDPR). The SPECIAL system differentiates itself from existing GDPR compliance tools by offering automatic compliance checking rather than relying solely on self-assessment questionnaires.

The authors propose a system that records both usage policies and data processing events in a manner that supports automatic compliance verification. This approach leverages the Resource Description Framework (RDF) to express usage constraints, data processing, and sharing events, ensuring transparency and compliance. The system includes components such as consent management and transparency dashboards, which allow users to grant or revoke consent and monitor data processing activities.

The structure of the paper includes an introduction to the significance of data and GDPR obligations, a review of related works, a description of the SPECIAL system's architecture, and a discussion on RDF vocabularies for usage policies and events. The paper concludes with insights into future work, including system benchmarking and security hardening.

## Approach Contribution For The Compliance Questions

- **Question 63**: The SPECIAL system can contribute to this question by recording and providing transparency on data transfers. The `Consent and Transparency & Compliance Dashboards` allow users to see which data is being processed and shared, including the nature of the data and the purpose of processing. This can be aligned with the requirement to list all transfers, including the nature of the data, the purpose, and the recipient.

## Approach Insufficiencies For Fulfill The Compliance Questions

- **Question 8**: The system lacks a specific component for tracking and listing the retention period for each category of personal data. While the `Consent and Transparency & Compliance Dashboards` provide transparency on data processing events, they do not explicitly address data retention periods.
- **Question 28**: There is no mention of procedures to ensure data accuracy and prompt corrections. The system focuses more on transparency and consent management rather than data accuracy.
- **Question 29**: The system does not include specific retention policies and procedures to ensure data is held only as long as necessary. The focus is on compliance with data processing and sharing practices rather than data retention.
- **Question 51**: The system does not explicitly address the destruction, erasure, or anonymization of personal data when no longer legally required.
- **Question 64**: The system does not provide information on the legal basis for data transfers. While it offers transparency on data processing events, it does not document legal bases such as EU Commission adequacy decisions or standard contractual clauses.

## Key Contributions

- Introduction of the SPECIAL consent, transparency, and compliance system.
- Automatic compliance checking for GDPR obligations.
- Use of RDF vocabularies to express usage constraints and data processing events.
- Components:
  - `Consent and Transparency & Compliance Dashboards`
- Focus on transparency and user control over personal data.
- Future work includes system benchmarking and security improvements.
- Supported by the European Union’s Horizon 2020 research and innovation programme.

## State-of-the-Art

The SPECIAL system advances the state-of-the-art by providing a scalable architecture for GDPR compliance that emphasizes automatic verification over manual self-assessment. This approach addresses the need for transparency and user control in personal data processing, which is critical given the increasing importance of data in various domains.

The system's use of RDF vocabularies for expressing usage policies and data processing events is a novel contribution, enabling detailed and structured representations of data processing activities. This contrasts with traditional methods that rely on general descriptions and manual compliance checks.

Related works include tools from the Information Commissioner’s Office (ICO), Microsoft, and Nymity, which focus on self-assessment through questionnaires. The SPECIAL system offers a more dynamic and automated solution, setting it apart from these existing tools. However, it still lacks components for addressing data retention, accuracy, and legal basis for transfers, indicating areas for future enhancement.
