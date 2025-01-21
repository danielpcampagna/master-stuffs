---
context: True
---


# Campagna, Daniel Prett and da Silva, Altigran Soares and Braganholo, Vanessa. Achieving GDPR Compliance through Provenance: An Extended Model. 2020.

> https://dew-uff.github.io/gdpr-data-provenance-model/

## Approach and Motivations

The approval of the General Data Protection Regulation (GDPR) has necessitated a revolution in how data produced in digital media is treated. The GDPR significantly increases individuals' participation in the treatment of their data and introduces stringent technical challenges. Non-compliance can lead to fines of up to 4% of an organization’s annual revenue. Among various approaches to tackle these challenges, the use of data provenance has been promoted to make transparent the increasingly complex workflows of systems. However, existing provenance models are not fully compliant with the GDPR.

This paper contributes to the evolution of the GDPR data provenance model proposed by Ujcich et al. The authors suggest eleven new changes to make the model more apparent and compatible with the GDPR text. They also introduce two design patterns to guide the application of these changes in real contexts. The primary motivation is to enhance the transparency and compliance of data processing activities concerning the GDPR, by improving how data provenance is tracked and documented.

## Approach Contribution For The Compliance Questions

### Question 8
The current model addresses the period for which personal data will be stored through the `startedAtTime` and `endedAtTime` relations. This allows tracking the retention period of data, partially answering this compliance question.

### Question 28
The model suggests using provenance to ensure personal data is kept up to date and accurate by tracking changes and corrections through `AlgorithmExplanation` entities, which describe the logic involved in automated decision-making processes.

### Question 29
The model incorporates retention policies by specifying the storage period of personal data, as seen with the `startedAtTime` and `endedAtTime` relations, which help ensure data is held only as long as necessary.

### Question 63
The model can list transfers of personal data and the related metadata through the `EvaluationOfAdequacy` entity, which documents the safeguards and legal bases for data transfers.

### Question 64
The `EvaluationOfAdequacy` entity also helps document the legal basis for data transfers, ensuring compliance with the GDPR requirements.

## Approach Insuficiecies For Fulfill The Compliance Questions

### Question 8
While the model includes components to track the storage period of data, it does not explicitly enforce the retention policies or check if data is deleted after the specified period.

### Question 28
The model does not provide mechanisms to ensure that personal data is kept current and accurate automatically. It lacks the ability to autonomously detect inaccuracies or enforce updates without delay.

### Question 29
Although the model specifies storage periods, it does not ensure that data is systematically destroyed, erased, or anonymized once it is no longer necessary.

### Question 51
The model lacks explicit components or mechanisms to automatically handle the destruction, erasure, or anonymization of data when it is no longer legally required.

### Question 63
The model does not cover all aspects of data transfers comprehensively, such as the nature of the data, the specific purposes of processing, and details about the countries involved in the transfer.

### Question 64
While the `EvaluationOfAdequacy` entity helps document legal bases for data transfers, the model does not ensure that all necessary legal bases and documentation requirements are consistently met.

## Key Contributions

- **Enhanced GDPR Compliance**: Provides a more comprehensive model for GDPR compliance using data provenance.
- **New Components**: 
  - `SourceExplanation`: Documents the source of personal data.
  - `AlgorithmExplanation`: Describes the logic behind automated decision-making processes.
  - `EvaluationOfAdequacy`: Documents the safeguards and legal bases for data transfers.
- **Design Patterns**: Introduces patterns for applying the model in real-world scenarios.
- **Transparency**: Increases the transparency of data processing activities.
- **Compatibility**: Aligns more closely with GDPR text and requirements.
- **Multidisciplinary Approach**: Considers multidisciplinary and practical issues for future implementation.

## State-of-the-Art

This approach advances the state-of-the-art by addressing gaps in existing provenance models concerning GDPR compliance. It builds on the work of Ujcich et al. and introduces new components to enhance the model’s applicability and compliance. The use of design patterns and detailed documentation of data processing activities contribute to more transparent and accountable data management practices.

Related works include:
- Aldeco Perez and Moreau (2008), who discussed provenance-based auditing of private data use.
- Bartolini, Muthuri, and Santos (2015), who used ontologies to model data protection requirements.
- Basin, Debois, and Hildebrandt (2018), who examined compliance under the GDPR.
- Bates et al. (2015), who explored trustworthy whole-system provenance for the Linux kernel.

This extended model provides a more robust framework for organizations to achieve GDPR compliance, addressing high-level criticism and practical issues identified in prior research.
