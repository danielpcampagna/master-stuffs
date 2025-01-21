---
context: True
---


# Ryan, Paul and Pandit, Harshvardhan J and Brennan, Rob. Building a Data Processing Activities Catalog: Representing Heterogeneous Compliance-Related Information for GDPR Using DCAT-AP and DPV. 2021.

## Approach and Motivations

This paper presents a novel approach to creating a semantic metadata-based catalog for managing data processing activities to comply with GDPR requirements. The motivation behind this approach stems from the need to consolidate diverse data processing activity descriptions from various organizational sources. As organizations already utilize a myriad of tools for documenting data processing activities, a standardized method to aggregate and homogenize these records is essential for efficient compliance monitoring.

The approach extends the well-known DCAT-AP standard and leverages the Data Privacy Vocabulary (DPV) to encapsulate the necessary concepts for creating a Register of Processing Activities (ROPA). This method supports the integration of metadata from heterogeneous sources without requiring full alignment or merging of the underlying data sources, thus providing a lightweight and cost-effective solution for compliance information integration.

A prototype system is demonstrated, utilizing diverse data processing records and a standard set of SPARQL queries to aid a Data Protection Officer (DPO) in preparing a ROPA. This prototype highlights the feasibility of the system and its effectiveness in simplifying the process of GDPR compliance documentation.

## Approach Contribution For The Compliance Questions

### Question 8
The approach supports documenting data processing activities in terms of their temporal period, which is directly related to the retention period for each category of personal data. By using the `temporal period` concept within the catalog, organizations can specify how long data will be retained, ensuring compliance with GDPR's requirement to retain data only as long as necessary.

### Question 28
The catalog can assign contact points within the organization for further information, which can be used to ensure that personal data is kept up to date and accurate. However, specific procedures for updating data must be implemented by the organization independently.

### Question 29
Retention policies and procedures can be documented within the catalog using the `temporal period` and other related metadata. This ensures data is held only as long as necessary, aligning with GDPR requirements.

### Question 51
The catalog does not provide a direct mechanism for destroying, erasing, or anonymizing data. The approach focuses on documenting and cataloging data processing activities rather than enforcing data destruction policies.

### Question 63
The approach can list all transfers by documenting the nature of the data, the purpose of processing, and other related metadata. This information can be queried and reported using SPARQL.

### Question 64
The catalog can document the legal basis for data transfers using DPV concepts. However, specific documentation and verification of legal bases must be managed by the organization.

## Approach Insuficiecies For Fulfill The Compliance Questions

### Question 51
This approach does not provide tools for the systematic destruction, erasure, or anonymization of data. It focuses only on documenting and cataloging data processing activities. Additional tools and processes are needed to manage the actual data destruction.

### Question 64
While the catalog can document the legal basis for data transfers, it does not verify or enforce these legal bases. Organizations need to implement their own measures to ensure the legal bases are valid and documented correctly.

## Key Contributions

- **Lightweight Metadata Integration**: Provides a cost-effective method for integrating compliance information.
- **Standardization**: Utilizes DCAT-AP and DPV standards for interoperability.
- **Prototyping**: Demonstrates feasibility with a prototype system for preparing a ROPA.
- **SPARQL Queries**: Enables efficient querying, filtering, and exporting of compliance information.
- **Metadata-Level Integration**: Allows for the aggregation of heterogeneous data sources without full data alignment.
- **Organizational Units**: Supports documenting data processing activities by organizational units and assigning contact points.

## State-of-the-Art

This approach advances the state-of-the-art by providing a standardized, lightweight method for documenting and integrating diverse data processing activities for GDPR compliance. Unlike previous methods focusing solely on detailed compliance graphs, this approach allows for metadata-level integration, making it easier and more cost-effective for organizations to manage their compliance documentation.

Related work includes developing compliance graphs and enterprise architecture models for creating ROPA, but they often require significant alignment of underlying data sources. This approach's use of DCAT-AP and DPV standards provides a more flexible and scalable solution.

The approach's ability to span both graph-based and non-graph data sources, and its reliance on common metadata, sets it apart from other solutions. It also addresses the practical need for organizations to continue using their existing diverse data collection tools while still achieving GDPR compliance.

Overall, this method represents a significant step forward in simplifying and standardizing the process of GDPR compliance documentation, making it accessible to a wider range of organizations.
