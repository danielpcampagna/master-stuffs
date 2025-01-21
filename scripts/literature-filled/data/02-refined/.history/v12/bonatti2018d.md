---
context: False
---


# Bonatti, Piero; Dullaert, Wouter; Fernández, Javier D.; Kirrane, Sabrina; Milosevic; Polleres, Axel. The SPECIAL Policy Log Vocabulary. 2018. 

## Approach and Motivations

The SPECIAL Policy Log Vocabulary is designed to address the need for transparent and accountable data processing under the GDPR. The vocabulary facilitates the logging and querying of data processing activities, ensuring that data processing is in line with user consent and legal requirements. The authors propose a structured approach to logging, centered around RDF (Resource Description Framework) technologies, to create machine-readable logs that can be easily queried and audited.

The vocabulary is composed of several core components, including `DataProcessing`, `Purpose`, `LegalBasis`, `ProcessingContext`, and `LogEntry`. These components are designed to capture essential information about data processing activities, such as the purpose of data processing, the legal basis for processing, the context in which data is processed, and detailed log entries of processing events. This structured approach ensures that data controllers can maintain detailed records of their data processing activities, which are necessary for compliance with GDPR.

The motivations behind this approach include the need for compliance with GDPR's accountability and transparency requirements, the facilitation of user rights such as access and rectification, and the need to provide evidence of compliance to regulatory authorities. By employing RDF technologies, the vocabulary aims to create a flexible and extensible framework that can be adapted to various data processing scenarios.

## Approach Contribution For The Compliance Questions

### Question 63

The SPECIAL Policy Log Vocabulary can contribute to answering Question 63 through its `LogEntry`, `DataProcessing`, `Purpose`, and `ProcessingContext` components. These components can be used to systematically log and query details about data transfers, including the nature of the data, the purpose of processing, the countries involved in the transfer, and the recipients. The `LogEntry` component can capture each transfer event, while the `ProcessingContext` can provide contextual information such as the source and destination countries.

### Question 64

The `LegalBasis` component of the SPECIAL Policy Log Vocabulary is directly relevant to Question 64. It allows for the documentation of the legal basis for data transfers, such as EU Commission adequacy decisions or standard contractual clauses. By logging the legal basis for each data processing activity, the vocabulary ensures that data controllers can provide evidence of compliance with GDPR's transfer requirements.

## Approach Insuficiecies For Fulfill The Compliance Questions

### Question 8

The SPECIAL Policy Log Vocabulary does not include specific components for tracking data retention periods. While it captures detailed information about data processing activities, it lacks a dedicated component for specifying the retention period for each category of personal data. This limitation makes it insufficient for answering Question 8 comprehensively.

### Question 28

Although the vocabulary includes components for logging data processing activities, it does not explicitly address procedures for ensuring that personal data is kept up to date and accurate. There are no specific components related to data accuracy or correction procedures, making it inadequate for answering Question 28.

### Question 29

The vocabulary does not provide components dedicated to retention policies and procedures. While it can log data processing activities, it does not offer a framework for managing and enforcing data retention policies, thus falling short of the requirements of Question 29.

### Question 51

The SPECIAL Policy Log Vocabulary does not include mechanisms for systematically destroying, erasing, or anonymizing personal data when it is no longer required. This lack of functionality means it cannot fully address Question 51.

## Key Contributions

- **Technology Used**: RDF (Resource Description Framework)
- **Core Components**:
  - `DataProcessing`
  - `Purpose`
  - `LegalBasis`
  - `ProcessingContext`
  - `LogEntry`
- **Background Concepts**: GDPR compliance, data provenance, data transparency, and accountability
- **Evaluation**: The model is evaluated based on its ability to log and query data processing activities in compliance with GDPR.

## State-of-the-Art

The SPECIAL Policy Log Vocabulary advances the state-of-the-art by providing a structured and machine-readable way to log data processing activities. This approach stands out due to its use of RDF technologies, which offer flexibility and extensibility in capturing various aspects of data processing. The vocabulary also addresses the GDPR's requirements for accountability and transparency, contributing to the broader effort of making data processing more compliant and auditable.

Compared to existing models, the SPECIAL Policy Log Vocabulary offers a more comprehensive logging framework that can capture detailed information about the legal basis for data processing and the context in which it occurs. This makes it particularly useful for organizations that need to demonstrate GDPR compliance through detailed logs and records.

Related work includes other data provenance models and GDPR compliance tools, but the SPECIAL Policy Log Vocabulary distinguishes itself through its specific focus on logging and its use of RDF for creating highly queryable and interoperable logs. This makes it a valuable contribution to the field of data protection and compliance.
