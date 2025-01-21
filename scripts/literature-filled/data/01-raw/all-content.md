


# Ryan, Paul and Pandit, Harshvardhan J and Brennan, Rob. Building a Data Processing Activities Catalog: Representing Heterogeneous Compliance-Related Information for GDPR Using DCAT-AP and DPV. 2021.

## Approach and Motivations

This paper presents a novel semantic metadata-based approach to describing and integrating diverse data processing activity descriptions across various organizational units and external processors. The motivation behind this approach is to address GDPR compliance requirements, particularly the creation of a Register of Processing Activities (ROPA). Given the heterogeneity of data sources within organizations, there is a need for a method to collate and harmonize this information efficiently.

The authors extend the well-known DCAT-AP standard by incorporating the Data Privacy Vocabulary (DPV) to express the concepts necessary for a ROPA. This integration allows for the federation of metadata without necessitating full alignment or merging of underlying data sources. A prototype system is developed, showcasing the feasibility of this approach using diverse data processing records and standard SPARQL queries to assist Data Protection Officers (DPOs) in monitoring compliance.

Key components of the proposed model include the use of catalogs as a 'collection of records' which simplifies the updating and maintenance of records, and the utilization of SPARQL for efficient information searching, filtering, and exporting necessary for ROPA creation.

## Approach Contribution For The Compliance Questions

**Question 8**: The approach can document data processing activities in terms of their temporal period, aiding in the list of the retention period for each category of personal data. `DCAT-AP` and `DPV` facilitate this by allowing the metadata to specify retention periods.

**Question 28**: Procedures for ensuring data accuracy and updates can be documented within the catalog. The catalog's inherent design, which includes assigning contact points and limiting scope to organizational units, supports the maintenance of up-to-date and accurate data.

**Question 29**: The use of `DCAT-AP` and `DPV` can support the documentation of retention policies, ensuring data are held no longer than necessary.

**Question 51**: By documenting the lifecycle of data processing activities, the catalog can include metadata about the destruction, erasure, or anonymization of personal data.

## Approach Insuficiecies For Fulfill The Compliance Questions

**Question 63**: The paper does not specify if the catalog can comprehensively list all data transfers, including details such as the nature of the data, processing purposes, and recipient information. It may require additional components to address this comprehensively.

**Question 64**: Similarly, the catalog's current model does not explicitly cover documenting the legal basis for data transfers, such as EU Commission adequacy decisions or standard contractual clauses. Additional metadata or extensions might be needed to capture this information.

## Key Contributions

- **Lightweight Integration**: Provides a low-cost, metadata-level integration point for compliance information.
- **Heterogeneous Data Sources**: Capable of representing processing activities from diverse sources without requiring full alignment.
- **Temporal Documentation**: Supports documenting the temporal period of data processing activities.
- **Organizational Scope**: Limits scope to organizational units and assigns contact points for further information.
- **SPARQL Utilization**: Facilitates efficient searching, filtering, and exporting of information for ROPA creation.
- **Prototype System**: Demonstrates practical feasibility with a prototype based on diverse data processing records.

## State-of-the-Art

This approach advances the state-of-the-art by providing a method to span both graph-based and non-graph data sources using common metadata. It addresses the need for lightweight, federated metadata integration for GDPR compliance, which is crucial as organizational data collection tools become increasingly diverse.

Related works have typically focused on developing detailed compliance graphs or models requiring full alignment of data sources. This approach diverges by offering a solution that integrates heterogeneous data sources at the metadata level, thus reducing the complexity and cost associated with compliance information integration. The use of well-established standards like DCAT-AP and DPV further enhances interoperability and scalability, setting a foundation for future research in automating and refining GDPR compliance processes.

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



# Campagna, Daniel Prett, da Silva, Altigran Soares, and Braganholo, Vanessa. Achieving GDPR Compliance through Provenance: An Extended Model. 2020.

> https://dew-uff.github.io/gdpr-data-provenance-model/

## Approach and Motivations

The paper "Achieving GDPR Compliance through Provenance: An Extended Model" by Campagna, da Silva, and Braganholo introduces an enhanced data provenance model aimed at achieving compliance with the General Data Protection Regulation (GDPR). The motivation for this work arises from the significant changes brought by GDPR in handling data produced in digital media, emphasizing transparency and the involvement of individuals in data treatment processes. However, existing provenance models fall short of being fully compliant with GDPR requirements.

The authors build upon the GDPR data provenance model proposed by Ujcich et al., suggesting eleven new changes to make the model more transparent and compliant with the GDPR text. These changes are categorized into three types: plumbing extensions, porcelain extensions, and wallpaper extensions. Plumbing extensions affect the functionality of the model by appending new elements, while porcelain and wallpaper extensions aim to enrich the model by clarifying semantic meanings and adding further information as detailed in the law. The paper also introduces two design patterns to guide the implementation of these changes in real-world contexts.

## Approach Contribution For The Compliance Questions

### Question 8
The model addresses the need to inform data subjects about the period for which their data will be stored. This is represented using the `startedAtTime` and `endedAtTime` relations in the provenance graph. These elements can be used to answer Question 8 by specifying the duration for which each category of personal data will be retained.

## Approach Insufficiencies For Fulfill The Compliance Questions

### Question 28, 29, 51, 63, 64
The current model does not fully address the remaining compliance questions due to various limitations:
- **Question 28**: The model lacks components to ensure personal data is kept up to date and accurate, and to handle corrections without delay.
- **Question 29**: There are no specific elements in the model to enforce retention policies and procedures that ensure data is held no longer than necessary.
- **Question 51**: The model does not cover systematic destruction, erasing, or anonymization of data when it is no longer legally required.
- **Question 63**: Comprehensive tracking of data transfers, including the nature, purpose, origin, destination, and recipients of the data, is not fully represented.
- **Question 64**: The model does not document the legal basis for data transfers, such as EU Commission adequacy decisions or standard contractual clauses.

## Key Contributions

- Introduction of eleven new changes to the existing GDPR data provenance model.
  - **Plumbing extensions**: Enhance the functionality by adding new elements.
  - **Porcelain extensions**: Clarify semantic meanings of GDPR text components.
  - **Wallpaper extensions**: Append further legal information to the model.
- Presentation of two design patterns to guide real-world implementation.
- Analysis of GDPR text to evolve the provenance model.

## State-of-the-Art

The approach advances the state-of-the-art by addressing some of the gaps in existing GDPR data provenance models. By introducing new elements and design patterns, the model enhances transparency and compliance with GDPR requirements. The work builds on previous models proposed by Ujcich et al., Bartolini et al., and Pandit and Lewis, extending their ideas and addressing some of their limitations.

However, the model still has insufficiencies in fully covering all compliance questions, indicating areas for future research and development. Competing approaches might address these gaps differently, potentially incorporating more comprehensive solutions for data accuracy, retention policies, and legal documentation of data transfers.


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


# Matulevicius, Raimundas and Tom, Jake and Kala, Kaspar and Sing, Eduard. A Method for Managing GDPR Compliance in Business Processes. 2020.

> [Link to the publication](https://link.springer.com/chapter/10.1007/978-3-030-49418-6_24)

## Approach and Motivations

In the paper "A Method for Managing GDPR Compliance in Business Processes," the authors introduce a structured approach to aid organizations in managing their GDPR compliance through the integration of compliance requirements into business processes. This method leverages Business Process Model and Notation (BPMN) to visualize and manage GDPR compliance.

The primary motivation behind this approach is to provide a systematic method to ensure GDPR compliance, addressing the complexity and dynamic nature of regulatory requirements. The authors argue that traditional methods are often insufficient due to their static nature and lack of integration with operational processes.

The core components introduced in this model include a compliance repository (`ComplianceRepository`), a set of compliance requirements (`ComplianceRequirements`), and a mechanism to integrate these requirements into BPMN models (`BPMNIntegration`). This ensures that GDPR principles are embedded directly into the business processes, facilitating continuous compliance monitoring and management.

## Approach Contribution For The Compliance Questions

### Question 63

The method incorporates a `ComplianceRepository` that can list all transfers, including details such as the nature of the data, the purpose of the processing, and transfer specifics such as the originating and receiving country, along with the recipient. This repository can be configured to maintain detailed records of all data transfers, thus contributing to answering Question 63.

### Question 64

The `ComplianceRepository` can also store legal bases for data transfers, such as EU Commission adequacy decisions or standard contractual clauses. This ensures that each transfer's legal justification is documented, which aligns with the requirements of Question 64.

## Approach Insuficiecies For Fulfill The Compliance Questions

### Question 8

The approach does not explicitly address the retention periods for different categories of personal data. While BPMN models and the compliance repository can document processes and compliance requirements, they lack specific components to systematically manage or enforce data retention periods.

### Question 28

The method does not provide a direct mechanism to ensure that personal data is kept up to date and accurate. While process integration helps in embedding compliance requirements, there is no dedicated component for data accuracy and timely updates.

### Question 29

Similar to Question 8, the approach lacks specific components or policies for data retention beyond documentation in the `ComplianceRepository`. There is no systematic procedure to enforce or monitor retention policies.

### Question 51

The destruction, erasure, or anonymization of personal data when no longer needed is not explicitly covered by the proposed method. While BPMN models can document these processes, there are no enforcement mechanisms specified.

## Key Contributions

- Introduction of a systematic method for integrating GDPR compliance into business processes.
- Use of BPMN for visualizing and managing compliance.
- Core components:
  - `ComplianceRepository`: Stores compliance requirements and data transfer details.
  - `ComplianceRequirements`: Defines GDPR compliance needs.
  - `BPMNIntegration`: Mechanism to embed compliance into business process models.
- The approach addresses complex regulatory requirements dynamically.
- Evaluation through case studies demonstrating practical applicability.

## State-of-the-Art

The proposed approach advances the state-of-the-art by integrating GDPR compliance directly into business processes using BPMN. This dynamic and visual method offers a significant improvement over static compliance checks and documentation, providing continuous monitoring and management capabilities.

Related work includes static compliance checklists and separate compliance management systems, which often fall short in integrating with operational processes. This method bridges the gap by embedding compliance into the workflow, enhancing real-time compliance adherence.

The approach competes with other GDPR compliance models like privacy-aware process modeling and compliance-by-design frameworks. However, its unique contribution lies in the seamless integration with BPMN and the emphasis on a compliance repository for tracking and documenting compliance requirements and data transfers.

The approach is particularly relevant for organizations looking to embed GDPR principles into their operational processes, providing a structured and systematic method to manage compliance dynamically.


# Besik, Saliha Irem and Freytag, Johann-Christoph. Ontology-Based Privacy Compliance Checking for Clinical Workflows. 2019.

## Approach and Motivations

The publication "Ontology-Based Privacy Compliance Checking for Clinical Workflows" by Saliha Irem Besik and Johann-Christoph Freytag introduces an innovative approach to ensure privacy compliance within clinical workflows through the use of ontology-based models. The authors aim to address the stringent requirements of the General Data Protection Regulation (GDPR) by leveraging ontological representations to model and track data processing activities. The motivation behind this approach is to provide a systematic and automated way to verify compliance, reducing the burden on data controllers and minimizing human errors.

The paper details the structure of the proposed model, which includes components to represent clinical workflows, data categories, processing activities, and compliance rules. By formalizing these elements within an ontology, the authors enable automated reasoning engines to check for compliance violations dynamically. This method is particularly relevant for clinical environments where complex data processing activities are prevalent, and adherence to privacy regulations is critical.

The components introduced by the publication include ontologies for data categories, processing activities, and compliance rules, each of which plays a crucial role in modeling the intricacies of clinical workflows. The authors also demonstrate how these ontologies can be integrated into existing clinical systems to provide real-time compliance checking.

## Approach Contribution For The Compliance Questions

### Question 8

The approach can partially address this question through its ontology for data categories, which can include attributes for data retention periods. By modeling each category of personal data and associating it with predefined retention periods, the system can track and verify if the data is retained for no longer than necessary.

### Question 28

The ontology-based model includes components for processing activities, which can be extended to incorporate procedures for ensuring data accuracy and up-to-dateness. By modeling these activities, the system can verify if procedures are in place and if necessary corrections are made without delay.

### Question 29

The ontology includes compliance rules that can be tailored to ensure data retention policies are in place. By defining these rules within the ontology, the system can automatically check if data is held for no longer than the necessary period and flag any violations.

### Question 51

The compliance rules within the ontology can be extended to include procedures for data destruction, erasure, or anonymization. By modeling these rules, the system can verify if personal data is systematically handled when it is no longer legally required.

### Question 63

The approach can model the nature of the data, purpose of processing, and data transfers within its ontology. By doing so, it can list all transfers and provide detailed information about the data flow, including exporting and receiving countries and recipients.

### Question 64

The ontology can include components to represent the legal basis for data transfers, such as EU Commission adequacy decisions or standard contractual clauses. By documenting these bases within the model, the system can verify if the legal requirements for data transfers are met.

## Approach Insuficiecies For Fulfill The Compliance Questions

### Question 8

While the ontology can model retention periods, it may lack the dynamic capability to enforce these periods automatically without additional integration with data management systems.

### Question 28

The model can represent procedures for data accuracy, but it may not have the mechanisms to enforce real-time data correction without integration with operational data systems.

### Question 29

The ontology can define retention policies, but ensuring these policies are enforced in practice requires integration with data storage and management systems, which may not be covered by the model alone.

### Question 51

The model can specify procedures for data destruction or anonymization, but it may not have the execution capability to perform these actions without additional system integration.

### Question 64

Documenting the legal basis for data transfers within the ontology is feasible, but the model may not be able to verify the legal compliance autonomously without access to external legal databases or documents.

## Key Contributions

- **Ontology-Based Model**: Utilizing ontologies to represent data categories, processing activities, and compliance rules.
  - **Data Categories Ontology**: Models various categories of personal data and associated attributes.
  - **Processing Activities Ontology**: Represents different processing activities and their compliance requirements.
  - **Compliance Rules Ontology**: Defines rules for verifying GDPR compliance dynamically.
- **Automated Compliance Checking**: Enabling automated reasoning to verify compliance with GDPR requirements.
- **Clinical Workflow Integration**: Tailoring the model for clinical environments with complex data processing activities.
- **Reduction of Human Error**: Minimizing manual compliance checks through automation.
- **Flexibility and Extensibility**: Allowing the model to be extended and adapted to different compliance requirements and environments.

## State-of-the-Art

The "Ontology-Based Privacy Compliance Checking for Clinical Workflows" approach advances the state-of-the-art by integrating ontological models with compliance verification processes. Traditional compliance methods often rely on manual checks and static documentation, which are prone to errors and inefficiencies. By leveraging ontologies, this approach allows for dynamic, automated compliance checking, significantly reducing the burden on data controllers.

This work relates to other research efforts in privacy compliance and ontology-based systems, such as those focusing on semantic web technologies and data protection frameworks. It competes with approaches that use rule-based systems and machine learning models for compliance verification but stands out due to its focus on clinical workflows and its comprehensive ontological representation.

Overall, the approach provides a robust framework for ensuring GDPR compliance in clinical settings, contributing to the broader field of privacy-preserving data management and compliance automation.


# Tom, Jake and Sing, Eduard and Matulevicius, Raimundas. Conceptual representation of the GDPR: model and application directions. 2018.

> [Link to publication](https://example.com/publication) 

## Approach and Motivations

The paper "Conceptual representation of the GDPR: model and application directions" by Tom, Jake, Sing, and Matulevicius proposes a model to systematically represent the General Data Protection Regulation (GDPR) guidelines. The primary motivation behind this approach is to provide a structured way to manage and track compliance with GDPR requirements. This is achieved by developing a conceptual model that encapsulates the key elements of GDPR and demonstrates how organizations can apply these in their data processing activities.

The structure of the paper outlines the development of the GDPRov model, which provides a formal representation of GDPR-related concepts. The model focuses on the relationships between data controllers, data processors, data subjects, and the personal data being processed. The model includes components such as `DataCategory`, `DataSubject`, `Purpose`, `Consent`, and `ProcessingActivity`.

The motivation for this approach stems from the need for organizations to have a comprehensive tool to ensure GDPR compliance, reduce the risk of non-compliance, and streamline data protection processes. By representing the GDPR requirements conceptually, the authors aim to bridge the gap between legal regulations and practical implementation.

## Approach Contribution For The Compliance Questions

### Question 28

The GDPRov model includes components such as `DataCategory`, `DataSubject`, and `ProcessingActivity` which can be leveraged to ensure personal data is kept up to date and accurate. For example, the `ProcessingActivity` component can be used to track updates and corrections to personal data, ensuring that any necessary changes are made without delay.

### Question 63

The model's `DataCategory` and `ProcessingActivity` components can help list all transfers, including the nature of the data and the purpose of the processing. Additionally, the `Transfer` component can capture information about the source and destination countries and the recipient of the data transfer, ensuring detailed documentation of all data transfers.

### Question 64

The `LegalBasis` component in the GDPRov model can be used to document the legal basis for data transfers. This component can capture information such as EU Commission adequacy decisions or standard contractual clauses, ensuring that all legal bases for data transfers are well-documented and accessible.

## Approach Insufficiencies For Fulfill The Compliance Questions

### Question 8

The GDPRov model does not explicitly include a component to specify the retention period for each category of personal data. While the `ProcessingActivity` component can track data processing activities, it lacks a direct mechanism to define and enforce data retention policies.

### Question 29

Similarly, the model does not provide a specific component for retention policies and procedures. Although `ProcessingActivity` tracks data usage, it does not inherently include the necessary features to ensure data retention aligns with the purposes for which the data was collected.

### Question 51

The model does not have a dedicated component to systematically manage the destruction, erasure, or anonymization of personal data when it is no longer legally required. The absence of such a component means the model does not fully address the systematic disposal of data.

## Key Contributions

- **Development of GDPRov Model**:
  - `DataCategory`
  - `DataSubject`
  - `Purpose`
  - `Consent`
  - `ProcessingActivity`
  - `Transfer`
  - `LegalBasis`
- **Structured Representation of GDPR**: Provides a formal framework for representing GDPR concepts and relationships.
- **Facilitates GDPR Compliance**: Assists organizations in tracking and managing GDPR compliance efficiently.
- **Application Directions**: Offers practical guidelines on how the model can be applied in real-world scenarios.

## State-of-the-Art

The approach presented in the paper advances the state-of-the-art by offering a structured and formal representation of GDPR requirements. This model bridges the gap between legal regulations and practical implementation, providing a comprehensive tool for organizations to manage GDPR compliance.

Compared to previous models, GDPRov introduces a more detailed and interconnected representation of GDPR components. It allows for more effective tracking of data processing activities, consent management, and legal basis documentation. However, it still lacks specific components for data retention policies and systematic data disposal, which are critical for full compliance.

Related works in this domain include various data protection frameworks and models, but GDPRov stands out due to its detailed representation of GDPR-specific requirements and its practical application directions. Future work could focus on extending the model to cover additional compliance questions and integrating it with existing data governance tools.



# Bartolini, Cesare and Muthuri, Robert and Santos, Cristiana. Using ontologies to model data protection requirements in workflows. 2015.

## Approach and Motivations

In this work, the authors present an ontology to model data protection requirements and an approach for integrating it into workflows to express GDPR requirements within business processes. The ontology aims to assist data controllers in achieving compliance with GDPR regulations. The paper illustrates the design and development of the ontology following an initial stage described in previous work. As a proof of concept, an approach is introduced that uses the ontology to enrich workflow models, such as business processes, with annotations that express data protection requirements.

The ontology was modeled by a legal expert, selectively identifying provisions that contain duties for the data controller and rights for data subjects, and building these into the ontology. Despite its coarse granularity, the ontology serves as a foundational structure necessary for long-term goals, such as verifying compliance with GDPR. The approach also aims to benefit various stakeholders, including data controllers, auditors, and Data Protection Authorities (DPAs), by providing a structured means of assessing compliance and detecting potential violations.

The ontology is designed to be adaptable to changes in the legal text, with an improved version under development to cover more provisions and provide a broader perspective on GDPR. The integration with security standards, like ISO 27001:2013, is also explored to facilitate a smoother transition to the new legislation.

## Approach Contribution For The Compliance Questions

### Question 28: Procedures to Ensure Data is Up-to-date and Accurate
The current model can contribute partially to Question 28 through its structured ontology, which helps data controllers understand their obligations. The ontology can be queried by data controllers to clarify their functions and ensure data accuracy and timely updates by referencing specific duties and rights.

## Approach Insufficiencies For Fulfill The Compliance Questions

### Question 8: Data Retention Periods
The current approach does not specifically address the categorization of personal data and the retention periods required for compliance. The ontology's granularity is too coarse, and it lacks specific provisions to list data retention periods explicitly.

### Question 28: Procedures to Ensure Data is Up-to-date and Accurate
While the ontology helps in understanding obligations, it does not provide a direct mechanism to ensure that personal data is kept up to date and accurately corrected without delay. It lacks procedural components that could automate or enforce these requirements.

### Question 29: Retention Policies and Procedures
The ontology does not include specific retention policies or procedures to ensure data is held no longer than necessary. It focuses more on identifying duties and rights rather than implementing retention strategies.

### Question 51: Data Destruction, Erasure, or Anonymisation
The model does not cover the systematic destruction, erasure, or anonymisation of personal data when no longer required. It lacks the components to manage data lifecycle and enforce such actions.

### Question 63: Listing All Data Transfers
The ontology does not specifically list all data transfers, including the nature of the data, processing purposes, and details of the transfers. It also does not document the legal basis for these transfers.

### Question 64: Legal Basis for Data Transfers
Although the model helps identify compliance with GDPR, it does not explicitly document the legal basis for data transfers, such as EU Commission adequacy decisions or standard contractual clauses.

## Key Contributions

- Development of an ontology to model data protection requirements.
- Integration of the ontology into business process workflows.
- Aids data controllers, auditors, and DPAs in understanding and assessing GDPR compliance.
- Identified duties for data controllers and rights for data subjects.
- Initial coarse granularity of the ontology, with plans for more detailed future versions.
- Exploration of the relationship between GDPR and security standards like ISO 27001:2013.

## State-of-the-Art

This approach advances the state-of-the-art by providing a structured ontology to model data protection requirements, which can be integrated into business process workflows. It addresses a critical need for compliance with the evolving GDPR regulations, offering a foundational structure for further refinement and broader coverage. The integration with security standards is also a novel aspect that facilitates a smoother transition to new legislation.

The related work includes other domain legal ontologies within data protection and privacy, but this approach stands out by focusing on GDPR compliance and integrating the ontology into business processes. Future improvements aim at broader coverage and more detailed granularity, enhancing its utility for real-world scenarios.


# Bonatti, Piero A and Kirrane, Sabrina and Petrova, Iliana M and Sauro, Luigi. Machine understandable policies and GDPR compliance checking. 2020.

## Approach and Motivations

The paper titled "Machine understandable policies and GDPR compliance checking" by Bonatti, Kirrane, Petrova, and Sauro introduces an approach aimed at automating the compliance checking process for GDPR. The motivation behind this approach stems from the need for technical and organizational measures to support the implementation of the GDPR. The SPECIAL H2020 project aims to address this by providing tools that data controllers and processors can use to ensure their data processing activities comply with GDPR regulations.

The approach leverages a policy language developed in collaboration with legal professionals to express consent, business policies, and regulatory obligations. This language is designed to be machine-understandable, enabling automated compliance checking. The paper also discusses two distinct methods for automated compliance checking: one to verify that data processing aligns with the consent provided by data subjects, and another to ensure that business processes adhere to GDPR's regulatory obligations.

The structure of the paper includes an analysis of the GDPR text, the introduction of the SPECIAL policy language, a discussion on encoding business policies and regulatory obligations, an overview of the compliance checking algorithm, and the results of an initial performance evaluation.

## Approach Contribution For The Compliance Questions

### Question 8
The approach can potentially contribute to answering this question through its `SPECIAL policy language`, which allows the encoding of the `envisaged time limits for erasure of the different categories of data (P5)` as specified by Article 30. This component can be used to define the retention periods for different data categories, aiding in compliance with this requirement.

### Question 28
The approach could relate to this question by using the `SPECIAL policy language` to encode policies that ensure data accuracy and prompt corrections. However, the paper does not explicitly mention mechanisms for keeping data up-to-date or procedures for making necessary corrections without delay.

### Question 29
The `SPECIAL policy language` can encode retention policies and procedures, aiding in ensuring data is held no longer than necessary. Article 30's requirement to describe the envisaged time limits for data erasure (P5) can be used in this context.

### Question 51
The paper does not explicitly address the systematic destruction, erasure, or anonymization of personal data when it is no longer legally required. Therefore, the approach may not fully answer this question.

### Question 63
The approach can partially address this question by using the `SPECIAL policy language` to encode the categories of recipients and transfers of personal data to third countries or international organizations (P4), as required by Article 30.

### Question 64
The paper does not explicitly discuss the legal basis for data transfers or the documentation of such bases. Thus, the approach may not fully cover this question.

## Approach Insuficiencies For Fulfill The Compliance Questions

### Question 28
The approach lacks specific mechanisms or components for ensuring personal data is kept up-to-date and accurate, and for making necessary corrections without delay.

### Question 51
The approach does not provide explicit methods for systematically destroying, erasing, or anonymizing personal data when no longer required, which is necessary to answer this question completely.

### Question 64
The approach does not address the documentation of legal bases for data transfers, nor does it provide components for ensuring compliance with EU Commission adequacy decisions or standard contractual clauses.

## Key Contributions

- **Policy Language**:
  - Developed in collaboration with legal professionals.
  - Encodes consent, business policies, and regulatory obligations.
- **Automated Compliance Checking**:
  - Two methods: one for data processing compliance with consent and another for business processes compliance with GDPR obligations.
- **GDPR Analysis**:
  - Detailed analysis of GDPR requirements and their machine-understandable representation.
- **Compliance Checking Algorithm**:
  - High-level overview and initial performance evaluation.

## State-of-the-Art

The approach contributes to the state-of-the-art by introducing a machine-understandable policy language and automated compliance checking methods. This advances the field of legal informatics by providing technical means to demonstrate GDPR compliance, which is crucial for companies processing personal data.

Related work includes existing GDPR compliance tools that use predefined questionnaires to assess compliance. However, these tools lack support for automated compliance checking, which the SPECIAL project aims to address. The approach builds upon a rich history of policy language research from the Semantic Web community, demonstrating how these technologies can be applied to GDPR compliance.

This work represents a significant step forward in automating the compliance process, reducing the need for manual checks and increasing the efficiency and accuracy of compliance assessments.



# Fatema, Kaniz and Hadziselimovic, Ensar and Pandit, Harshvardhan J and Debruyne, Christophe and Lewis, Dave and O'Sullivan, Declan. Compliance through Informed Consent: Semantic Based Consent Permission and Data Management Model. 2017. ISWC

## Approach and Motivations

The approach presented in this publication proposes a semantic model for consent that leverages existing models of provenance, processes, permission, and obligations to ensure compliance with GDPR requirements. The motivations behind this approach include the need to satisfy GDPR's requirements for specificity and unambiguity in user consent and to enable organizations to efficiently demonstrate their compliance. The model aims to make consent explicit, establish a common understanding, and enable the re-use of consent.

The paper introduces a Consent and Data Management Model (CDMM) that uses an open vocabulary for expressing consent. This model incorporates changes in the context of the relationship between data controllers and data subjects into the data processing activities. By doing so, it seeks to improve the integration of data management systems and to help controllers demonstrate compliance with GDPR.

The reference architecture proposed in the paper aims to automate the reasoning over the contextual integrity of the relationship between user consent and compliance by service providers. The implementation of the ontology in Protégé and the use of XACML for machine-enforceable consent permissions are key components of this approach.

## Approach Contribution For The Compliance Questions

**Question 8**: 
The `Consent and Data Management Model (CDMM)` incorporates the lifecycle of consent and data. This includes the period for which the data will be retained as part of the consent information. The `Provenance` component can be used to track the retention period associated with each category of personal data, ensuring it is retained no longer than necessary.

**Question 28**:
The model's focus on the lifecycle of consent and data can help ensure that personal data is kept up to date and accurate. The `Processes` and `Obligations` components can be utilized to define procedures for data correction and updates, ensuring that necessary changes are made without delay.

**Question 29**:
Retention policies can be managed using the `Permission` and `Provenance` components of the CDMM. These components ensure that data is held only for as long as necessary and provide a clear audit trail for data retention decisions.

**Question 51**:
The `Obligations` component can define rules for the systematic destruction, erasure, or anonymization of personal data. The `Provenance` component tracks compliance with these rules, ensuring data is handled appropriately when no longer legally required.

**Question 63**:
The `Provenance` component can document all data transfers, including the nature of the data, purpose of processing, and details of the transfer. This ensures comprehensive tracking of data flows and compliance with GDPR requirements.

**Question 64**:
The `Permission` component can record the legal basis for data transfers, such as EU Commission adequacy decisions or standard contractual clauses. This information can be documented and managed within the CDMM to demonstrate compliance.

## Approach Insuficiecies For Fulfill The Compliance Questions

**Question 8**:
The current model might not fully cover the granularity required for all possible retention scenarios across different categories of personal data. It may need further refinement to address specific retention periods comprehensively.

**Question 28**:
While the model addresses data corrections and updates, it might lack the detailed mechanisms to automatically ensure all data remains up to date across multiple databases and systems, especially in complex environments.

**Question 29**:
The model's approach to retention policies may need more detailed guidelines and enforcement mechanisms to ensure that data is not retained longer than necessary in all possible scenarios.

**Question 51**:
The systematic destruction, erasure, or anonymization processes might require more specific implementation details to ensure they are carried out consistently across different systems and platforms.

**Question 63**:
Although the model tracks data transfers, it might not cover all the complexities involved in international data transfers and the specific legal requirements for each transfer case.

**Question 64**:
While the model records the legal basis for transfers, it might require additional components to ensure that all legal bases are documented and managed correctly across different jurisdictions and regulatory environments.

## Key Contributions

- **Open Vocabulary for Expressing Consent**:
  - Leveraging existing open ontology models.
  - Improving integration across different information systems.
- **Machine Readable and Enforceable Consent**:
  - Mapping consent into XACML for policy enforcement.
- **Consent and Data Management Model (CDMM)**:
  - Incorporating consent and data lifecycle.
  - Addressing changes in context and ensuring compliance.
- **Implementation in Protégé**:
  - Preliminary ontology version implemented.
  - Use of XACML for consent permission enforcement.

## State-of-the-Art

This approach advances the state-of-the-art by providing a semantic model for consent that addresses GDPR requirements for specificity and unambiguity. By integrating existing models of provenance, processes, permission, and obligations, it creates a comprehensive framework for managing consent and data processing activities. 

The use of XACML for machine-enforceable consent permissions provides a robust mechanism for ensuring compliance. The proposed CDMM offers a structured approach to handling the lifecycle of consent and data, improving the ability of organizations to demonstrate their compliance with GDPR.

Related works include ontology-based tools for reasoning about consent permission and integrating patient consent in e-health access control. However, this approach distinguishes itself by focusing on the comprehensive management of consent and data lifecycle, incorporating changes in context, and providing automated reasoning over contextual integrity.



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


# Kirrane, Sabrina and Fernández, Javier D and Dullaert, Wouter and Milosevic, Uros and Polleres, Axel and Bonatti, Piero A and Wenning, Rigo and Drozd, Olha and Raschke, Philip. A scalable consent, transparency and compliance architecture. 2018. ESWC.

> https://svn.aksw.org/papers/2018/ESWC_Share_Like_Cook_Cookie/public.pdf

## Approach and Motivations

The paper presents a scalable architecture designed to facilitate consent management, transparency, and compliance with the General Data Protection Regulation (GDPR). The authors propose a framework that integrates various technologies and methodologies to ensure that personal data handling practices align with GDPR requirements. The system leverages Semantic Web technologies and Linked Data principles to provide a machine-readable, interoperable, and extensible solution for data governance.

The key motivation behind this approach is the increasing complexity of data processing activities and the stringent requirements imposed by GDPR. Organizations need robust mechanisms to manage user consent, ensure transparency in data processing, and maintain compliance with regulatory standards. The proposed architecture aims to address these challenges by providing a scalable and flexible solution that can adapt to diverse data processing environments.

The paper outlines several components of the architecture, including a consent management module, a transparency framework, and a compliance monitoring system. Each component is designed to address specific aspects of GDPR compliance, from obtaining and managing user consent to ensuring that data processing activities are transparent and accountable. The integration of these components provides a comprehensive solution for GDPR compliance.

## Approach Contribution For The Compliance Questions

### Question 8: Data Retention Periods

The architecture includes a `consent management module` which can be extended to track the retention periods for different categories of personal data. By leveraging Linked Data principles, the system can represent and query data retention policies, ensuring that data is retained no longer than necessary.

### Question 28: Data Accuracy and Updates

The `transparency framework` within the architecture can be employed to ensure that personal data is kept up to date and accurate. The framework can facilitate the logging of data updates and corrections, ensuring that any necessary changes are made without delay.

### Question 29: Retention Policies and Procedures

The architecture’s `compliance monitoring system` can be used to implement and enforce data retention policies. By monitoring data processing activities, the system can ensure that data is held only for as long as necessary for the purposes for which it was collected.

### Question 51: Data Destruction, Erasure, and Anonymisation

The `compliance monitoring system` can also support the systematic destruction, erasure, or anonymisation of personal data when it is no longer legally required to be retained. The system can log and audit these activities to ensure compliance with GDPR requirements.

### Question 63: Data Transfers

The architecture provides mechanisms to log and track data transfers, including the nature of the data, the purpose of the processing, and the countries involved. This can be managed through the `transparency framework` and `consent management module`.

### Question 64: Legal Basis for Data Transfers

The `consent management module` can document the legal basis for data transfers, such as EU Commission adequacy decisions or standard contractual clauses. This information can be queried and audited to ensure that all data transfers comply with legal requirements.

## Approach Insufficiencies For Fulfill The Compliance Questions

### Question 8: Data Retention Periods

While the architecture can track data retention periods, it may lack detailed mechanisms to automatically enforce the deletion of data once the retention period has expired, requiring additional tools or manual intervention.

### Question 28: Data Accuracy and Updates

The framework ensures data accuracy and updates but might not fully automate the correction process, potentially requiring user or administrator intervention to make necessary changes.

### Question 29: Retention Policies and Procedures

The architecture can monitor and enforce retention policies, but it may not provide a complete solution for all types of data and processing activities, necessitating supplementary systems or protocols.

### Question 51: Data Destruction, Erasure, and Anonymisation

While the architecture supports data destruction and anonymisation, it may not offer comprehensive tools for all data types and scenarios, potentially requiring additional software or manual processes.

### Question 63: Data Transfers

The system can log data transfers, but it might not fully capture all details or automate compliance checks for every transfer, requiring supplementary logging and auditing tools.

### Question 64: Legal Basis for Data Transfers

The architecture documents the legal basis for transfers but may not fully automate the verification process, necessitating manual reviews or complementary systems.

## Key Contributions

- **Scalable Architecture**: Designed to handle large-scale data processing activities.
- **Consent Management Module**: Manages user consent and tracks data processing activities.
- **Transparency Framework**: Ensures transparency in data processing and facilitates data updates.
- **Compliance Monitoring System**: Monitors and enforces compliance with GDPR requirements.

### Components Introduced

- **Consent Management Module**
- **Transparency Framework**
- **Compliance Monitoring System**

### Background Concepts

- **Semantic Web Technologies**
- **Linked Data Principles**
- **GDPR Compliance**

### Evaluation

- The architecture is evaluated through case studies and prototype implementations, demonstrating its scalability and effectiveness in managing consent, transparency, and compliance.

## State-of-the-Art

The proposed architecture advances the state-of-the-art by integrating Semantic Web technologies and Linked Data principles into a comprehensive GDPR compliance framework. This approach provides a machine-readable and interoperable solution, addressing the complexities of modern data processing activities.

Compared to existing solutions, this architecture offers a more scalable and flexible approach, capable of adapting to diverse data environments. The use of standardized technologies ensures interoperability and extensibility, making it easier for organizations to implement and maintain compliance.

The architecture's ability to manage consent, ensure transparency, and monitor compliance sets it apart from traditional data governance solutions. By providing a holistic and integrated approach, it addresses the key challenges posed by GDPR and offers a robust framework for data protection.

Related works include various GDPR compliance tools and frameworks, but this architecture distinguishes itself through its use of Semantic Web technologies and its focus on scalability and flexibility. The integration of consent management, transparency, and compliance monitoring into a single architecture provides a unique and effective solution for GDPR compliance.
