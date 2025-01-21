---
context: True
---


# Ujcich, Benjamin E and Bates, Adam and Sanders, William H. A provenance model for the European union general data protection regulation. 2018.

## Approach and Motivations

The European Union (EU) General Data Protection Regulation (GDPR) has significantly expanded regulations regarding the storage and processing of personal data. This regulation mandates that organizations demonstrate compliance with data privacy laws, which includes showing how data were generated and used. The authors, Benjamin E. Ujcich, Adam Bates, and William H. Sanders, propose a data provenance model specifically tailored to the GDPR. This model aims to help organizations track the processing of personal data and ensure compliance with the regulation.

The proposed model captures data provenance, which involves the history and lifecycle of data, including its origins, transformations, and usage. The model includes high-level classes such as agents, activities, and entities, represented by house symbols, rectangles, and ellipses, respectively. Additionally, it incorporates relations and other properties essential for understanding data processing workflows. The authors emphasize the importance of temporal reasoning in determining the lawfulness of data processing, particularly concerning data consent validity over time.

## Approach Contribution For The Compliance Questions

### Question 8
The model includes temporal notions and timestamps for data activities, which can partially address the requirement to list the data retention period. By tracking when data were collected and processed, the model can help ensure that data are retained only as long as necessary.

### Question 28
The model's design patterns for data collection and consent can help track when corrections to personal data are made. By capturing timestamps and the provenance of data changes, the model supports the requirement to keep data up to date and accurate.

### Question 29
The model's emphasis on temporal reasoning and data retention periods can contribute to establishing retention policies. By tracking the lifecycle of data, the model helps ensure data are held no longer than necessary.

### Question 51
The model's provenance tracking can help document when data are destroyed, erased, or anonymized. By maintaining a record of these actions, the model supports the systematic handling of data no longer legally required.

### Question 63
The model includes components for tracking data transfers, including the origins and destinations of data. This can help list all transfers and answer questions about the nature and purpose of data processing.

### Question 64
The model does not explicitly address the legal basis for data transfers. While it can track data origins and destinations, it lacks components to document the legal justifications for these transfers.

## Approach Insuficiecies For Fulfill The Compliance Questions

### Question 8
While the model includes temporal components, it does not explicitly provide a mechanism for specifying data retention periods for different categories of personal data. Additional components may be needed to define and enforce retention policies.

### Question 28
The model can track updates to personal data, but it does not provide specific mechanisms for ensuring data accuracy and making necessary corrections without delay. This may require integration with other data quality management systems.

### Question 29
Although the model tracks data lifecycles, it does not include explicit retention policies or procedures. Organizations may need to develop additional policies and integrate them with the model to ensure compliance.

### Question 51
The model supports documenting data destruction, but it does not include specific procedures for systematically handling data when it is no longer required. Additional processes and controls may be needed to ensure compliance.

### Question 64
The model lacks components to document the legal basis for data transfers. This information is crucial for GDPR compliance but is not covered by the current model.

## Key Contributions

- **Data Provenance Model:** A model to track the history and lifecycle of personal data.
- **Temporal Reasoning:** Incorporation of temporal components to determine the lawfulness of data processing.
- **Design Patterns:** Patterns for modeling common events such as data collection, consent, and updates.
- **Compliance Support:** Helps organizations demonstrate GDPR compliance through data provenance tracking.
    - **Components:**
        - Agents (house symbols)
        - Activities (rectangles)
        - Entities (ellipses)
        - Relations (arrows)
        - Properties (notes)
- **Evaluation:** Analysis of GDPR text to identify compliance challenges and how data provenance can address them.

## State-of-the-Art

This approach advances the state-of-the-art by providing a structured model for tracking data provenance in the context of GDPR compliance. It builds on previous work by Pandit and Lewis and Bartolini et al., who developed GDPR ontologies. By incorporating temporal reasoning and design patterns, the model offers a practical tool for organizations to manage and document their data processing activities.

The model's emphasis on temporal aspects and compliance verification distinguishes it from prior research, which may not have focused as explicitly on these areas. Additionally, the model's alignment with the GDPR's requirements provides a robust framework for organizations seeking to ensure compliance and avoid significant penalties for non-compliance.

Related work includes the GDPR ontologies by Pandit and Lewis, and Bartolini et al., which structure the regulation's concepts. The current model extends these efforts by providing a practical tool for tracking data processing activities and ensuring compliance with the regulation's temporal and documentation requirements.

