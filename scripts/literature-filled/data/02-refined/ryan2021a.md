---
context: True
---


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
