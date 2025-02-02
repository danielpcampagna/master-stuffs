Durante a fase de construção da base de dados (SAPOS + TCD Privacy Policies) para validação da abordagem, foi detectado um erro da primeira base utilizada para validação. Dentre os erros, listamos a seguir.

## 1. Uso incorreto de propriedades domain e range

No primeiro exemplo criado para avaliação, foram utilizadas **classes** como sujeito e objetos das propriedades `rdfs:domain` e `rdfs:range`, respectivamente; todavia, a definição destas propriadades estabelece que o sujeito e o objeto das triplas que utilizam esta relação sejam instâncias das classes utilizadas na sua definição[^1].

E.g., no arquivo `queries/questions/CQ08/database.ttl`, a partir da linha 86, encontramos a seguinte tripla definida:

```turtle
prox:PersonalDataCollectionProcess rdf:type gdprov:HandleDataCollectionProcess ;
    gdprov:hasStorageCondition [
        rdf:type gdprov:StorageCondition ;
        gdprov:hasDuration prox:12monthsDuration ;
    ] .
```

Sendo que `gdprov:hasStorageCondition`, no GDPRov, é definido como uma propriedade:

```turtle
:hasStorageCondition rdf:type owl:ObjectProperty ;
                    rdfs:subPropertyOf owl:topObjectProperty ;
                    rdfs:domain :Process ;
                    rdfs:range :StorageCondition ;
                    rdfs:comment "Indicates the conditions required or followed regarding storage of data"@en ;
                    rdfs:label "has Storage Condition" ;
                    rdfs:isDefinedBy dpv:hasStorageCondition .
```

## 2. Nova subclasse ou nova instância?

Outra decisão que constantemente se fazia presente era a decisão sobre se um determinado sujeito deveria ser uma subclasse ou uma instância de uma classe anteriormente definida.

Para citar um exemplo, considere o sujeito `:StudentEnrolmentRecord`, que especifica um **grupo** de registros[^2]. Se por um lado não faz sentido criar diferentes instâncias desta classe (o que sugeriria tratá-lo como uma intância de `:RecordSeries`); por outro lado, é possível representar esta entidade também como uma classe cujos registros (i.e., `:Records`) específicos (ID do aluno, nome, etc) herdam.

Outro exemplo que também elucida este desafio são as instâncias ou subclasses de `:RetentionPeriod`, que especificam o período de retenção de um registro antes que uma decisão final seja tomada. Se tratamos, por exemplo, `:RetainForDurationOfStudiesPlus3Years` (i.e., o período de retençao durante os estudos mais três anos) como uma instância, perdemos a possibilidade de expressar as particularidades de cada instanciação (i.e., a data de início e fim); por outro lado, se tratamos este sujeito como uma classe, como seria possível explicitar sua política de duração (i.e., dura até que um evento aconteça, até uma data final, ou durante um período fixo)?

Noy e McGuinness [^3], ao lidarem com este tipo problema, propõem duas regras para auxiliar na tomada de decisão. A primeira regra vai de encontro direto com o primeiro exemplo trazido, pois diz que:

> [!HINT] Regra 1 (Noy e McGuinness)
> instâncias individuais são os conceitos mais específicos representados numa base de dados.

A partir dessa regra, decidimos modelar `:StudentEnrolmentRecord` como uma instância, pois de fato ele é o menor conceito que precisa ser representado.

Para decidir sobre o segundo exemplo trazido, valeu-nos tanto esta primeira regra quanto a segunda, que diz que:

> [!HINT] Regra 2 (Noy e McGuinness)
> se os conceitos formam uma hierarquia natural, então eles devem ser representados como classes.

Nos pareceu claro que o conceito `:RetainForDurationOfStudiesPlus3Years` pode possuir instâncias particulares para representar o período de duração de um conjunto de registros específico (e.g., informações pessoais de graduandos e pós-graduandos que não são mantidos pela Academic Registry). Com isso, aplicamos ambas as regras notarmos que há uma hierarquia natural existente entre este conceito e o conceito `:RetentionPeriod`.

Por fim, aplicando a metodologia sugerida, modelamos `:StudentEnrolmentRecord` como uma **instância** e `:RetainForDurationOfStudiesPlus3Years` como uma **subclasse** de `:RetentionPeriod`. Esta modelagem, contudo, introduziu alguns problemas que precisam lidar, sendo o principal deles a decisão de como conectar o período de retenção (uma classe) com uma instância [de `:RecordSeries`]?

A propriedade que foi proposta para realizar a conexão entre esses dois conceitos (i.e., `:hasRetentionPeriod`), foi desenhada para ligar duas instâncias. Nosso problema, contudo, consiste em termos uma instância e uma classe.

## 3. Utlizar versões graficas para modelar (e integrar com o GDPRov) a política privacidade da TCD

Durante a construção (e integração com o GDPRov) do modelo da política de privacidade da TCD, encontramos algumas decisões de modelagem difíceis de serem tomadas. Para auxiliar nessas decisoes, encontramos na representação gráficas (Graffoo[^4]) uma excelente ferramenta para facilitar a enxergar as possibilidades de modelagem, as consequências de cada decisão e a arguição sobre a decisão de modelagem tomada.

## 4. Mudança de classe para instância de `gdprov:EndlessDuration`

Outra mudança dentro desta categoria de classe-instância foi a da classe `gdprov:EndlessDuration` do modelo proposto. Inicialmente, este sujeito foi proposto para ser uma classe, todavia, aplicando as regras proposta por Noy e McGuinness [^3], não faz sentido instâncias ou subclasses desse sujeito. Logo, mudamos para que este seja uma instancia.

> [!TODO]
> Visto que detectamos esse problema ao fazer o desenho do modelo, talvez seja uma boa ideia fazer o desenho de todo o modelo, buscando esses tipos de mudanças.

## 5. Por que o GDPRov modela a relação de período de retenção de um dado específico através de um processo e não diretamente com o dado?

O GDPRov segue a modelagem proposta pelo **[Data Privacy Vocabulary](https://harshp.com/research/publications/035-representing-activities-processing-personal-data-consent-semweb-gdpr-compliance#sec:intro:dpvcg)** (DPV) para construir a relação entre um dado e sua política de retenção (`:StorageCondition`). O DPV é orientado para descrever as dimensões (o que, como, onde, por que, etc.) de um dado pessoal e seu processamento[^5].

Nessa modelagem, a informação do período de retenção de qualquer dado é obtida indiretamente através do processamento deste dado. ==A vantagem desta abordagem está no ganho de representatividade de vários períodos de retenção para um mesmo (tipo de) dado== (a depender da maneira como ele será manuseado, os propósitos para seu uso, etc.).

O conflito desta escolha de modelagem surge quando o GDPRov precisa ser usado para modelar um caso de uso onde esta informação (do período de retenção) é associada diretamente com o dado. Portanto, uma vez que o GDPRov foi criado modelando uma relação indireta entre o dado e seu período de retenção, através do processamento, [[Notas obtidas durante o processo de construção da base de validação#6. Como o GDPRov pode ser usado para modelar ontologias que conectam o período de retenção diretamente com o [tipo do] dado pessoal?|como o GDPRov pode ser usado para representar um caso onde essas informações são modeladas diretamente?]]

## 6. Como o GDPRov pode ser usado para modelar ontologias que conectam o período de retenção diretamente com o [tipo do] dado pessoal?

Não seria o caso de modelos que realizam esta conexão de forma direta modelos que visam representar políticas de privacidade enquanto que modelos que representam indiretamente são para representar o uso?

A [Tabela 3.3](https://harshp.com/research/publications/035-representing-activities-processing-personal-data-consent-semweb-gdpr-compliance#table:sota:analysis:process-flow) (na coluna **St**) do trabalho do Pandit (2020) mostra que apenas alguns trabalhos da literatura representa o conceito de `data storage`. Logo, podemos verificar como esses trabalhos realizam essa representação.

![[Pandit2020a-Table3.3.png]]

### Análise da literatura

A [[#^Tabela1|Tabela 1]] mostra o resultado desta análise. As subseções seguinte apresentamos mais detalhadamente cada abordagem.

| Abordagem     | Direta | Indireta |
|---------------|--------|----------|
| SPECIAL       |        | ✓        |
| SPL+CitySPIN  |        | ✓        |
| MIREL         | ?      | ?        |
| MRL+DAPRECO   | ?      | ?        |
| Ujcich et al. | X      | X        |
| Tom et al.    | X      | X        |
| Sion et al.   | ?      | ?        |
| RestAssured   | ?      | ?        |
^Tabela1
#### Abordagens
##### SPECIAL

A linguagem de política de privacidade do SPECIAL faz uma relação indireta entre ambos. A linguagem provê conceitos para descrever os atributos de um conjunto de *autorizações* (`slp:Authorization`), sendo estes: 

- the data processed by the operation;
- the purpose of the operation;
- a description of the operation itself (e.g. “query”, “classification”, “disclosure”, etc.);
- a description of where the result is stored and for how long;
- the entities that can access the result of the operation (recipients).

> [!INFO] EXEMPLO 1: Example of an abstract policy
> A policy P allows to disclose the file John_Smith_profile.jsonld to company ACME for commercial purposes iff a corresponding authorization
> 
> ```
> <John_Smith_profile.jsonld, CommercialPurpose, disclose, null, ACME>
> ```
> 
> belongs to `P`.
> 
> ---
> 
> Source: https://ai.wu.ac.at/policies/policylanguage/#ex1



A data subject’s consent comprises a usage policy; the authorizations contained in that policy are the operations allowed by the data subject. Dually, the usage policy enforced by a data controller contains the operations that are permitted within the data controller’s organization.

Therefore, the usage policy adopted by the data controller (call it `Pc`) complies with the usage policy in the data subject’s consent (call it `Ps`) if and only if all the authorizations in `Pc` are also authorized by `Ps`, that is, `Pc` complies with `Ps` if and only if

```math
Pc ⊆ Ps (Eq1)
```

Now we have to define a policy language where this kind of policies can be modelled precisely and unambiguously, possibly by representing large sets of authorizations (tuples) in a concise way. Such policy language should be equipped with an inference engine capable of checking reliably and exhaustively whether policy containments such as [(Eq1)](https://ai.wu.ac.at/policies/policylanguage/#eq1) hold, whenever `Pc` and `Ps` are expressed with the policy language. These are the goals of the next sections.

###### Storage Policy
- seeAlso: [The SPECIAL Usage Policy Language (wu.ac.at)](https://ai.wu.ac.at/policies/policylanguage/#storage)

The `hasStorage` policy attribute is a structured object itself, with two attributes, and is specified as follows (Eq3):

```
ObjectIntersectionOf(
    ObjectSomeValuesFrom(spl:hasLocation SomeLocation)
    ObjectSomeValuesFrom(spl:hasDuration SomeDuration)
    DataSomeValuesFrom(spl:durationInDays Interval)
)
```

In this expression, _SomeLocation_ and _SomeDuration_ are expressed in terms of the corresponding storage location and duration auxiliary vocabularies. It is not necessary to include in the policy both `hasDuration` and `durationInDays`. However at least one of them should be specified. The _Interval_ limiting storage duration in days is expressed with the integer facets of OWL2, that is (Eq4):

```
DatatypeRestriction( xsd:integer
xsd:minInclusive min duration          (optional)
xsd:maxInclusive max duration          (optional)
)
```

In this expression, _min_ and _max_ durations follow the syntax of `xsd:integer`. Note that here we are choosing days as the finest granularity for the shake of simplicity, but any standard mapping from dates to integers could be used, e.g. the one used in Unix-like systems.

##### SPL+CitySPIN

Não apresenta nenhuma diferença em relação à politica de retenção do SPECIAL. Apenas extende as classes de dados, processamento e propósito do SPECIAL.

##### MIREL

Desenvolve o [[PrOnto]], a aprtir do [Akoma Ntoso format]([Schema | Akoma Ntoso](http://www.akomantoso.org/?page_id=47)), que é um formato utilizado para descrever leis, decisões, opiniões, doutrinas, etc. Apesar de estar na tabela, não encontramos o modelo final[^6]. Nas publicações, não encontramos nenhuma informação de que tal modelo representa a política de armazenamento.

##### MRL+DAPRECO

Por utilizar o [[Notas obtidas durante o processo de construção da base de validação#MIREL|MIREL]] para abordar o GDPR na representação, não é possível fazer esta análise.

##### Ujcich et al.

Não modela a política de retenção nem direta nem indiretamente.

##### Tom et al.

A abordagem representa não representa o período de retenção de um dado.

##### Sion et al.

O autor cita, no seu artigo, que o período de retenção do armazenamento dos dados é um requisito da lei, porém o modelo não informa como esta relação é modelada. Ademais, o artigo não informa o endereço para acessar o modelo.

O meta-modelo publicado não mostra haver qualquer conceito para representar esta informação referente ao período de retenção.

##### RestAssured

Idem. A abordagem parece ter sido descontinuada. Todos os entregaveis não estão acessíveis e os artigos citados não apresentam como a relação entre o dado e a sua política de armazenamento se dá.


#### Conclusão

A [[#Abordagens|literatura]] tem apresentado pouca contribuição quando precisamos consutá-la para saber como é possível modelar a relação entre o dado e sua política de retenção. Em nossa análise, a maioria dos modelos não foram possíveis de serem verificados, pois tal modelagem não era descrita nos artigos e os modelos não estão acessível [através do artigo]. Outros casos, como [[#Ujcich et al.]] e [[#Tom et al.]], foram possíveis de se verificar que não modelam este tipo de relação.

Apenas o modelo [[#SPECIAL]] foi possível verificar e modela este tipo de relação. Conforme mostra a [[#^Tabela1|Tabela 1]], o [[#SPECIAL]] usa uma relação indireta entre o dado e o seu período de retenão.

### Decisão de modelagem

A partir dos resultados obtidos na [[Notas obtidas durante o processo de construção da base de validação#Análise da literatura|análise da literatura]], vimos que 

## 7. Adição de conceitos artificiais

![[Pasted image 20231113093909.png]]
Figura 1: Periodo de retenção dos dados pessoais de Alice no modelo TCD-SAPOS + GDPRov.

A modelagem acima é o 

![[Pasted image 20231113094111.png]]

# Footnotes e references

[^1]: [RDF 1.2 Schema [(w3.org)](https://www.w3.org/TR/rdf12-schema/#ch_domain)
[^2]: Traduzido de "General classes of records held", a primeira coluna da tabela do documento [[Records Management Policy_Records Retention Schedule.pdf|Records Management Policy Records Retention Schedule]].
[^3]: [Ontology Development 101: AGuide to Creating Your First Ontology (corais.org)](https://corais.org/sites/default/files/ontology_development_101_aguide_to_creating_your_first_ontology.pdf#page=20)
[^4]: [Graffoo - Graphical Framework for OWL Ontologies [(essepuntato.it)](https://essepuntato.it/graffoo/)
[^5]: [DPV Examples [(w3c.github.io)](https://w3c.github.io/dpv/examples/#E0011)
[^6]: O texto aponta que o PrOnto foi publicado atraveis de entregaveis neste endereço: [MIREL - Publications (mirelproject.eu)](https://www.mirelproject.eu/publications.php). Todavia, ao acessar [este entregável]([D2.4.pdf (mirelproject.eu)](https://www.mirelproject.eu/publications/D2.4.pdf)), que descreve esta ontologia, na página 10 há uma nota de roda pé indicando [este endereço](https://github.com/guerret/lu.uni.dapreco.parser/blob/master/resources/pronto-v8.graphml) onde supostamente a ontologia está publicada. Todavia, ao acessar o link, obtemos um 404.