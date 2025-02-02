A metodologia utilizada para desenvolver o GDPRov foi desenvolvido usando uma mesca de três metodologias.[^1]

De forma breve, o autor utilizou uma metodologia geral e introdutória ([Ontology Development 101](https://corais.org/sites/default/files/ontology_development_101_aguide_to_creating_your_first_ontology.pdf)) para entender e iniciar o processo de construção da ontologia. Em seguida, passou a usar uma combinação da metodologia [NeOn](https://www.academia.edu/download/96971442/9783642247934-c1.pdf) com a [UPON Lite](https://dl.acm.org/doi/fullHtml/10.1145/2818359#body-1). A primeira foi usada para identificar os cenários e definir os requisitos que deveriam estar presentes no modelo. A última o autor usou para derivar as tarefas necessárias para construir e testar a ontologia, usando um processo de desenvolvimento ágil.

Ao final, a metodologia usada na construção do GDPRov contou com os seguintes passos:

1. Identificação de objetivos, metas, escopo
2. Identificar e analisar informações relevantes
3. Criar casos de uso e questão de competência
4. Identificar conceitos e relacionamentos
5. Criar Ontologia
6. Avaliar
7. Iterações progressivas seguindo os passos 2 a 6
9. Disseminação

Para a tarefa de evolução do GDPRov, os passos 1-3 devem ser idênticos aos introduzidos pelo modelo original, uma vez que se trata do mesmo modelo. E desde que o objetivo deste trabalho é evoluir o GDPRov (v0.7) de modo a ser capaz de responder às demais questões de competência que não foram respondidas, usamos, como metodologia, uma iteração progressiva entre os passos 4-6 para cada questão de competência a ser abordada.

No passo 4, identificamos os conceitos e as relações relevantes para expressar informações necessárias para responder a perguntas de conformidade em questão. Fizemos uma análise desses termos apresentando utilizando outras fontes.

No passo 5, ao propor classes e relacionamentos para representar os conceitos identificados no passo 4, buscamos, antes, verificar referências em trabalhos relacionados e outras modelos, elemntos que já carregavam um significado semelhante. Além disso, foram propostas representações das questões de conformidade em consultas SPARQL utilizando esses novos elementos do modelo. 

Para avaliar a proposta, imposta pelo passo 6, buscamos aplicar as consulltas no passo anterior numa base real em RDF. Essa base foi construída a partir de um esquema do banco de dados do SAPOS[^3] tendo como guia a política de privacidade da Trinity College Dublin.[^4] 
# Referêcia

[^1]:  Aqui deixo a referência da descrição da metodologia utiliada na construção do GDPRov: https://harshp.com/research/publications/035-representing-activities-processing-personal-data-consent-semweb-gdpr-compliance#sec:intro:ontology-engineering
[^2]:  It also suggested use of competency questions to determine scope of an ontology and for evaluation after creation.