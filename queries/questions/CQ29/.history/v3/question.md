# CQXX

Are retention policies and procedures in place to ensure data are held for no longer than is necessary for the purposes for which they were collected?

## Discussion

<!-- TODO: Improve this  -->
<!-- This question pertains to the GDPR's requirement for data controllers to implement retention policies and procedures that ensure personal data is not kept longer than necessary for the purposes it was collected. -->

Facing this question, Pandit assumes these procedures in question as synonyms for data deletion. Hence, he highlights the difficuty to evaluate programmatically whether these procedures deleted the data once the purposes for which the data was collected has been acheived. Said differently, he places the difficulty to assert the causality between the event of the data's purpose fulfillment and the data deletion performation. Additionally, he appends as a question requisit the necessity to demonstrate whether this data deletion was performed at the correct time. He places the insufficiency of holding the information of what data is collected and for what purposes to demonstrate whether the data was deleted whithout delay. He ends his comment suggesting that some information at the instance level might be considered to answer this question, although (without further explanation) it might be very complex, according to him.

In summary, Pandit approaches this question placing the data deletion procedure as the center of this question. From that, it is necessary to show the causality dimension of this data deletion and, in case it was caused by the data's purpose fulfillment, it must be shown whether it was performed withou delay in terms of the data retention policy.

In our analysis, it seems reasonable the assumptions made by Pandit that connects the procedures in question to the data deletion. We just attach the case where deletion is not possible. In such the cases, the GDPR introduces the data anonymization procedures as alternatives (see more in Article 89(1) and Recital 26). Indeed, we can read the sentence "data are held for no longer than is necessary" as the following conditional sentence: "once the data is no longer necessary, then it must be deleted". Hence, we also approach this question as one interested in the information of data deletion.

However, from our perspective, this Pandit's comment have also introduced a tacit assumption we are not in fully agreement; or, at least, we see as if his comment have limited the question to the matter of the that assumption. From our perspective, we see as whether this Pandit's comment faces this question assuming it is only interest in the retrospective information, disregarding the prospective information. We see it when he opt by using the verbs in the past form, places the necessity of demonstration that the deletion was performed at the correct time (instead of what can do), and ends by appealing to the instance level of the provenance graph as the only possible way to address this question (despite his ackownledgement about the complexity).

However, in our analysis, we argue this question is more about the prospective graph than the retrospect one: the question is concerned whether there are plans that rule the data deletion, when a data is no longer necessary for the purposes for which they were collected. We propose this interpretation as a more accurate one based on the two following pilars: first, the sentence is not in the past form (i.e., it is written "data **are** held" instead of "data **were** hold"), which not necessarily bind our attention solely to the past; and, second, if it is somehow concerned to the retrospective events, it is made unecessarily, since the question CQ51[^1] already covers this case.

[^1]: "Are personal data systematically destroyed, erased, or anonymised when they are no longer legally required to be retained."

Therefore, we approach CQ29 assuming it as a question concerned with the prospective information solely, while CQ51 is looking at for the retrospective ones. In light of this assumption, backing to the Pandit's approach, only the causality dimension of data deletion stands; while the procedure perfomation time belongs to the realm of past, which we are dealing in the question CQ51. As a consequence, the properly addressing to this question depends on answering the following subquestion: _how to assert whether a data deletion procedure is caused by the fact the data is no longer necessary for the purposes for which it was collected initially?_

Before address that subquestion, we must analyse the terminology enolved. For the sake of simplification in the further terminology analysis subsection, we transpose that subquestion into the following sentence: _when the data is no longer necessary, then it must be deleted_

### Analysis: The Terminology in Question

#### Data No Longer Needed For Original Purpose

Starting from the antecedent, we are dealing with the data storage condition term which is narrowly attached to the **purpose limitation** principle (Article 5(1)(b)), where personal data is "collected for specified, explicit, and legitimate purposes and not further processed in a manner that is incompatible with those purposes." [^7] and to the **storage limitation** principle (Article 5(1)(e)), which states that personal data is "kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed." [^8]

In Q08, we already introduce four cases of possible data storage conditions: Data can be retained for a fixed period (e.g., 3 years), for fixed date achieves (e.g., 3 december 2033), after purpose (e.g., during the period the subject is a employee), or indefinite. Hence, at this time, our model is alread capable to represent the case when the data is no longer necessary for the purposes for which it was collected initially.

#### Data Deletion Procedure

Indeed, the current version of GDPR model does not support elements capable of representing the causality between events. This lacking of these components give rises to our effort to evolving this model so that it can represent causality.

Even the the related models, shown in the Related Work section, do not introduce such a component, capable of representing causality. Consequently, there are no models in the literature, gathered in this study, capable of address this question correctly.


sosa:Procedure <-[subclassof]- gdprov:EnsureComplianceProcess <-[subclassof]- gdprov:EnsureStoringOnlyNecessaryDataProcess
sosa:FeatureOfInterest <-[subclassof]- gdprov:StorageCondition
sosa:ObservableProperty <-[subclassof]- time:Duration (TODO: create gdprov:Duration)
sosa:Observation, gdprov:DataUsageStep <-[subclassof]- gdprov:StorageConditionFulfillmentObservationStep
sosa:Actuation <-[subclassof]- gdprov:DataAnonymisationStep, gdprov::DataDeletionStep

QUESTION: Por que nosso modelo especifica as StorageConditions como subclassses de Duration ao inves de Storage Condition? Não seria mais simples representar como subclasses de StorageCondition?
  Resposta: Proavelmente seguimos a definição proposta pela DPV, que define desse jeito
  TODO: Criar um arquivo de QnA e colocar todas as perguntas lá.


----


Hence, since this question ask for  To represent the causality relation between the deletion procedure

---

In summary, based on this Pandit's analysis, to properly address this question we must solve the following two subquestions: (i) How to establish whether a data deletion procedure is/was caused by the fact the data is no longer necessary for the purposes for which it was collected initially? (ii) How to evaluate whether the data was deleted at the correct time?

In addition to these Pandit's subquestion, we : "How to evaluate programmatically whether the purposes for which data was collected have been achieved?"

Before address these two subquestions, let first analysis the Pandit's analysis. It seems reasonable his assumption that connects these procedures in question to the data deletion. Indeed, we can read "data are held for no longer than is necessary" as the following conditional sentence: "once the data is no longer necessary, then it must be deleted". Hence, this question is interested in the information of data deletion.

However, this Pandit's comment also holds a tacit assumption we are not sure about. It seems Pandit assumes this question is interest in retrospective information solely. 

Based on this commentary, we can deduce Pandit is assuming this question

Considering this Pandit's comments, we 

This Pandit's analysis raises up some issues we must solve to address this question.

---

When approching this question, Pandit raises up two issues: first, how to evaluate programmatically whether the purposes for which data was collected has been achieved? Second, how to evaluate whether the data was deleted at the correct time? He recomends to consider the instance-level graph, despite he admits the complexity of the question. Hence, based on this Pandit's analysis, we need to consider two critical subquestions to address this question:

1. How to evaluate programmatically whether the purposes for which data was collected have been achieved?

2. How to evaluate whether the data was deleted at the correct time?

To provide a comprehensive answer, it is mandatory to analyze how other ontologies proposed in the scientific literature have addressed similar questions. We will integrate relevant concepts from these ontologies into our analysis and model extension.

### Relevant Ontologies in the Literature

Several ontologies have been proposed to address GDPR compliance and data privacy concerns:

- **Data Privacy Vocabulary (DPV)**[^1]
- **PROV-O (Provenance Ontology)**[^2]
- **GDPRtEXT**[^3]
- **GConsent**[^4]
- **Privacy Ontology by Bartolini et al.**[^5]
- **PrOnto (Privacy Ontology)**[^6]

These ontologies offer concepts and structures that can help model data retention, purpose specification, and compliance procedures.

## Analysis: The Terminology in Question

### Retention Policies and Procedures

- **Retention Policies**: Formal guidelines defining how long different categories of personal data should be retained, based on legal obligations and the purposes for which the data was collected.

- **Procedures**: Systematic processes implemented to enforce retention policies, ensuring that data is deleted or anonymized when it is no longer necessary.

### Purpose Specification and Fulfillment

Under the GDPR's **purpose limitation** principle (Article 5(1)(b)), personal data should be:

> "collected for specified, explicit, and legitimate purposes and not further processed in a manner that is incompatible with those purposes." [^7]

### Storage Limitation

The **storage limitation** principle (Article 5(1)(e)) states that personal data should be:

> "kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed." [^8]

## Subquestion 1: Evaluating Whether Purposes Have Been Achieved

The calculation whether the data was deleted at the correct time depends on the time the purposes for which data was collected has been achieved, which depends on the storage condition under which the data is submitted. In Q08, we introduce four cases of storage condition: Data can be retained for a fixed period (e.g., 3 years), for fixed date achieves (e.g., 3 december 2033), after purpose (e.g., during the period the subject is a employee), or indefinite.

### How Other Ontologies Address This

#### Data Privacy Vocabulary (DPV)

The DPV provides classes and properties for representing purposes (`dpv:Purpose`), processing activities, and legal bases. It allows for the specification of purposes and linking them to data processing activities.

#### GConsent

GConsent extends DPV and provides mechanisms to represent consent and its associated purposes. It includes classes like `consent:Consent`, `consent:hasPurpose`, and properties to link consent to data processing.

#### PROV-O

PROV-O provides a framework for representing provenance information, which can be used to track activities, entities, and agents involved in data processing.

#### PrOnto

PrOnto offers a legal ontology for privacy and data protection compliance, providing concepts for legal justifications, purposes, and obligations.

### Integrating Concepts

By leveraging concepts from these ontologies, we can represent purposes, link them to data processing activities, and define criteria for purpose fulfillment.

## Subquestion 2: Evaluating Whether Data Was Deleted at the Correct Time

To evaluate whether data was deleted at the correct time, we need to:

1. **Determine Retention Periods**: For each data element, calculate the retention period based on the collection date and the purpose.

2. **Monitor Data Lifecycles**: Keep track of data from collection to deletion, including any processing activities.

3. **Verify Deletion Activities**: Check if a deletion activity occurred at or before the end of the retention period.

4. **Assess Compliance**: Compare the actual deletion time with the scheduled deletion time to determine compliance.

### How Other Ontologies Address This

#### DPV

DPV includes the concept of `dpv:Duration` and properties like `dpv:hasDuration` to specify retention periods.

#### PROV-O

PROV-O allows for the representation of activities (`prov:Activity`), entities (`prov:Entity`), and the relationships between them, including timestamps (`prov:generatedAtTime`, `prov:invalidatedAtTime`).

#### Privacy Ontology by Bartolini et al.

This ontology provides concepts for data handling policies, including retention and deletion policies.

### Integrating Concepts

By incorporating these concepts, we can represent retention periods, link them to data elements, and track deletion activities with timestamps.

## Representing the Concepts in GDPRov Ontology

### Existing Classes and Properties

From the provided GDPRov ontology and considering extensions from other ontologies:

- **Classes**:
  - `gdprov:PersonalData`
  - `gdprov:DataEntity`
  - `gdprov:Process`
  - `gdprov:DataDeletionActivity`
  - `gdprov:Purpose`
  - `dpv:Purpose` (from DPV)
  - `prov:Activity`, `prov:Entity` (from PROV-O)

- **Properties**:
  - `gdprov:hasPurpose`
  - `gdprov:collectedAt`
  - `prov:used`
  - `prov:invalidated`
  - `dpv:hasDuration`

### Proposed Extensions

#### New Classes

1. **`gdprov:PurposeFulfillmentEvent`**

   - **Definition**: Represents an event or condition indicating that the purpose for which data was collected has been achieved.
   - **Subclass of**: `prov:Entity`
   - **Alignment**: Similar to `prov:Activity` and `dpv:Processing`.

2. **`gdprov:PurposeFulfillmentActivity`**

   - **Definition**: An activity that results in the fulfillment of a purpose.
   - **Subclass of**: `prov:Activity`

3. **`gdprov:DataLifecycle`**

   - **Definition**: Represents the lifecycle of data from collection to deletion.
   - **Subclass of**: `prov:Entity`
   - **Alignment**: Can be aligned with `dpv:PersonalDataHandling`.

#### New Properties

1. **`gdprov:hasPurposeFulfillmentEvent`**

   - **Domain**: `gdprov:Purpose`
   - **Range**: `gdprov:PurposeFulfillmentEvent`
   - **Alignment**: Similar to `prov:wasGeneratedBy`.

2. **`gdprov:fulfillsPurpose`**

   - **Domain**: `gdprov:PurposeFulfillmentActivity`
   - **Range**: `gdprov:Purpose`
   - **Alignment**: Similar to `dpv:hasPurpose`.

3. **`gdprov:hasLifecycle`**

   - **Domain**: `gdprov:PersonalData`
   - **Range**: `gdprov:DataLifecycle`

4. **`gdprov:deletedAt`**

   - **Domain**: `gdprov:DataDeletionActivity`
   - **Range**: `xsd:dateTime`
   - **Alignment**: Similar to `prov:invalidatedAtTime`.

## Extending the Model with Concepts from Other Ontologies

### Incorporating DPV Concepts

- **`dpv:Purpose`**: Use `dpv:Purpose` to define and categorize purposes.

- **`dpv:hasPurpose`**: Use this property to link `gdprov:PersonalData` to `dpv:Purpose`.

- **`dpv:Duration`**: Use for specifying retention periods.

### Utilizing PROV-O Relationships

- **`prov:wasGeneratedBy`**: Link data to the activity that generated it.

- **`prov:wasInvalidatedBy`**: Link data to the activity that deleted it.

- **`prov:generatedAtTime`** and **`prov:invalidatedAtTime`**: Record timestamps for creation and deletion.

### Integrating GConsent Elements

- **`consent:Consent`**: Represent consent as an entity that may specify purposes and retention periods.

- **`consent:hasExpiryTime`**: Indicate when consent expires, which may affect data retention.

### Including PrOnto Legal Concepts

- **`pronto:LegalBasis`**: Represent the legal basis for data processing.

- **`pronto:Obligation`**: Represent obligations such as data deletion after purpose fulfillment.

## The Query

### Subquestion 1: Evaluating Purpose Achievement

#### SPARQL Query for Purpose Fulfillment

```sparql
PREFIX gdprov: <https://w3id.org/GDPRov#>
PREFIX dpv: <https://w3id.org/dpv#>
PREFIX prov: <http://www.w3.org/ns/prov#>

SELECT ?data ?purpose ?fulfillmentEvent ?eventTime
WHERE {
  ?data a gdprov:PersonalData .
  ?data dpv:hasPurpose ?purpose .
  OPTIONAL {
    ?purpose gdprov:hasPurposeFulfillmentEvent ?fulfillmentEvent .
    ?fulfillmentEvent prov:generatedAtTime ?eventTime .
  }
}
```

#### Explanation

- Retrieves all personal data and their associated purposes.
- Checks if there is a fulfillment event for each purpose.
- Retrieves the event and its timestamp if it exists.

### Subquestion 2: Evaluating Data Deletion Timing

#### SPARQL Query for Data Deletion Timing

```sparql
PREFIX gdprov: <https://w3id.org/GDPRov#>
PREFIX dpv: <https://w3id.org/dpv#>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?data ?collectionDate ?fulfillmentDate ?retentionDuration ?scheduledDeletionDate ?actualDeletionDate
WHERE {
  ?data a gdprov:PersonalData .
  ?data gdprov:collectedAt ?collectionDate .
  ?data dpv:hasPurpose ?purpose .
  
  OPTIONAL {
    ?purpose gdprov:hasPurposeFulfillmentEvent ?fulfillmentEvent .
    ?fulfillmentEvent prov:generatedAtTime ?fulfillmentDate .
  }
  
  ?purpose dpv:hasDuration ?retentionDuration .
  
  BIND(IF(BOUND(?fulfillmentDate), ?fulfillmentDate, ?collectionDate) AS ?startDate)
  BIND(xsd:dateTime(?startDate) + xsd:duration(?retentionDuration) AS ?scheduledDeletionDate)
  
  OPTIONAL {
    ?deletionActivity a gdprov:DataDeletionActivity .
    ?deletionActivity prov:used ?data .
    ?deletionActivity gdprov:deletedAt ?actualDeletionDate .
  }
}
```

#### Explanation

- Calculates the scheduled deletion date based on purpose fulfillment.
- Compares it with the actual deletion date.
- Identifies discrepancies between scheduled and actual deletion times.

## Evaluation

By integrating concepts from DPV, PROV-O, and other ontologies, data controllers can:

- **Programmatically Evaluate Purpose Achievement**: Use purpose fulfillment events and activities to monitor when data is no longer needed.

- **Assess Timely Data Deletion**: Track deletion activities and compare them with scheduled dates to ensure compliance.

- **Demonstrate Compliance**: Provide a transparent audit trail of data processing activities.

## Conclusion

Incorporating concepts from established ontologies like DPV, PROV-O, GConsent, and PrOnto enriches the GDPRov model, allowing for a more robust representation of data retention policies and procedures. This integration enables data controllers to:

- **Define and Track Purposes**: Clearly specify purposes and monitor their fulfillment.

- **Implement Retention Policies**: Programmatically enforce retention periods based on purpose fulfillment.

- **Ensure Timely Deletion**: Verify that data is deleted or anonymized at the correct time.

- **Enhance Compliance**: Provide comprehensive documentation and evidence of compliance efforts.

By adopting this multi-ontology approach, small and medium-sized businesses can effectively address GDPR requirements regarding data retention, optimizing their data handling practices and reducing the risk of non-compliance.

## Footnotes

[^1]: **Data Privacy Vocabulary (DPV)**: A vocabulary providing terms for describing and categorizing purposes, processing, and legal bases under GDPR. [DPV Specification](https://w3id.org/dpv)

[^2]: **PROV-O (Provenance Ontology)**: A W3C recommendation for representing provenance information. [PROV-O Specification](https://www.w3.org/TR/prov-o/)

[^3]: **GDPRtEXT**: An ontology providing a machine-readable version of the GDPR text. [GDPRtEXT](https://w3id.org/GDPRtEXT)

[^4]: **GConsent**: An ontology for expressing consent and its associated information. [GConsent Specification](https://w3id.org/GConsent)

[^5]: Bartolini, C., Muthuri, R., & Santos, C. (2015). Using ontologies to model data protection requirements in workflows. *ISWC 2015 Privacy and Policy Workshop*.

[^6]: Bonatti, P. A., Kirrane, S., Polleres, A., & Wenning, R. (2017). Transparent Personal Data Processing: The Road Ahead. *International Conference on Computer Safety, Reliability, and Security*, 337-349.

[^7]: GDPR, Article 5(1)(b) - Purpose Limitation Principle.

[^8]: GDPR, Article 5(1)(e) - Storage Limitation Principle.

---

By leveraging established ontologies and integrating their concepts into the GDPRov model, we create a comprehensive framework for addressing data retention requirements under the GDPR. This approach facilitates programmatic evaluation of purpose achievement and timely data deletion, ensuring robust compliance mechanisms.