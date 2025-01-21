---
context: True
---


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
