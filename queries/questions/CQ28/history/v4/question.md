# CQ28

Are procedures in place to ensure personal data is kept up to date and accurate and where a correction is required, the necessary changes are made without delay?

## Discussion

This question may suggest to burden the controller the guarantee that the personal data is kept up-to-date and accurate through the use of procedures. However, what do these terms mean in this context? In addition, how do we certify that a correction is required, that the necessary changes were made, and that they were done without undue delay?

### Analysis: The Terminology in Question

#### Up-to-data and Accurate Data

Before to approach this question properly, we need to clarify some terms used in the question. We highlight the terms 'up to date' and 'accurate' in the question: what does indeed it mean by the 'up to date' and 'accurate' data?

As long as we know, the GDPR corpus (including specialized text) lacks a definition of these terms. According to the Cambridge Dictionary, the concepts of 'up to date' and 'accurate' can be understood as something in accordance or agreement with the latest, the newest, the most recent standard or model. Note the definition of these terms pressuposes an object (e.g., the standard or model) which is used to evaluate whether the sentence subject (i.e., the 'something') is 'accurate' and 'up to date'. Hence, the use of 'accurate' always implies in the existence of an object in the sentence and qualifies the sentence subject by establishing some kind of proximity, in accordance, between this one and the object. For example, when we say "A is accurate", we tacitly presuppose a B (an ideal version of A) in such a way that makes it equivalent to saying "A is somehow equal to B". This predicate is usually measured through a quantifier (i.e., A is 73% accurate when compared to B).

The 'up to date' predicate establishes some kind of proximity (lack of differentiation) between the subject and the object. In general, both of these elements of the sentence refer to the same entity, but at a different instants along the time. For example, by saying "A is up to date", we tacitally evoque an A' (i.e., the state or version of A at the instant A was most-recently updated) which means "A, at the instant we say it, is somehow equal to A'". In other words, we mean "there is no variation in A, now, since its last updating".

From this analysis, we note, first, the mandatory presence of a third element, B or A' (the sentence object) when we employ both predicates. Back to the question, both predicates connect 'the personal data' (the subject in the sentence) to some sort of object, but what object? We understand that this object should be something in reality, something outboundary of the controller representations. For the purpose of clarifying this analysis, we name this entity that holds the truth as the source of truth (SOT). The SOT is the final entity, in reality, that possesses accurate and up-to-date information about the representative personal data in possession of the controller. Therefore, since the controller possesses a representation of the SOT, when the SOT changes, the controller does not have any more accurate and up-to-date personal data (e.g., Once Alice moved to a new address, the address she registered in a retail shop becomes inaccurate and out-to-date). Hence, the SOT provides the final answer about whether the personal data is accurate and up-to-date. For the sake of simplicity, we assume only problems with a single source of truth (SSOT). In the context of GDPR, only the data subject or a third party can assume the role of SSOT[^2]. The GDPRov provides classes like `gdprov:PersonalData`, `gdprov:Data`, `gdprov:Controller`, `gdprov:DataSubject`, and `gdprov:ThirdParty` to represent these terms.

The second conclusion we can deduce from this analysis is that both predicates, in this context, bear the same meaning: they establish a relation of similarity between the data in possession of the controller and the information of reality. The current GDPRov version needs classes to represent this information, although we need to analyze further terms before we propose something.

<!-- [TODO: you need to improve this explanation about proactive or reactive processing of rectify. It derives from the fact that the controller should have procedures to ensure the personal data is acurated. However, at the end of the day, this differenciation means make no sense. It just maybe be useful for the case of explanation the decision we take to model] -->

<!-- [NOTE: Not necessary for the purposes of this work] When the data subject assumes the role of the SSOT, the controller can proactively rectify the data by asking the data subject for the latest version of his/her data; otherwise, when the data subject requests for the controller to rectify his/her data, by informing them (rolling as the SSOT), the controller must **reactively** rectify them. The same actions are present when a **third party** roles the SSOT, differing only in that the third party does not hold the ownership of the personal data but the subject[^3]. -->

<!-- [NOTE: Not necessary for this work] The redaction may suggests to the comprehension that every changes in the SSOT is perceived by the controller via **requests**; the GDPRov, however, represents this perception as the controller **collecting** the data from that latter[^4]. -->

<!-- [NOTE: prior redaction about the term request] Note that in the controller realm, the changes in the SSOT can only be perceived via **requests** between the controller and the agent roling the SSOT. Only if and when the controller has this request can he assess the need for and delay of the change. -->

#### Procedures to Ensure the Accuracy

The question starts by asking whether there "are procedures in place to ensure personal data is kept up to date and accurate." At first glance, we may believe this question is fulfilled when we demonstrate the existence of activities that rectify every kind of personal data. In other words, since the controller has prescribed activities that rectify all modeled personal data, such a controller complies with this question. The GDPRov provides the classes `gdprov:RectifyData` to represent the prospective rectification process and `gdprov:RectifyDataActivity` for retrospective. Also, `gdprov:DataRectificationProcess` represents the plan of activitities for describing recification procedures.

However, the mere existence of such procedures is insufficient since the entire rectification process also involves (as we argue in the previous subsection) collecting the data from the SOT to ensure data accuracy and up-to-dateness. Therefore, alongside these rectification procedures, it is also necessary to demonstrate that every procedure to (proactively or reactively[^3]) collect personal data from the SOT leads to a rectification process when that correction is required. The classes `gdprov:DataCollectionStep` and `gdprov:DataCollectionActivity` respectively represent this collection procedure of personal data prospectively and retrospectively. The properties `gdprov:collectsData` and `prov:used` specifies the relation between the collection procedure and the personal data.

Finally, to complete address this question, we need to analyse and propose a representation for the cases where corrections were necessary.

#### Detecting Required Corrections and Applying Necessary Changes

When the controller has collected the personal data from the SOT (within the context of rectification), it owns the most accurate personal data (the same information the SOT has). At this time, the controller can take procedures to detect whether a correction is necessary by comparing the collected data against the stored data. In the event of a data discrepancy, we have detected a required correction case; in the event of a data correspondence, no correction is needed. Since the GDPRov does not provide any method to represent procedures to detect whether a correction is required, we introduce the class `gdprov:DataComparisonStep`, extending from `gdprov:DataStep`, to represent the prospective step of comparing different data. For the retrospective representation, we introduce the class `gdprov:DataComparisonActivity` as a subclass of `gdprov:DataActivity`. Both new classes also extend from `dpv:Match`, which represents procedures of combining, comparing, or matching data from different sources.

Once we detect a required correction, we can easily query for existing processes associated with those data that should be rectified and ensure the changes were applied. We introduce the property `gdprov:hadDataDiscrepancy` to represent the result of the analysis of whether there is a discrepancy in the data. Such a relation range to the `xsd:boolean` data, which carries the comparison outcome. In addition (following Pandit's commentary about this question), in the event of a discrepancy takes place, we propose the provenance graph represent this data discrepancy by using the property `owl:differentFrom`.

#### Without delay

The last term we must clarify is about such a delay time that must be avoided by the controllers who should apply 'the necessary changes'. What objectively does 'without delay' mean? What are its boundaries? One hour or two minutes? What could be used as a common ground for deciding whether a rectification was performed without delay?

Article 12 [[eugdpr2016a]] lays down the rules about the communication between the controller and the data subject to ensure the exercise of the rights introduced in GDPR. This article, specifically, has clarified the comprehension of 'without delay' by aggregating it through a coordinating conjunction to a sentence that establishes **the period within one month of receipt of the rectification request**. The article says:

> The controller shall provide information on action taken on a request under Articles 15 to 22 to the data subject without undue delay and in any event within one month of receipt of the request.
>
> [[GDPR|GDPR, Article 12, part of point 3]]

As far we understand, this 'without delay' is used to prevent a lazy controller. However, it does not serve as an objective parameter to establish the boundaries between a complaint and a non-compliant scenario. Thus, we consider the period of one month to answer this question. Since it is concerned with the time spent in performing the procedures, we are interested in the retrospective graph. This can be obtained by querying the period between the time the first activity took place and the time the last activity ended. PROV ontology sets up `prov:startedAtTime` and `prov:endedAtTime` to represent these period.

## Related Work Comparison

<!-- [TODO: Improve this section] -->

Beyond the common terms (i.e., the data subject, the controller), the related work have introduced the following terminology that might be useful to represent this question:

 - `bartolini:Rectification` — The request to obtain from the controller the rectification of personal data relating to them is inaccurate. Subclass of Action.
 - `ucjcich:Request` — This model represents the request concept as a movement started by the data subject towards the controller so that the latter performs the desired action using the informed data. We believe that this form of modeling introduces a counter-intuitive relationship between the data subject and the controller, according to the principle established by the GDPR[^4].

<!-- Ok. -->
<!-- We need to represent the request. Thus, how does Pandit represent a request? It does not represet it. -->

## Extending the model

Considering the prior analysis, we summarize in Table X the terms we identify in this question and the derived classes to represent them in the GDPRov ontology.

| Classes                                          | Description | Extending? |
|--------------------------------------------------|-------------|--------|
| `:PersonalData`, `:PersonalDataEntity`           | The accurate or inaccurate data at the prospective and retrospective level, respectively. | |
| `:DataSubject`, `:ThirdParty`                    | The data subject and third party how possess the source of truth about data accuracy and up-to-dateness. | |
| `:DataRectificationProcess`                      | The rectification process describes all plans and processes of data rectification (subclass of `:Process`). | |
| `:RectifyData`, `:RectifyDataActivity`           | The propsective and retrospective activity for rectifying data respectively. | |
| `:DataCollectionStep`, `:DataCollectionActivity` | The request to rectify the data proactively or reactively. | |
| `:DataComparisonStep`                            | The prospective comparison of the collected data against the stored one. (subclass of `:DataStep`) | ✓ |
| `:DataComparisonActivity`                        | The retrospective comparison of the collected data against the stored one. (subclass of `:DataActivity`) | ✓ |

| Properties            | Domain                                 | Target                                 | Description                                                                                                              | Extending? |
|-----------------------|----------------------------------------|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------|------------|
| `:collectsData`       | `:DataStep`                            | `:Data`                                | Links data obtained (collected) by the step/activity that acquired it                                                     |            |
| `:hadDataDiscrepancy` | `:DataComparisonActivity`              | `xsd:boolean`                          | The comparison activity result. It is "true" in case of collected and stored data are the same; otherwise, it is "false". | ✓          |
| `owl:differentFrom`   | `:PersonalDataEntity`, `:PersonalData` | `:PersonalDataEntity`, `:PersonalData` | The relation stablising the existing differentiation between a collected and stored data.                                 |            |

<!-- [[NOTE: This is a paragraph for consultation. Its Ideal were prior introduced ]] Before we address this question properly, some clarification about the utilized terminology is required. We might analyze this question into three parts. The first one is concerned about the 'procedures [that] ensure personal data is ketp up to date and acurate'. Another way to approach this is from the perspective of the controller, for every personal data it holds must have a check whether there 'are procedures in place to ensure personal data is kept up to date and accurate'. This first part can be addressed by answering positively or negatively, for each personal data the controller holds, whether there is a plan that ensure the rectification of that data[^3]. -->

<!-- [TODO: Is it indeed no necessary to represent an activity that made the checking whether there are differences between the current and stored data?] -->

## The Query

The process of building SPARQL queries from natural language is an in-process task in the literature[^5]. Since our objective here is solely to demonstrate the feasibility of employing provenance techniques to address the remaining question elicited in the [[TODO: Nome do documento que trás as perguntas de conformidade]], We are comfortable at proposing of generical SPARQL query at the GDPRov level, capable of answer the question at hand. We will also bring some highlights about the decisions we made during the process of building this query. The query we propose is depicted in the [[#^Figure01|Figure 1]]. We use Graffoo to graphically represent the classes and properties in the query.

![](./.data/query.png)
Figure 1: The SPARQL query representation of question CQ28 using Graffoo standard.
^Figure01

1. The GDPRov centralizes all information about rectification activity around the instances of `:RectificationProcess`. Each of these instances is captured by the variable `?process` and contains the prospective graph that is used to demonstrate the required procedures in question;
2. The `?collectedData` represent the instances of the categories of personal data the controller allows to rectify, by collecting the data (`?dataCollection`) from the user. The plan also describes the fundamental step comparison of the collected data and the store (`?dataComparison`), which ;
3. Since we demonstrate that every category of personal data can be rectified through this process, we then have fulfilled the first part of the current question; we assure there "are procedures in place to ensure [every] personal data is kept up to date and accurate";
4. The second part of this question concerns to the retrospective information. Since we do not represent the information about the time each step will take, to answer whether such procudures in question have performed without delay. For address this question, we must ensure that every subgraph which `?resultComparison` is `true`, we also have the difference between `?startedAt` and `?rectificationEndedAt` lower than one month.
<!-- The question can be addressed into the three following questions:

(a) Are procedures in place to ensure personal data is kept up to date and accurate?

The answer for this question is simple querying for the existant instances of `gdprov:RectifyData`, which represent a instance of a plan to rectify data

(b) What corrections are necessary?

List all individuals involved the cases where the collected data is different from the stored data.

(c) For those which correction is necessary, it was taken into a month?

For all individuals in the last query result, list the delta time between the instances of gdprov:DataCollectionActivity and the instances gdprov:RectifyDataActivity involved in the same change. -->

## Evaluation


The privacy policy of TCU does not provide any specific information about the rectification process. On the counter part, SAPOS does not provide a interface for the use to edit their information (such as>)

<!-- First, we analyze the question into three parts: (i) '_Are procedures in place to ensure personal data is kept up to date and accurate_'; (ii) '_Where a correction is required, the necessary changes are made_'; and (iii) '_without delay_.' -->

<!-- > [!INFO]
> This question requires knowledge about how SAPOS personal data correction occurs. Answer: The students and professors cannot edit their own information. So, I suppose they should email the admin to change it.

The second part lies over those personal data that have a posivive answer in part one: on existing such a procedures, 'where a correction is required [...]' This statement is part of a boolean sentance that can be evaluante 

[The third is about the qualifier "without delay"] -->

<!-- ### Within the context: The Trinity College Case

"Personal data processed by Trinity College should be reviewed and verified as being accurate wherever possible. Where inconsistencies are identified by Trinity College, or where a data subject or other party informs the University of same, actions should be taken to ensure that such inaccuracies are corrected with immediate effect. All requests for rectification of personal data should be forwarded to the Data Protection Officer without delay." (Data Protection Handbook, p. 31).  -->

# Footnote

[^1]: Note that both definitions relies on a certain kind of philsophy of differenciation, which approaches the nature of identities which conceive the formulation of ... see more at <https://iep.utm.edu/differential-ontology/>. Additionally, the definition of 'up to date' also includes the information of the instant the reader was doing so.

[^2]: The cases where the controller roles the SSOT necessarily lead to a tautological assessment since the represented personal data also assumes the role of the source of truth. Thus, it is unnecessary to face this question.

[^3]: Differentiating between proactive and reactive rectifications can be helpful for evaluations interested in verifying the controller's intention to keep personal data accurate and up-to-date. Since the controller does not directly relate to the SSOT, only through requests, those who (e.g., every semester) proactively ask for the SSOT to rectify the personal data have demonstrated to bear more interest in the actual value of the data than that reactively informed.

<!-- Finally, differentiating between proactive and reactive rectifications can be helpful for evaluations interested in verifying the controller's intention to keep personal data accurate and up-to-date. Since the controller does not directly relate to the SSOT, only through requests, those who (e.g., every semester) proactively ask for the SSOT to rectify the personal data have demonstrated more interest in the actual value of the data than that declared through reactive receiving requests. -->

[^4]: By representing the data subject requesting the data controller to perform some operation over his/her data, it may reinforce the prior language used before the GDPR, in which the data controller is the real owner of the data and data subject should ask (permission for) the controller to perform processing over their data. However, as appointed by [[kuner2012european|Kuner]], that is the right copernican reversion the GDPR introduced: by shifting toward the data subject's conception of privacy, we believe that a better representation might be the controller collecting the data from the data subject, as proposed by GDPRov.

[^5]: Ferré, Sébastien. ‘Sparklis: An Expressive Query Builder for SPARQL Endpoints with Guidance in Natural Language’. Semantic Web 8(3) : 405-418. IOS Press, 2017. PDF [[TODO: Add on the literature]]