## Diferentes ontologias para diferentes fins
- Tenho notado que existe uma ontologia para cada tipo de coisa:
	- Um primeiro tipo visa observar as relações deônticas (permissão, violação, direito, etc) entre os agentes, as entidades e as atividades (e.g., [[Data Privacy Vocabulary|DPV]], [[Elluri, 2018a]]);
	- [[GConsent]] visa representar os estados do consentimento;
	- [[GDPRov]], [[Besik, 2019a]] visa representar as atividades, os processamentos e os fluxos dos dados;

- De fato, algumas abordagens chegam a propor o use de três tipos de ontologia ([[Besik, 2019a]]):
	- uma para representar os processos do sistema (e.g., manipulação dos dados); e a partir dessa
	- outra para representar as relações deônticas entre os recursos e sistemas envolvidos (essas relações tanto no nível de políticas de privacidade legais quanto do negócio); e
	- uma última para representar as entidades, agentes e processos relacionados ao contexto do negócio.

## Sobre o uso de modelos da literatura
- O fato é que existem muitas ontologias bastante ricas e expressivas para vários propositos. A pergunta principal é: **Com o que eu posso contribuir?**
	- Eu estava seguindo pelo caminho de tentar propor uma extensão ao modelo do [[Ujcich et al]].
		- O grande differencial do modelo do [[Ujcich et al]] parece que é a dissociação da entidade que representa o dado pessoal (i.e., PersonalData) com a ação que representa a justificativa para um processo ser considerado legal (ie, Justify) (isso traz alguma vantagem?). No restante, ele parece (ou pode ser) tão representativo quanto o modelo do Pandit.
		- O argumento que usei em favor do modelo do [[Ujcich et al]] é sua capacidade de representar outras bases legais para o processamento (algo que o [[GDPRov]] não é capaz).
		- Todavia, a ontologia [[Data Privacy Vocabulary|DPV]] é capaz de representar essas outras bases legais, além disso, esta parece ser mais utilizada, visto ter sido criada e mantida por uma comunidade.
		- Logo, é preferível abandonar o modelo do [[Ujcich et al]] e utilizar o [[Data Privacy Vocabulary|DPV]] em seu lugar.
		- O ponto, agora, é saber quais as diferenças entre o [[Data Privacy Vocabulary|DPV]] e o modelo do [[GDPRov|Pandit]]. De fato, essa discussão foi iniciada em [[Comparing DPV with GDPRtEXT, GDPRov, and GConsent]]. O próximo passo é verificar se a versão que o Pandit critica do DPV e a versão atual deste essas criticas ainda permanecem ou não. Outra forma de avaliar (e talvez mais precisa, uma vez que o Pandit não é específico em dizer quais são de fato os componentes que a ontologia dele apresenta que o DPV não o faz) é verificar direto no Readiness Checklist se o DPV é suficiente para responder as research questions.
		- Um ponto importante a se verificar (algo que defato o Pandit destaca como sendo a sua principal contribuição) é se o modelo DPV cobre planos (IPA) 

## Onde posso contribuir?
De fato, apesar de tantas abordagens, é possível perceber, rapidamente, que elas não são completas em si. Nisso entraria minha contribuição: pegar o melhor de cada abordagem e tentar unificá-las, trazendo o melhor de cada um dos mundos.
1. **Propor um novo modelo unificado** que reutiliza tanto as contribuições feitas no SBBD, quanto os demais modelos. Pois o modelo do [[Ujcich et al]] faz sentido (em relação ao [[Data Privacy Vocabulary|DPV]] e ao do [[GDPRov|Pandit]]), tanto por propor a ideia de Request para representar solicitações do sujeito que ainda não se concretizaram em consentientos quanto por permitir outros meios legais (algo que o modelo do [[GDPRov|Pandit]]) não permite. Contudo, dá pra fazer ligação dessas outras bases legais com o modelo do DPV fácilmente (e ainda ampliar com os conceitos que o próprio DPV já trás).
2. **Cobrir as lacunas do Readiness que o Pandit não foi capaz de cobrir** Além de ampliar o modelo, adicionando a capacidade de representar outros casos de usos além dos exigidos pelo documento Readiness, seria de bastante proveito conseguir representar casos que o modelo do Pandit não foi capaz de representar neste documento.
3. **Preencher as perguntas de compliance do outro documento semelhante ao Readiness** Sei que existe um outro documento do Readiness. Não sei quais são as questões de conformidade que contêm nele, mas seria interessante verificar se os modelos atuais (que vou unificar e extender) são capazes de representá-lo.

## Métodos para acelerar a revisão
1. Na tese do [[pandit, 2020, pdf.pdf]], na p. 36, ele agrupa suas publicações de acordo com o objetivo além de trazer um comentário sobre a publicação. Isso pode ser útil para acelerar a tomada de decisão se tal artigo deve ou não entrar na nossa revisão.
2. Além disso, nesse trabalho tbm existe uma boa revisão da literatura. Use-a para o mesmo fim!