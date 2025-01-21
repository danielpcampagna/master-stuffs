```md
# Campagna, Daniel Prett and da Silva, Altigran Soares and Braganholo, Vanessa. Achieving GDPR Compliance through Provenance: An Extended Model. 2020.

> https://dew-uff.github.io/gdpr-data-provenance-model/

## Approach and Motivations

The paper proposes an extended model to enhance the GDPRov (GDPR data provenance model) initially introduced by Ujcich et al. The motivation stems from the increasing complexity of data workflows and the need for transparency and compliance with GDPR regulations. The GDPR aims to protect the personal data of individuals and to enforce stricter data management practices. However, existing provenance models fall short in fully complying with the GDPR's requirements.

The extended model introduces eleven changes to address the gaps in the original GDPRov. These changes are categorized into three types: plumbing, porcelain, and wallpaper extensions. Plumbing extensions directly impact how the model functions by adding new elements. Porcelain and wallpaper extensions aim to enrich the model with additional semantic meaning and detailed information as required by the GDPR text.

## Approach Contribution For The Compliance Questions

### Question 8
For each category of personal data, list the period for which the data will be retained. The model introduces the `startedAtTime` and `endedAtTime` relations to represent the period for which personal data will be stored. These components can be utilized to answer this question by providing explicit retention periods.

### Question 28
Are procedures in place to ensure personal data is kept up to date and accurate? The model does not explicitly address this but can track data updates through its provenance mechanisms, making it easier to ensure data accuracy.

### Question 29
Are retention policies and procedures in place to ensure data are held for no longer than is necessary? The `startedAtTime` and `endedAtTime` components can be used to track data retention policies, ensuring compliance with data retention requirements.

### Question 51
Are personal data systematically destroyed, erased, or anonymized when no longer legally required? While the model can track when data is created and modified, it does not explicitly cover data destruction or anonymization processes.

### Question 63
Are all transfers listed, including the nature of the data, the purpose of processing, etc.? The model introduces the `SourceExplanation` entity to document the source of data, which can partially address this question by tracking where data comes from and its purpose.

### Question 64
Is there a legal basis for the transfer, e.g., EU Commission adequacy decision? The `EvaluationOfAdequacy` entity can document the legal basis for data transfers, ensuring compliance with GDPR requirements.

## Approach Insuficiecies For Fulfill The Compliance Questions

### Question 28
While the model can track data updates through provenance, it does not explicitly ensure that procedures for keeping data up to date are in place. Additional mechanisms would be needed to enforce these procedures.

### Question 51
The model currently lacks components to systematically destroy, erase, or anonymize personal data. Additional extensions or integrations with data destruction mechanisms would be necessary to fully comply with this requirement.

## Key Contributions

- Eleven new changes to the GDPRov model to enhance compliance with GDPR.
- Introduction of `SourceExplanation` and `AlgorithmExplanation` entities for better transparency.
- Addition of `EvaluationOfAdequacy` entity to document the legal basis for data transfers.
- Categorization of changes into plumbing, porcelain, and wallpaper extensions for better organization and understanding.
- Enhanced tracking of data retention periods with `startedAtTime` and `endedAtTime` relations.

## State-of-the-Art

This extended model advances the state-of-the-art by filling gaps left by the original GDPRov model. It introduces new entities and relations that align more closely with the GDPR text, providing better tools for compliance. While other works have focused on using ontologies to model data protection requirements or trustworthy system provenance, this approach uniquely combines these elements with a specific focus on GDPR compliance.

The model also aligns with the work by Basin et al. (2018), which emphasizes the need for compliance by design. By integrating these new entities and relations, the model contributes to making data workflows more transparent, thus easing the burden of GDPR compliance.

While previous research has tackled issues like provenance-based auditing and trustworthy whole-system provenance, this extended model uniquely addresses the specific requirements of GDPR, making it a valuable contribution to the field. However, the model still requires further practical implementations and possibly additional mechanisms to fully automate and enforce GDPR compliance.

```