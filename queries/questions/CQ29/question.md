# CQ29

Are retention policies and procedures in place to ensure data are held for no longer than is necessary for the purposes for which they were collected?

## Discussion

<!-- TODO: Improve this  -->
<!-- This question pertains to the GDPR's requirement for data controllers to implement retention policies and procedures that ensure personal data is not kept longer than necessary for the purposes it was collected. -->

Facing this question, Pandit assumes these procedures in question as synonyms for data deletion. Hence, he highlights the difficulty of programmatically verifying whether these procedures effectively deleted the data once its initial purpose was fulfilled. In other words, he emphasizes the challenge of establishing causality between the fulfillment of the data’s purpose and the execution of data deletion. Furthermore, he adds a requirement to demonstrate whether this deletion was performed at the appropriate time. Pandit argues that merely knowing what data was collected and for what purposes is insufficient to prove that the data was deleted without undue delay. He concludes by suggesting that information at the instance level might be necessary to answer this question, although he notes that this approach could be highly complex without providing further details.

In summary, Pandit’s approach centers on data deletion or anonymization procedures as the core of this question; in particular, those procedures occasionated due to the fulfillment of the data’s purposes. He also points the importace of demonstrating that such the procedures was performed without delay in accordance with the data retention policy.

In our analysis, Pandit's assumptions connecting the procedures in question to data deletion appear reasonable. However, we must also account for cases where deletion is not feasible. In s" instances, the GDPR offers data anonymization as an alternative (see Article 89(1) and Recital 26). Indeed, the phrase "data are held for no longer than is necessary" can be interpreted as a conditional statement: "once the data is no longer necessary, it must be deleted or anonymized." Therefore, we approach this question with an interest in data deletion and anonymization.

Nevertheless, we identify an implicit assumption in Pandit’s argument with which we do not fully agree, or at least find to be overly limiting the question matter. Pandit seems to frame the question solely in terms of retrospective information, disregarding the prospective perspective. This is evident from his use of past-tense verbs, his also emphasis on demonstrating that deletion was performed at the correct time (rather than focusing on future actions), {{[TODO:] and from his conclusion that evoques the instance level of the provenance graph despite acknowledging its complexity.}}

In contrast, we argue that the question is more about prospective planning than the retrospective verification. The central concern is whether plans are in place to regulate data deletion when the data is no longer needed for its original purpose. We base this interpretation on two key points: first, the sentence is phrased in the present tense ("data **are** held" rather than "data **were** held"), indicating that the focus need not be limited to past events. Second, if there were any concerns about retrospective events, they are already addressed by CQ51[^1].

[^1]: "Are personal data systematically destroyed, erased, or anonymised when they are no longer legally required to be retained."

Therefore, we interpret CQ29 as a question concerned solely with prospective information, while CQ51 addresses retrospective ones. In light of this assumption, we approach this question as whether it is only searching for plans of data deletion or anonymization once the purpose for which the data was collected has expired. The information whether such the procedures has performed in-time (as pointed by Pandit), we address in CQ51, due to be related to retrospective information.

Finally, for the sake of clarity, we analyze the terms within this question considering the sentences in the following conditional statement: _If the data purposes expires, then it must be deleted or annymized._

### Analysis: The Terminology in Question

#### The Data Purpose Expiring

Starting by the antecedent, we address the term concerning data storage conditions, which is closely tied to the purpose **limitation principle** (Article 5(1)(b)). This principle mandates that personal data must be "collected for specified, explicit, and legitimate purposes and not further processed in a manner that is incompatible with those purposes" [^7]. Additionally, it is connected to the **storage limitation** principle (Article 5(1)(e)), which stipulates that personal data must be "kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed" [^8].

In Q08, we arguably elicit four scenarios as being enough to represent the all possibilities concerning to data storage conditions. For each scenario, we extend the original GDPRov model with a new set of componets inheriting from well-stablished ontologies (e.g., Time Ontology):

- When data must be retained for a period of time (e.g., "The data is retained for 3 year since the instant it was collected"), we introduce the component `gdprov:TemporalDuration`;
- In case the data is kept until a specific data (e.g., "All data we collect is kept until December 3th, 2033"), the component `gdprov:UntilTimeDuration` must be used;
- Whether the controller holds the data unless some event takes place (e.g., "We keep all personal data until the data owner asks for deletion"), we suggest the use of `gdprov:UntilEventDuration` component;
- Finally, when the controller keeps the data indefinitely, we introduce `gdprov:EndlessDuration` component.

Therefore, with those introduced components, our model is already capable of representing cases where the data purposes has expired and it is no longer necessary for the original purposes for which it was collected.

#### The Data Deletion or Anonymization Procedure

In GDPRov, we find components designed to those case when data must be deleted and anonymized. Such the procedures can take place using `gdprov:DataErasureProcess` or `gdprov::HandleRightOfErasure` components, which the steps involved in the prospective plan are described through `gdprov:DataDeletionStep` or `gdprov:DataAnonymisationStep`, while the retrospective activities by `gdprov:DataDeletionActivity` or `gdprov:AnonymisationActivity`. The `gdprov:AnonymisedDataEntity` component depicts those data anonymized by some activity. On the other hand, prospective data can be represented by `gdprov:AnonymisedData` or with `gdprov:PersonalData` having `gdprov:hasAnonymityLevel`, which enable discretion of anonymity level amoung `gdprov:Anonymised`, `gdprov:DeAnonymised`, or `gdprov:PseudoAnonymised`.

<!-- generatesAnonymisedData
isAnonymisedByStep
AnonymityLevel -->

#### If...Then


Although the GDPRov already provide components to represent data deletion or anonymization procedures, the current version of GDPR model does not provide elements capable of representing the causality between the events. This lacking places the necessity to evolve the GDPRov so that it can represent causality between the event when the data is no loger needed and the data deletion or anonymization procedures. In literature, we found the Semantic Sensor Network Ontology (SSN) as an ontology designed to represent the relationships between events and processes, including causal connections. By injecting SSN concepts to the GDPRov model, that latter gains the capability to express the causality between the procedures in which the data is no longer needed and the initiation of data deletion procedures. Specifically, the SSN ontology utilizes constructs such as `sosa:Procedure` and `ssn:Stimulus` to model the performance and outcomes of processes, making it a suitable foundation for representing the causal triggers in GDPRov.

{{TODO: Despites this trigging takes place from different techniques, the prospective 

To illustrate, this causality problem in software engineering can be instantiated in three common scenarios:

1. **Periodic Compliance Checks**: The compliance process is periodically activated to verify whether the storage condition for any data has expired. In this case, the procedure continuously monitors data status and triggers deletion processes accordingly.
2. **Event-Driven Activation**: When a storage condition expires, it directly triggers a function responsible for ensuring compliance with data retention policies. This event-driven approach eliminates the need for continuous monitoring, relying instead on explicit signals from the storage condition.
3. **Message Queue System**: When a storage condition ends, a message indicating this event is sent to a queue or messaging pool. This queue contains all expired conditions, allowing compliance mechanisms to process and address them asynchronously.

Our proposed model can accommodate all these scenarios, offering flexibility in how organizations implement and enforce compliance with retention policies. }}

## Extending the model

In light of the analysis presented here, we summarize in Table X the terms identified in this question and the corresponding classes introduced to represent them within the GDPRov ontology:

| Term                            | Ontology Class                               | Subclass of                             |
|---------------------------------|----------------------------------------------|-----------------------------------------|
| Procedure                       | sosa:Procedure                               | gdprov:EnsureComplianceProcess          |
| Ensuring Necessary Data Storage | gdprov:EnsureStoringOnlyNecessaryDataProcess | sosa:Procedure                          |
| Storage Condition               | sosa:FeatureOfInterest                       | gdprov:StorageCondition                 |
| Duration                        | sosa:ObservableProperty                      | time:Duration (suggest gdprov:Duration) |
| Data Usage Step                 | sosa:Observation, gdprov:DataUsageStep       | gdprov:StorageConditionFulfillmentStep  |
| Anonymization Step              | sosa:Actuation                               | gdprov:DataAnonymisationStep            |
| Deletion Step                   | sosa:Actuation                               | gdprov:DataDeletionStep                 |

This table outlines the classes and subclass relationships necessary to fully represent the concepts addressed in CQ29. By incorporating these classes, GDPRov is equipped to handle both the retrospective and prospective dimensions of data retention and deletion, ensuring that compliance is systematically verified and enforced.'