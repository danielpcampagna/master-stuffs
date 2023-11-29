Durante a fase de construção da base de dados (SAPOS + TCD Privacy Policies) para validação da abordagem, foi detectado um erro da primeira base utilizada para validação. Dentre os erros, listamos a seguir.

### 1. Uso incorreto de propriedades domain e range

No exemplo criado para avaliação prévia, foram utilizadas **classes** como sujeito e objetos das propriedades `rdfs:domain` e `rdfs:range`, respectivamente; todavia, a definição destas propriadades estabelece que o sujeito e o objeto das triplas que utilizam esta relação sejam instâncias das classes utilizadas na sua definição[^1].

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

### 2. Nova subclasse ou nova instância?

Outra decisão que constantemente se fazia presente era a decisão sobre se um determinado sujeito deveria ser uma subclasse ou uma instância de uma classe anteriormente definida.

Para citar um exemplo, considere o sujeito `:StudentEnrolmentRecord`, que especifica uma "classe geral de registros"[^2]. Se por um lado não faz sentido criar diferentes instâncias desta classe (o que sugeriria tratá-lo como uma intância de `:RecordSeries`); por outro lado, a lista de `:Records` que serão incluídos será definida em tempo de execução do sistema, aumentando para cada novo aluno que for cadastrado no sistema.

Outro exemplo que também elucida este desafio são as instâncias ou subclasses de `:RetentionPeriod`, que especificam o período de retenção de um registro antes que uma decisão final seja tomada. Se tratamos, por exemplo, `:RetainForDurationOfStudiesPlus3Years` (i.e., o período de retençao durante os estudos mais três anos) como uma instância, perdemos a possibilidade de expressar as particularidades de cada instanciação (i.e., a data de início e fim); por outro lado, se tratamos este sujeito como uma classe, como seria possível explicitar sua política de duração (i.e., dura até que um evento aconteça, até uma data final, ou durante um período fixo)?

Noy e McGuinness [^3], ao lidarem com este tipo problema, propõem duas regras para auxiliar na tomada de decisão. A primeira regra vai de encontro direto com o primeiro exemplo trazido, pois diz que "*instâncias individuais são os conceitos mais específicos representados numa base de dados.*" A partir dessa regra, decidimos modelar `:StudentEnrolmentRecord` como uma instância, pois de fato ele é o menor conceito que precisa ser representado.

Para decidir sobre o segundo exemplo trazido, valeu-nos tanto esta primeira regra quanto a segunda, que diz que "*se os conceitos formam uma hierarquia natural, então eles devem ser representados como classes*." Nos pareceu claro que o conceito `:RetainForDurationOfStudiesPlus3Years` pode possuir instâncias particulares para representar o período de duração de um conjunto de registros específico (e.g., informações pessoais de graduandos e pós-graduandos que não são mantidos pela Academic Registry). Com isso, aplicamos ambas as regras notarmos que há uma hierarquia natural existente entre este conceito e o conceito `:RetentionPeriod`.

Por fim, aplicando a metodologia sugerida, modelamos `:StudentEnrolmentRecord` como uma **instância** e `:RetainForDurationOfStudiesPlus3Years` como uma **subclasse** de `:RetentionPeriod`. Esta modelagem, contudo, introduziu alguns problemas que precisam lidar, sendo o principal deles a decisão de como conectar o período de retenção (uma classe) com uma instância [de `:RecordSeries`]?

A propriedade que foi proposta para realizar a conexão entre esses dois conceitos (i.e., `:hasRetentionPeriod`), foi desenhada para ligar duas instâncias. Nosso problema, contudo, consiste em termos uma instância e uma classe.

### 3. Utlizar versões graficas para modelar (e integrar com o GDPRov) a política privacidade da TCD

Durante a construção (e integração com o GDPRov) do modelo da política de privacidade da TCD, encontramos algumas decisões de modelagem difíceis de serem tomadas. Para auxiliar nessas decisoes, encontramos na representação gráficas (Graffoo[^4]) uma excelente ferramenta para facilitar a enxergar as possibilidades de modelagem, as consequências de cada decisão e a arguição sobre a decisão de modelagem tomada.

# Footnotes e references

[^1]: [RDF 1.2 Schema (w3.org)](https://www.w3.org/TR/rdf12-schema/#ch_domain)
[^2]: Traduzido de "General classes of records held", a primeira coluna da tabela presente no documento [[Records Management Policy_Records Retention Schedule.pdf|Records Management Policy Records Retention Schedule]].
[^3]: [Ontology Development 101: AGuide to Creating Your First Ontology (corais.org)](https://corais.org/sites/default/files/ontology_development_101_aguide_to_creating_your_first_ontology.pdf#page=20)
[^4]: [Graffoo - Graphical Framework for OWL Ontologies (essepuntato.it)](https://essepuntato.it/graffoo/)