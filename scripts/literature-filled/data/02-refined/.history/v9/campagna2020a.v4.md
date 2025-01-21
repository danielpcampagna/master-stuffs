```md
# Campagna, Daniel Prett and da Silva, Altigran Soares and Braganholo, Vanessa. Achieving GDPR Compliance through Provenance: An Extended Model. 2020.

## Approach and Motivations

The paper "Achieving GDPR Compliance through Provenance: An Extended Model" by Campagna, da Silva, and Braganholo proposes an evolved data provenance model aimed at enhancing compliance with the General Data Protection Regulation (GDPR). The motivation behind this work stems from the increasing complexity of modern data workflows and the stringent requirements set forth by GDPR. The GDPR emphasizes individual participation in data handling processes and introduces technical challenges that, if unmet, can lead to significant fines. 

The authors build upon the existing GDPR data provenance model proposed by Ujcich et al., suggesting eleven new changes to make the model more transparent and closely aligned with the GDPR text. The new model is designed to address the gaps and limitations identified in the previous model, offering more comprehensive tracking and auditing capabilities. Two design patterns are also introduced to guide the implementation of these changes in real-world contexts.

## Approach Contribution For The Compliance Questions

### Question 8
The extended model introduces specific elements to represent the period for which personal data is stored, addressing the need for transparency about data retention durations. The model's use of the startedAtTime and endedAtTime relationships helps capture this information.

### Question 28
By incorporating mechanisms to track data updates and corrections, the model aims to support procedures ensuring data accuracy and timeliness. The provenance data can log changes, making it possible to verify that updates are made without delay.

### Question 29
The model includes retention policies within its provenance records, ensuring data is held only as long as necessary. This feature helps enforce compliance with data retention requirements.

### Question 51
The model supports the systematic destruction, erasure, or anonymization of personal data by logging these actions within the provenance records. This capability ensures that data is appropriately handled when no longer legally required.

### Question 63
The model can track data transfers, including the nature of the data, the purpose of processing, and details about the source and destination countries. This comprehensive logging ensures all transfers are documented.

### Question 64
By capturing the legal basis for data transfers within the provenance records, the model ensures that these bases are documented and can be audited for compliance.

## Approach Insufficiencies For Fulfill The Compliance Questions

### Question 8
While the model captures retention periods, it may not fully automate enforcement of these periods. Additional mechanisms may be needed to ensure data is actually deleted or anonymized at the end of the retention period.

### Question 28
The model can log updates and corrections, but it may require integration with other systems to ensure that changes are made promptly. The provenance model alone cannot enforce timeliness of updates.

### Question 29
Retention policies are logged, but the model does not inherently enforce these policies. External systems or processes must be in place to ensure data is deleted or anonymized according to the logged policies.

### Question 51
Although the model logs destruction or anonymization actions, it does not provide mechanisms for actually performing these tasks. Additional tools are needed to carry out these actions in practice.

### Question 63
The model logs data transfers, but ensuring the legality and compliance of these transfers may require further regulatory checks and validation processes beyond what the provenance model captures.

### Question 64
Documenting the legal basis for transfers is a strength of the model, but ensuring ongoing compliance with these legal bases may require additional oversight and regulatory mechanisms.

## Key Contributions

- Extension of the GDPR data provenance model to better align with GDPR requirements.
- Introduction of eleven new changes to enhance transparency and compliance.
- Development of two design patterns to guide implementation in real-world contexts.
- Enhanced capability to log data retention periods, updates, corrections, and transfers.
- Support for documenting legal bases for data transfers.

## State-of-the-Art

This extended model advances the state-of-the-art in GDPR compliance by addressing specific gaps in existing provenance models. By enhancing the transparency and auditability of data processing activities, the model supports organizations in meeting the stringent requirements of GDPR. 

The approach builds on prior work by Ujcich et al., incorporating feedback and practical considerations to offer a more robust solution. It also addresses critiques related to provenance granularity and the need for inter-controller audits. 

Related work includes provenance capture mechanisms like Hi-Fi, CamFlow, and the Linux Provenance Module, which focus on fine-grained data capture at the kernel level. However, these mechanisms may be too detailed for enforcing data privacy policies, highlighting the need for a more semantically rich model like the one proposed.

Other approaches not based on provenance data, such as those by Shastri et al. and Wang et al., offer alternative solutions for GDPR compliance. These include database management adaptations and new paradigms for storing sensitive data. However, the provenance-based approach provides a unique advantage in its ability to offer a comprehensive and transparent view of data processing activities.
```