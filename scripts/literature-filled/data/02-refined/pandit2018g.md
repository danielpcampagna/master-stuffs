---
context: True
---


# Pandit, Harshvardhan Jitendra, O’Sullivan, Declan, and Lewis, Dave. Extracting provenance metadata from privacy policies. 2018.

## Approach and Motivations

In this paper, the authors present their early-stage work on the identification, extraction, and representation of provenance metadata found in privacy policies. The motivation behind this work is the difficulty users face in understanding privacy policies, which are legal documents describing activities over personal data such as collection, usage, processing, sharing, and storage. The approach leverages keyword-based entity extraction using GDPR terms and concepts provided by the GDPRtEXT resource. Additionally, the authors utilize a machine-learning model from the UsablePrivacy project to annotate privacy policies.

The paper details how the extracted provenance metadata is represented using GDPRov, an ontology that extends PROV-O and P-Plan to model data flows involving consent and data using GDPR terminology. This novel representation allows for an abstract model of the policy to be created, which can be applied to several important topics related to privacy and data practices. The work aims to provide structured information about real-world usage of personal data, which is currently lacking, thereby improving legal accountability and data usage modeling.

## Approach Contribution For The Compliance Questions

### Question 8
The current approach does not specifically address the retention period for each category of personal data. The focus is on extracting and representing provenance metadata related to data collection, usage, processing, sharing, and storage, rather than the retention periods.

### Question 28
The approach does not cover procedures for ensuring personal data is kept up to date and accurate. The extraction of provenance metadata is centered around the activities over personal data rather than the accuracy and updating procedures.

### Question 29
Similar to Question 8, the approach does not address retention policies and procedures. It is focused on the identification, extraction, and representation of provenance metadata related to the handling of personal data.

### Question 51
The approach does not provide mechanisms for ensuring the systematic destruction, erasure, or anonymization of personal data. The extracted metadata deals with the collection and usage activities rather than the end-of-life processes for personal data.

### Question 63
The current approach does not list all transfers of personal data, including details about the nature of the data, purpose of processing, and details of cross-border transfers. It is primarily aimed at extracting provenance metadata related to data handling activities within privacy policies.

### Question 64
The approach does not address the legal basis for data transfers. It focuses on representing the data flows and activities involving personal data rather than the legal justifications for data transfers.

## Approach Insufficiencies For Fulfil The Compliance Questions

### Question 8
The model lacks components to capture the retention period for each category of personal data. The current focus is on provenance metadata related to data handling activities, not on retention schedules.

### Question 28
There are no mechanisms in place within the model to ensure that personal data is kept up to date and accurate. The approach does not cover procedures for data accuracy and timely corrections.

### Question 29
Retention policies and procedures are not part of the model. The approach focuses on the extraction and representation of provenance metadata related to data handling activities, not on data retention.

### Question 51
The model does not include components for the systematic destruction, erasure, or anonymization of personal data. Its focus is on the activities involving personal data, not on its end-of-life processes.

### Question 63
The approach does not encompass the listing of all data transfers or the details of such transfers. It is primarily aimed at extracting metadata related to data handling activities within privacy policies.

### Question 64
The model does not address the legal basis for data transfers. It focuses on data flows and activities involving personal data, rather than the legal justifications for transfers.

## Key Contributions

- Introduction of a keyword-based entity extraction approach using GDPR terms and concepts.
- Utilization of the UsablePrivacy project's machine-learning model for annotating privacy policies.
- Development of the GDPRov ontology to represent extracted provenance metadata.
  - GDPRov extends PROV-O and P-Plan for modeling data flows involving consent and data using GDPR terminology.
- Identification of provenance metadata in privacy policies.
- Representation of complex data handling activities using RDF triples.

## State-of-the-Art

This approach advances the state-of-the-art by providing a structured method for extracting and representing provenance metadata from privacy policies. It addresses the lack of structured information about real-world usage of personal data, which is a significant gap in current research. By leveraging GDPR terms and concepts, the model aligns with existing legal frameworks, enhancing its applicability and relevance.

The approach is related to other works in the field, such as the UsablePrivacy project, which also uses machine learning and natural language processing to annotate privacy policies. However, it distinguishes itself by focusing on the provenance metadata and its representation using the GDPRov ontology, which extends established ontologies like PROV-O and P-Plan. This novel representation allows for an abstract model of privacy policies, contributing to improved legal accountability and data usage modeling.
