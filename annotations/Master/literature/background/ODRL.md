---
aliases: [ODRL, ]
---
- similarAimsTo [[GDPRtEXT]]
- isA [[Deontic Ontology]]

# Open Digital Right Language
available in: https://www.w3.org/TR/odrl-model/

## Introduction

reference: https://www.w3.org/TR/odrl-model/

"The Open Digital Rights Language (ODRL) is a policy expression language that provides a flexible and interoperable information model, vocabulary, and encoding mechanisms for representing statements about the usage of content and services. The ODRL Information Model describes the underlying concepts, entities, and relationships that form the foundational basis for the semantics of the ODRL policies.

Policies are used to represent permitted and prohibited actions over a certain asset, as well as the obligations required to be meet by stakeholders. In addition, policies may be limited by constraints (e.g., temporal or spatial constraints) and duties (e.g. payments) may be imposed on permissions."

## Aims of the Model

reference: https://www.w3.org/TR/odrl-model/#aimsModel

"The primary aim of the ODRL Information Model is to provide a standard description model and format to express permission, prohibition, and obligation statements to be associated to content in general. These statements are employed to describe the terms of use and reuse of resources. The model should cover as many permission, prohibition, and obligation use cases as possible, while keeping the policy modelling easy even when dealing with complex cases.

The ODRL Information Model is a single, consistent model that can be used by all interested parties. A single method of fulfilling a use case is strongly preferred over multiple methods, unless there are existing standards that need to be accommodated or there is a significant cost associated with using only a single method. While the ODRL Information Model is built using Linked Data principles, the design is intended to allow non-graph-based implementations."

This approach can be used to link relevant text in GPDR, using RDF properties, similar to the aims of GDPRtEXT

## ODRL Profile

deontic concepts (permissions, prohibitions, obligations and dispensations)

---

ODRL is a method for checking compliance, it has a parallel meaning with [[OWL]], [[RuleML]], UML, Smart Contract, [[BPMN]], for example.

---

## Perguntas

- Qual a diferença deste para os demais (eg, DPV)