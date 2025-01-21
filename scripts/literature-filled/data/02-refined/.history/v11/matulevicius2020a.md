---
context: False
---


# Matulevicius, Raimundas and Tom, Jake and Kala, Kaspar and Sing, Eduard. A Method for Managing GDPR Compliance in Business Processes. 2020.

> [Link to access publication](https://link.springer.com/chapter/10.1007/978-3-030-49418-6_14)

## Approach and Motivations

The publication "A Method for Managing GDPR Compliance in Business Processes" by Matulevicius et al. introduces a novel approach to assist organizations in ensuring compliance with GDPR regulations. The approach is motivated by the need for businesses to systematically manage personal data in alignment with GDPR requirements. This is particularly crucial given the stringent penalties associated with non-compliance and the growing awareness of data privacy among consumers.

The authors present a model that integrates GDPR compliance directly into business process management (BPM). This integration is achieved through a combination of conceptual modeling and practical implementation steps. The model emphasizes the importance of transparency, accountability, and traceability in handling personal data. By embedding GDPR considerations into the BPM lifecycle, the proposed method aims to streamline compliance efforts and reduce the risk of violations.

Central to this approach are specific components such as `DataFlow`, `DataPurpose`, and `ConsentManagement`, which help track and manage personal data throughout its lifecycle. These components are designed to ensure that data processing activities are aligned with GDPR principles, such as data minimization, purpose limitation, and lawful processing.

## Approach Contribution For The Compliance Questions

### Question 28

The approach includes the `DataFlow` component which tracks the flow of personal data within the business processes. This component can be leveraged to ensure that data is kept up to date and accurate by identifying points in the process where data validation and updates are necessary. Additionally, the `ConsentManagement` component can be used to ensure that any corrections to personal data are made promptly and in accordance with the data subject's rights.

### Question 63

The `DataFlow` and `DataPurpose` components provide a structured way to document and track data transfers across different jurisdictions. By detailing the nature of the data, the purpose of processing, and the parties involved in the transfer, these components can be used to create comprehensive records of data transfers, thereby addressing the requirements of Question 63.

### Question 64

The approach includes documenting the legal basis for data processing activities through the `ConsentManagement` component. This component ensures that any data transfer is backed by an appropriate legal framework, such as standard contractual clauses or adequacy decisions. This documentation is essential for demonstrating compliance with GDPR transfer requirements.

## Approach Insuficiecies For Fulfill The Compliance Questions

### Question 8

The approach does not explicitly address data retention periods for different categories of personal data. While `DataFlow` and `DataPurpose` components can track data usage, they do not inherently manage or enforce retention schedules. To fully comply with Question 8, additional mechanisms or policies need to be integrated to specify and enforce retention periods.

### Question 29

Although the approach emphasizes tracking and managing personal data, it lacks explicit components or procedures for enforcing retention policies. The `DataFlow` component can help identify when data is no longer needed, but there is no direct mechanism to ensure that data is systematically deleted or archived according to predefined retention policies.

### Question 51

The proposed method does not provide a systematic approach for the destruction, erasure, or anonymization of personal data once it is no longer required. While the `DataFlow` component can track the lifecycle of data, additional functionalities are needed to manage the secure disposal of data in compliance with GDPR requirements.

## Key Contributions

- Integration of GDPR compliance into Business Process Management (BPM).
- Emphasis on transparency, accountability, and traceability in data handling.
- Introduction of key components:
  - `DataFlow`: Tracks the flow and usage of personal data.
  - `DataPurpose`: Documents the purpose of data processing activities.
  - `ConsentManagement`: Manages consent and legal bases for data processing.
- Conceptual modeling combined with practical implementation steps.
- Focus on data minimization, purpose limitation, and lawful processing.

## State-of-the-Art

The proposed method represents a significant advancement in the integration of GDPR compliance mechanisms within BPM. By embedding compliance considerations directly into business processes, the approach facilitates a more proactive and systematic management of personal data. This is in contrast to reactive compliance measures that are often implemented as separate, standalone activities.

The approach builds on existing BPM methodologies by introducing GDPR-specific components, thereby extending the capabilities of traditional BPM frameworks. Related work in this area includes various tools and frameworks for data governance and privacy management, but none offer the same level of integration with business processes.

One of the key contributions of this work is its emphasis on traceability and accountability, which are critical for demonstrating compliance during audits. By providing a clear and documented trail of data processing activities, the method helps organizations meet GDPR requirements more effectively.

Overall, this publication pushes the boundaries of current BPM practices by incorporating data protection principles directly into the process design and execution phases, thereby setting a new standard for GDPR compliance management.

