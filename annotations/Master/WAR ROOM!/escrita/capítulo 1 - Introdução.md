Link [aqui](https://www.overleaf.com/project/61cc5c66ea9d235f253f9771
)

- Metodologia:
	- Algumas referencias boas para construção de ontologia ([aqui]())
	- Metodologia que usamos: [UPON Lite](https://scholar.google.com/scholar?q=De%20Nicola,%20Antonio,%20and%20Michele%20Missikoff.%202016.%20%E2%80%9CA%20Lightweight%20Methodology%20for%20Rapid%20Ontology%20Engineering.%E2%80%9D%20Communications%20of%20the%20ACM%2059%20(3):%2079%E2%80%9386.%20https://doi.org/10/gftgpt.) Fast and simple.
	- Methdologia

	The process for developing the ontology is based on (Gharib et al., 2021), and it follows the five principles proposed in (Gruber, 1995) (i.e., clarity, coherence, extendibility, minimal encoding bias, and minimal ontological commitment). The process is composed of the following five consecutive steps:

	**1. Scope & objective identification** aims at identifying the scope and the purposes for which the ontology will be developed. As discussed earlier, such ontology needs to provide concepts and relationships that allows a DS to express its privacy requirements by defining a PPPr in terms of PPPo, which should be written in a way that allows matching them with notices. Existing ontologies miss key privacy concepts and relationships to achieve that. Therefore, there is a need for developing such an ontology to solve the aforementioned problems

	**2. Knowledge acquisition** aims at collecting knowledge needed for the development of the required ontology. Kurteva et al. (Kurteva et al., 2020) provided an extensive literature survey concerning existing ontologies for modeling and implementing consent. Therefore, we analyzed these ontologies (e.g., CDMM (Fatema et al., 2017), PrOnto (Palmirani et al., 2018), LloPy (Loukil et al., 2018), GConsent (Pandit et al., 2019), ColPri (Toumia et al., 2020)) aiming at identifying the concepts and relationships required for developing our ontology. Although these ontologies have the potential to model informed consent, they are somewhat generic, developed for specific use cases or areas (Kurteva et al., 2020). Moreover, most of these ontologies do not cover several key concepts related to informed consent and notice, and most importantly, they were not designed to consider the possibility of matching PPPo with notice as this is out of their scope. To cover these important aspects, we enrich the concepts/relationships of our ontology with concepts/relationships identified in sections 4 and 5.

	**3. Conceptualization** aims at developing the ontology based on the key concepts and relationships identified in the previous step. A detailed description of the resulting ontology is provided in section 6.2.
	
	**4. Implementation** aims at codifying the ontology in a formal language. We have used Prot´eg´e5 to implement a preliminary version of the ontology. Prot´eg´e is open-source and domain-independent ontology design software, which has been proven to be one of the best tools to develop ontologies. A detailed description of the ontology implementation is provided in section 6.3.
	
	**5. Validation** aims at assuring that the resulting ontology meets the needs of its usage, i.e., checking whether the ontology captures enough detailed knowledge about the targeted domain to fulfill the needs of its intended usage. This can be done relying on Competency Questions (CQs), which represent a set of queries that the ontology must be capable of answering to be considered competent for conceptualizing the domain of discourse (Gharib et al., 2020). The validation of the ontology is out of the scope of this paper, but it is on our list for future work.
- 