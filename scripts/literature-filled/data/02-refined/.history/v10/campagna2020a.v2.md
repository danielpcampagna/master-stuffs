```md
# Campagna, Daniel Prett and da Silva, Altigran Soares and Braganholo, Vanessa. Achieving GDPR Compliance through Provenance: An Extended Model. 2020.

> [https://dew-uff.github.io/gdpr-data-provenance-model/](https://dew-uff.github.io/gdpr-data-provenance-model/)

## Approach and Motivations

This paper introduces an extended model for achieving GDPR compliance using data provenance. The GDPR has revolutionized data handling practices, increasing individual participation and introducing technical challenges for data controllers. Non-compliance can lead to significant fines, making it crucial to develop robust methods for managing and demonstrating data handling compliance. The authors build upon the GDPR data provenance model proposed by Ujcich et al., aiming to improve it by suggesting eleven new changes. These changes are intended to make the model more transparent and better aligned with the GDPR text.

The proposed model adds new elements classified into three types: plumbing, porcelain, and wallpaper extensions. Plumbing extensions affect how the model operates by appending new elements. Porcelain and wallpaper extensions enrich the model by adding new subclasses representing semantic meanings from the GDPR text and additional detailed information required by the law.

## Approach Contribution For The Compliance Questions

**Question 8**: For each category of personal data, list the period for which the data will be retained.
- The model introduces the `startedAtTime` and `endedAtTime` relations to represent the storage period of personal data, addressing the need to track and inform data retention periods.

**Question 64**: Is there a legal basis for the transfer, e.g., EU Commission adequacy decision; standard contractual clauses. Are these bases documented?
- The `EvaluationOfAdequacy` entity is introduced to document the legal basis for data transfers, aligning with the need to provide information on transfer legality and adequacy decisions.

## Approach Insuficiecies For Fulfill The Compliance Questions

**Question 28**: Are procedures in place to ensure personal data is kept up to date and accurate and where a correction is required, the necessary changes are made without delay?
- The model lacks specific components or mechanisms to ensure data accuracy and timely updates. There is no mention of processes or entities that handle data corrections or updates.

**Question 29**: Are retention policies and procedures in place to ensure data are held for no longer than necessary?
- While the `startedAtTime` and `endedAtTime` relations help track retention periods, the model does not provide comprehensive procedures or policies to enforce adherence to these retention periods.

**Question 51**: Are personal data systematically destroyed, erased, or anonymized when they are no longer legally required to be retained?
- The model does not include mechanisms or entities to ensure systematic destruction, erasure, or anonymization of data. This functionality is essential for compliance but is not covered in the current approach.

**Question 63**: Are all transfers listed, including answers to the previous questions (e.g., the nature of the data, the purpose of the processing, etc.)?
- The model does not comprehensively address the listing of all data transfers. While `EvaluationOfAdequacy` covers the legal basis, it does not account for all details such as the nature of the data or recipient information.

## Key Contributions

- Introduction of eleven new changes to enhance the GDPR data provenance model.
- Classification of extensions into plumbing, porcelain, and wallpaper types.
- Addition of new entities like `SourceExplanation`, `AlgorithmExplanation`, and `EvaluationOfAdequacy` to address specific GDPR requirements.
- Improved transparency and alignment with the GDPR text.

## State-of-the-Art

This approach advances the state-of-the-art by addressing limitations in existing GDPR compliance models through the use of data provenance. The proposed model builds on the work of Ujcich et al. and introduces additional elements to enhance transparency and compliance. The classification of extensions into plumbing, porcelain, and wallpaper types provides a structured way to implement changes in the model.

The approach aligns with related work that uses ontologies and provenance data to model data protection requirements, such as the work by Bartolini et al. and Basin et al. However, it also highlights practical issues not fully addressed, such as the need for data accuracy mechanisms and comprehensive data transfer documentation. Future work should focus on integrating practical measures and multidisciplinary approaches to achieve true compliance.

Overall, the extended model represents a significant step towards robust GDPR compliance but requires further development to address all compliance questions comprehensively.
```