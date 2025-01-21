# CQ29

Are retention policies and procedures in place to ensure data are held for no longer than is necessary for the purposes for which they were collected?

## Discussion

This question may suggests to burden the controller to guarantee that the personal data are held for no longer than is necessary for the purposes for which they were collected initially, it must be achieved through the use of retention policies and procedures. Both have been addressed this question places some challenges for modelling: how can it programmatically evaluate whether the purposes for which data was collected has been achieved? how to ensure whether the data was deleted at the correct time? Before address this questions, it is necessary to clarify some terms used in this question.

Indeed, provenance solely have no capability to enforce the controllers. 



---

Decisões de modelagem:

- Consideramos utilizar o elemento `gdprov:MonitorCompliance` da ontologia original para esta tarefa. Porém, os procedimentos em questão devem "garantir" e não apenas "monitorar".

---

> [NOTE!]
> **It does either necessary to represent the plan or not?** It must be answered! It sounds like plan. However, question CQ51 sounds like retrospective graph. The problem with interpreting this sounds like a plan is the word "ensure". A plans do not ensure! Even retrospective provenance: it does not ensure too.

> [QUESTION?]
> Do 

Despites of it might induces this question is concerned about existing plans, ruling the deletion of no longer necessary data, we assume it more about the retrospective information.   t This question seems not concerned about whether it exists plans that deletes data 


The procedures in question seem require for mechanisms that ensure the data is deleted once the purposes for which it was collected has been achieved. These mechanisms may be instantiated is a variable ways: a garbage collector for data without valid purposes or a publisher-subscriber service that watches and deletes data with outdated purposes.



Regardless of who these procedures in question take place, we must be able to represent the effect of a data that no longer holds 

Due to this variability of how these procedures can take place, we must avoid to specifically represent the steps involved. The GDPRov already provides the elements that represent the case of deleting data; and, in Q08, we introduce those elements to describe the retention policies.



Hence, to properly address this question, we should take into account the calcul

When approching this question, Pandit points two issues: first, how to evaluate programmatically whether the purposes for which data was collected has been achieved? Second, how to evaluate whether the data was deleted at the correct time? He recomends to consider the instance-level graph, despite his admission of the question complexity.

Starting by the last Pandit's issue, the calculus whether the data was deleted at the correct time depends on the time the purposes for which data was collected has been achieved, which depends on the storage condition under which the data is submitted. In Q08, we introduce four cases of storage condition: Data can be retained for a fixed period (e.g., 3 years), for fixed date achieves (e.g., 3 december 2033), after purpose (e.g., during the period the subject is a employee), or indefinite.

- The question `how to evaluate programmatically whether the purposes for which data was collected has been achieved?` certainly requires to consider the retention policies introduced in Q08. If the data is ruled by a retention police like a `fixed period`, it's necessary to take into account the start/end time of the activity involved in collect the data. If the retention police is for a `fixed data`, we should consider the calendar; if it is `after some purpose`, we need an extra vocabulary to express this idea (maybe it's time of using SSN and SASA ontology?).


- The question `how to evaluate whether the data was deleted at the correct time?` we should to consider the time when the purposes for which data was collected has been achieved and the deletion time.

(the time of which the purposes for which data was collected has been achieved) -> time:before -> (the time of the deletion process ended);
    initiated -> (deletion process)

retention policies and procedures

ensure data are held

no longer than is necessary for the purposes for which they were collected

## Related Work Comparison




----

By approaching this question, Pandit highlights the difficult to programmatically verify whether the data has been deleted by an automated procedure when the purpose for which it was collected has been fulfilled.

It seems to me his position lies in the detection of whether the purpose for which the data was collected is no longer necessary. However, we can argue that such an event must occur at the same time as the expiry of the legal basis for which the data was initially collected. In other words, we can unite purpose and legal basis.

Does it make sense to separate these two concepts in this context? See how the literature approach this discussion. See also the DPV. The definitions in DPV.


## Extending the model
## The Query
## Evaluation