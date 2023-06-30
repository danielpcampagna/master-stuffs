## Resumo com relação ao problema de representação das questões de pesquisa

Este trabalho focou em apenas demostrar a factibilidade do uso de tecnologias de semantic web para ajudar na demonstração da conformidade. Dessa forma, todas as SPARQL queries devem ser submetidas ao escrutínio de uma avaliação de generalidade do modelo de base, até mesmo aquelas propostas pelo autor.

Nossa perguta se torna, então:

    1. Sobre a possiblidade de responder às demais questões (+fácil, -impacto)
    2. Demonstrar a generalidade dessas questões (-fácil, +impacto)

## Tabela das compliance questions atendidas

| ID | Type | Data | E/A | E/P | SPARQL | GDPRov |
|----|------|------|-----|-----|--------|--------|
| G1 | Demonstrative | personal data, data subjects | Y | N | Y | Y |
| G2 | Demonstrative | personal data | Y | N | Y | Y |
| G3 | Demonstrative | personal data, steps that collect data, entities that provide data | Y | Y | Y | Y |
| G4 | Demonstrative | results of G1, processes acting on data | Y | N | Y | Y |
| G5 | Demonstrative | results of G4, processes acting on data | Y | N | Y | Y |
| G6 | Demonstrative | special category personal data | Y | N | Y | Y |
| G7 | Demonstrative | results of G6, steps that collect data, steps that store data | Y | N | Y | Y |
| G8 | Not-Implemented | results of G1, steps that store data |  |  | N | N |
| G9 | Not-Implemented |  |  |  | N | S |
| P1 | Assistive | consent, steps that acquire consent | Y | N | Y | Y |
| P2 | Not-Implemented |  |  |  | N | S |
| P3 | Evaluative | consent | Y | Y | Y | Y |
| P4 | Evaluative | steps that withdraw consent | Y | N | Y | Y |
| P5 | Evaluative | steps that acquire consent, steps for age verification | Y | N | Y | Y |
| P6 | Assistive | steps that process personal data | Y | N | Y | Y |
| R1 | Assistive | steps that handle SAR | Y | N | Y | Y |
| R10 | Not-Implemented |  |  |  | N | S |
| R2 | Assistive | steps that handle SAR | N | Y | N | Y |
| R3 | Evaluative | steps that address right to data portability | Y | N | Y | Y |
| R4 | Evaluative | steps that address right to rectification | Y | N | Y | Y |
| R5 | Assistive | data subject request, steps that process personal data | N | Y | N | Y |
| R6 | Not-Implemented |  |  |  | N | Y |
| R7 | Evaluative | steps that process personal data | Y | N | Y | Y |
| R8 | Assistive | steps that make automated decisions, consent | Y | Y | Y | Y |
| R9 | Assistive | steps that make automated decisions, right to contest automated decisions | Y | N | Y | Y |
| A1 | Evaluative | personal data, consent, steps that involve personal data through use, share, store | Y | Y | Y | Y |
| A2 | Assistive | personal data, steps that process personal data | Y | Y | Y | Y |
| A3 | Not-Implemented |  |  |  | N | S |
| A4 | Not-Implemented |  |  |  | N | S |
| A5 | Not-Implemented |  |  |  | N | S |
| A6 | Assistive | steps that delete data | Y | N | Y | Y |
| A7 | Not-Implemented |  |  |  | N | S |
| T1 | Not-Implemented |  |  |  | N | S |
| T2 | Assistive | steps that collect personal data | Y | N | Y | Y |
| T3 | Assistive | steps that collect personal data | Y | N | Y | Y |
| T4 | Not-Implemented |  |  |  | N | S |
| T5 | Not-Implemented |  |  |  | N | S |
| C1 | Not-Implemented |  |  |  | N | S |
| C2 | Not-Implemented |  |  |  | N | Y |
| C3 | Not-Implemented |  |  |  | N | S |
| C4 | Not-Implemented |  |  |  | N | S |
| C5 | Not-Implemented |  |  |  | N | S |
| C6 | Assistive | steps part of the DPIA process | Y | N | Y | Y |
| S1 | Assistive | steps that process data | Y | N | Y | Y |
| S2 | Not-Implemented |  |  |  | N | S |
| S3 | Not-Implemented |  |  |  | N | S |
| S4 | Not-Implemented |  |  |  | N | S |
| S5 | Not-Implemented | steps that share data |  |  | N | N |
| S6 | Not-Implemented |  |  |  | N | Y |
| S7 | Not-Implemented |  |  |  | N | N |
| B1 | Evaluative | processes or plan that address security incidents | Y | N | Y | Y |
| B2 | Not-Implemented |  |  |  | N | S |
| B3 | Evaluative | processes or plans for notifying DPC | Y |  | Y | Y |
| B4 | Evaluative | processes or plans for notifying data subjects of a data breach |  |  | Y | Y |
| B5 | Not-Implemented |  |  |  | N | Y |
| B6 | Not-Implemented |  |  |  | N | S |
| I1 | Evaluative | steps that share data | Y | Y | Y | Y |
| I2 | Evaluative | results from I1, category of personal data | Y | N | Y | Y |
| I3 | Assistive | steps that share data | Y | Y | Y | Y |
| I4 | Evaluative | steps that share data | Y | Y | Y | Y |
| I5 | Not-Implemented |  |  |  | N | Y |
| I6 | Not-Implemented |  |  |  | N | Y |
| I7 | Not-Implemented | steps that share data |  |  | N | S |


## Descrição da cobertura do documento

"Of the total 63 questions within the GDPR readiness guide, 32 questions have corresponding SPARQL queries created and used in the demo. Of 31 questions that were not implemented, 20 questions were considered out of scope as they do not relate to the research question, with the other 3 questions lacking corresponding concepts in GDPRov to create SPARQL queries. Of these, question G8 concerning retention periods for personal data can be expressed using Time ontology (Cox and Little 2017). The other two, S5 and S7 require specification of information associated with information management and governance procedures utilised within an organisation. While these are technically not outside the scope of GDPRov, they require a larger understanding of how such processes are specified and managed and commonly involve use of specifications to denote practices - for example ISO/IEC 27001 describing a framework for information management and protection. Some questions not considered within scope concern information not associated with processing of personal data or consent, but which can be represented as activities using GDPRov. These include questions C1 concerning agreements between entities or question C4 concerning escalation procedures involving DPO."