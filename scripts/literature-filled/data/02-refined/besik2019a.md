---
context: True
---


# Besik, Saliha Irem and Freytag, Johann-Christoph. Ontology-Based Privacy Compliance Checking for Clinical Workflows. 2019. LWDA.

## Approach and Motivations

The paper "Ontology-Based Privacy Compliance Checking for Clinical Workflows" by Saliha Irem Besik and Johann-Christoph Freytag introduces an approach to ensure privacy compliance in clinical workflows. The motivation behind this approach is the necessity to safeguard patient data privacy in the healthcare domain, a sector particularly sensitive due to the nature of the data involved. The authors propose using an ontology-based reasoner to verify privacy compliance, leveraging the principles and requirements outlined by the General Data Protection Regulation (GDPR).

The approach is structured around the development of a Privacy-aware Clinical Workflow (PaCW) Ontology. This ontology integrates business process modeling, data privacy regulations, and clinical workflow requirements to create a comprehensive framework for privacy compliance checking. The paper illustrates the applicability of the proposed methodology through a case study involving a newborn screening procedure in Germany, demonstrating how semantic reasoning can be applied to support privacy-awareness in clinical workflows.

The paper is organized into several sections: an introduction that sets the context and importance of data privacy in healthcare, a detailed explanation of the PaCW Ontology, a description of the reasoning approach for privacy compliance, and a running example in the clinical domain. The ontology aims to represent privacy-awareness not only in terms of regulatory compliance but also in adherence to the privacy preferences of patients.

## Approach Contribution For The Compliance Questions

### Question 8
The `PaCW Ontology` can partially contribute to answering Question 8 by ensuring that personal data is retained only for the period necessary for its specified purpose. The ontology includes principles such as `Limited Retention Period` which mandates that data must be erased when it is no longer necessary.

### Question 28
The approach includes a `Consent Check` component that ensures the processing of personal data is lawful and that necessary changes are made when consent is updated, which is related to keeping data up to date and accurate.

### Question 29
Similar to Question 8, the `Limited Retention Period` principle within the `PaCW Ontology` helps ensure that data is not held longer than necessary, aligning with retention policies and procedures.

### Question 51
The `Limited Retention Period` principle also addresses the requirement for systematic destruction, erasure, or anonymization of data when it is no longer legally required, contributing to answering Question 51.

## Approach Insufficiencies For Fulfill The Compliance Questions

### Question 63
The approach does not explicitly cover the listing of all data transfers, including details such as the nature of the data, the purpose of processing, and the countries involved. This lack of detailed tracking and documentation of data transfers means the ontology cannot fully address Question 63.

### Question 64
The `PaCW Ontology` does not provide mechanisms to document the legal basis for data transfers, such as EU Commission adequacy decisions or standard contractual clauses. This limitation makes it insufficient to fully answer Question 64.

## Key Contributions

- **Ontology Development**: Introduction of the Privacy-aware Clinical Workflow (PaCW) Ontology.
    - **Purpose Specification**
    - **Data Minimization**
    - **Consent Check**
    - **Limited Retention Period**
- **Semantic Reasoning**: Application of an ontology-based reasoner to verify privacy compliance.
- **Integration of Domains**: Bridging business process modeling, data privacy, and clinical workflows.
- **Case Study**: Demonstration of the approach through a newborn screening scenario in Germany.
- **Privacy-awareness**: Ensuring compliance with GDPR and patient privacy preferences.

## State-of-the-Art

This approach advances the state-of-the-art by integrating ontology-based reasoning into clinical workflow privacy compliance, offering a structured and regulated method to ensure data privacy in healthcare. The use of ontologies facilitates a common understanding across different domains, enhancing the effectiveness of privacy compliance checks. 

Related works include:
- **Privacy enforcement in data analysis workflows** by Yolanda Gil et al., which focuses on privacy enforcement but lacks the specific integration of clinical workflows and GDPR principles.
- **Ontology-based Approach for Business Process Compliance Checking** by Tuan Pham and Nhan Le Thanh, which deals with business process compliance but not specifically tailored to clinical workflows or GDPR.

Overall, while the proposed model makes significant strides in privacy compliance for clinical workflows, it still requires enhancements to fully address all compliance questions, particularly those involving detailed data transfer documentation and legal bases for data transfers.
