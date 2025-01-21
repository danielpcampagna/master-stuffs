# CQ64

Is there a legal basis for the transfer, e.g. EU Commission adequacy decision; standard contractual clauses. Are these bases documented?

## Discussion

This question is addressed by applying the query in CQ05 (G5), which has retrieved the legal basis for every processing, in every controllers who is part in this transferring.

Pandits, commenting this question, do not propose a answer arguing it depends on this query to be applied into each Controller graph. However, we could imagine that Data Protection Officer applies this query into a federated database system, which integrates multiple autonomous and heterogeneous provenance models and databases as whether they are a single one.

Starting from that assumption, the query related to this question is closed to the one presented by CQ05 (G5), it just has been necessary to explicit the Controllers involved in the transfers.

```sparql

SELECT DISTINCT ?process ?legal ?thirdParty ?involvedAgent where {
    ?data rdf:type/rdfs:subClassOf+ gdprov:PersonalData .
    ?step rdf:type/rdfs:subClassOf+ gdprov:DataStep .
    ?step gdprov:usesData ?data .
    ?step gdprov:isPartOfProcess ?process .

    OPTIONAL { ?step gdprov:sharesDataWithThirdParty ?thirdParty } .
    OPTIONAL { ?process gdprov:involvesAgent ?involvedAgent . } .
    OPTIONAL { ?process gdprov:hasLegalBasis ?legal . } .
} ORDER BY ?process

```

## Related Work Comparison
## Extending the model
## The Query
## Evaluation

We cannot evaluate this question within SAPOS, since it was not developed for fulfill this feature.

# Footnote
# References