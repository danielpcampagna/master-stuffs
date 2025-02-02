- source [[Noy and McGuiness, 2001]]

[**Ontology development 101**: A guide to creating your first **ontology**](https://corais.org/sites/default/files/ontology_development_101_aguide_to_creating_your_first_ontology.pdf)

## Why develop an ontology?
In recent years the development of ontologies—explicit formal specifications of the terms in the domain and relations among them (Gruber 1993)—has been moving from the realm of Artificial-Intelligence laboratories to the desktops of domain experts. Ontologies have become common on the World-Wide Web. The ontologies on the Web range from large taxonomies categorizing Web sites (such as on Yahoo!) to categorizations of products for sale and their features (such as on Amazon.com). The WWW Consortium (W3C) is developing the Resource Description Framework (Brickley and Guha 1999), a language for encoding knowledge on Web pages to make it understandable to electronic agents searching for information. The Defense Advanced Research Projects Agency (DARPA), in conjunction with the W3C, is developing DARPA Agent Markup Language (DAML) by extending RDF with more expressive constructs aimed at facilitating agent interaction on the Web (Hendler and McGuinness 2000). Many disciplines now develop standardized ontologies that domain experts can use to share and annotate information in their fields. Medicine, for example, has produced large, standardized, structured vocabularies such as SNOMED(Price and Spackman 2000) and the semantic network of the Unified Medical Language System (Humphreys and Lindberg 1993). Broad general-purpose ontologies are emerging as well. For example, the United Nations Development Program and Dun & Bradstreet combined their efforts to develop the UNSPSC ontology which provides terminology for products and services (www.unspsc.org). An ontology defines a common vocabulary for researchers who need to share information in a domain. It includes machine-interpretable definitions of basic concepts in the domain and relations among them.
Why would someone want to develop an ontology? Some of the reasons are:

* To share common understanding of the structure of information among people or software agents 
* To enable reuse of domain knowledge
* To make domain assumptions explicit
* To separate domain knowledge from the operational knowledge
* To analyze domain knowledge Sharing common understanding of the structure of information among people or software agents is one of the more common goals in developing ontologies (Musen 1992; Gruber 1993). provide medical e-commerce services. For example, suppose several different Web sites contain medical information or If these Web sites share and publish the same underlying ontology of the terms they all use, then computer agents can extract and aggregate information from these different sites. The agents can use this aggregated information to answer user queries or as input data to other applications.

*Enabling reuse of domain knowledge* was one of the driving forces behind recent surge in ontology research. For example, models for many different domains need to represent the notion of time. This representation includes the notions of time intervals, points in time, relative measures of time, and so on. If one group of researchers develops such an ontology in detail, others can simply reuse it for their domains. Additionally, if we need to build a large ontology, we can integrate several existing ontologies describing portions of the large domain. We can also reuse a general ontology, such as the UNSPSC ontology, and extend it to describe our domain of interest.

*Making explicit domain assumptions* underlying an implementation makes it possible to change these assumptions easily if our knowledge about the domain changes. Hard-coding assumptions about the world in programming-language code makes these assumptions not only hard to find and understand but also hard to change, in particular for someone without programming expertise. In addition, explicit specifications of domain knowledge are useful for new users who must learn what terms in the domain mean. 

*Separating the domain knowledge from the operational knowledge* is another common use of ontologies. We can describe a task of configuring a product from its components according to a required specification and implement a program that does this configuration independent of the products and components themselves (McGuinness and Wright 1998). We can then develop an ontology of PC-components and characteristics and apply the algorithm to configure made-to-order PCs. We can also use the same algorithm to configure elevators if we “feed” an elevator component ontology to it (Rothenfluh et al. 1996).

*Analyzing domain knowledge* is possible once a declarative specification of the terms is available. Formal analysis of terms is extremely valuable when both attempting to reuse existing ontologies and extending them (McGuinness et al. 2000).

Often an ontology of the domain is not a goal in itself. Developing an ontology is akin to defining a set of data and their structure for other programs to use. Problem-solving methods, domain-independent applications, and software agents use ontologies and knowledge bases built from ontologies as data. For example, in this paper we develop an ontology of wine and food and appropriate combinations of wine with meals. This ontology can then be used as a basis for some applications in a suite of restaurant-managing tools: One application could create wine suggestions for the menu of the day or answer queries of waiters and customers. Another application could analyze an inventory list of a wine cellar and suggest which wine categories to expand and which particular wines to purchase for upcoming menus or cookbooks.

---

# Usefulness of using semantic representation of processes
Source: https://link.springer.com/chapter/10.1007/978-3-030-33220-4_2
From: [[Pandit, Test-Driven Approach]], Introduction

Interoperable semantics are beneficial when information is shared between stakeholders such as - controllers and processors, or controllers and certification bodies or supervisory authorities. The interoperability is also helpful towards transparency regarding processing activities to address the discrepancy between requirements of an organisation and compliance [18]. A discussion of four areas where automation can be applied [7], one of which is compliance using checklists, shows possible avenues for further incorporating semantics into the compliance process.

## References

[18] Schiffner, S., et al.: Towards a roadmap for privacy technologies and the general data protection regulation: a transatlantic initiative. In: Medina, M., Mitrakas, A., Rannenberg, K., Schweighofer, E., Tsouroulas, N. (eds.) APF 2018. LNCS, vol. 11079, pp. 24–42. Springer, Cham (2018). [https://doi.org/10.1007/978-3-030-02547-2_2](https://doi.org/10.1007/978-3-030-02547-2_2)

[7] Kingston, J.: Using artificial intelligence to support compliance with the general data protection regulation. Artif. Intell. Law **25**(4), 429–443 (2017). https://doi.10/gfxvtc, [https://doi.org/10.1007/s10506-017-9206-9](https://doi.org/10.1007/s10506-017-9206-9)
