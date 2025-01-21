# CQ63

Are all transfers listed - including answers to the previous questions (e.g. the nature of the data, the purpose of the processing, from which country the data is exported and which country receives the data and who the recipient of the transfer is?)

## Discussion

This question is scoped to the legality of international transfers. Pandit just states this question cannot be evaluated programmatically, without providing further argumentation for that position. However, we argue that it is not the case, since we can capture the provenance data related to the international transfers. This position is supported by the comment of Pandit in the CQ64, which belongs to this same scope. On CQ64, he made clear the capability of provenance in addressing this kind of question.

Therefore, this question is already addressed by previous questions, since those ones already list all information related to the transfer procedures. To be more specific, we might filter the queries of the previous question by considering only activities and processes related to the transfers.

For example, considering question CQ01 (also known as G1), instead of the following query (as proposed by Pandit at <https://openscience.adaptcentre.ie/GDPR-checklist-demo/demo/>):

```sparql

SELECT DISTINCT ?category where {
    ?category rdfs:subClassOf gdprov:PersonalData .
    FILTER(regex(str(?category), "http://example.com/ontology/shoppingapp#")) .
} ORDER BY ?category

```

We might use as following:

```sparql

SELECT DISTINCT ?category ?thirdParty where {
    ?category rdf:type/rdfs:subClassOf+ gdprov:PersonalData .
    ?category gdprov:isSharedWithThirdParty ?thirdParty .
} ORDER BY ?category ?thirdParty

```


## Related Work Comparison
## Extending the model
## The Query
## Evaluation

We cannot evaluate this question within SAPOS.

# Footnote
# References