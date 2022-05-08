## mario_cesa_780_projeto_2

Os Dados
Utilizaremos um Dataset obtido do Twitter com 100K postagens entre os dias 01/08/2018 e 20/10/2018. Cada postagem é classificada como positiva, negativa ou neutra.

Dois arquivos serão disponilizados para o desenvolvimento dos modelos, um para treino/validação e outro para submissão. Os arquivos se encontram na pasta /Dados/train e /Dados/subm, respectivamente.

Descrição das colunas:

id: ID único para o tweet
tweet_text: Texto da publicação no Twitter
tweet_date: Data da publicação no Twitter
sentiment: 0, se negativo; 1, se positivo; 2, se neutro
query_used: Filtro utilizado para buscar a publicação

O Problema

Você deverá desenvolver um modelo para detectar o sentimento de uma publicação do Twitter a classificando em uma das três categorias: positiva, negativa ou neutra. O texto da publicação está disponível na coluna "tweet_text". Teste pelo menos 2 técnicas de NLP diferentes e escolha a métrica de avaliação que julgar mais pertinente.

Escolha o melhor modelo e gere uma base a partir dos dados de submissão, que estão no caminho Dados/subm/Subm3Classes.csv, com o seguinte formato:

id	sentiment_predict
12123232	0
323212	1
342235	2
Salve essa tabela como um arquivo csv com o nome <nome>_<sobrenome>_nlp_degree.csv e submeta-o como parte da entrega final do projeto.

Para ajudar no desenvolvimento, é possível dividir o projeto em algumas fases:

Análise de consistência dos dados: analise se os dados estão fazendo sentido, se os campos estão completos e se há dados duplicados ou faltantes. Se julgar necessário, trate-os.
Análise exploratória: analise a sua base como um todo, verifique o balanceamento entre as classes e foque, principalmente, na coluna tweet_text.
Pré-processamento e transformações: projetos de NLP exigem um considerável pré-processamento. Foque no tratamento da string do texto. Procure começar com tratamentos simples e adicione complexidade gradualmente. Nessa etapa você testará diferentes técnicas de transformações, como o Bag Of Words e o TF-IDF.
Treinamento do modelo: depois das transformações, você poderá executar o treinamento do modelo classificador. Nessa etapa o problema se torna semelhante aos abordados na primeira parte do módulo. Você pode testar diversos classificadores como RandomForest, AdaBoost, entre outros. Otimize os hiperparâmetros do modelo com técnicas como a GridSearch e a RandomizedSearch.
Conclusões: descreva, em texto, as conclusões sobre os seus estudos. O modelo é capaz de identificar o sentimento das publicações? É possível extrapolar o modelo para outros contextos, como a análise de sentimento de uma frase qualquer? Pense em questões pertinentes e relevantes que você tenha obtido durante o desenvolvimento do projeto!
Critérios de avaliação
Os seguintes itens serão avaliados:

Desenvolvimento das etapas descritas acima;
Reprodutibilidade do código: seu código será executado e precisa gerar os mesmos resultados apresentados por você;
Clareza: seu código precisa ser claro e deve existir uma linha de raciocínio direta. Comente o código em pontos que julgar necessário para o entendimento total;
Justificativa das conclusões obitdas: não existirá certo ou errado, mas as decisões e as conclusões precisam ser bem justificadas com base nos resultados obtidos.
O desempenho do modelo não será considerado como critério de avaliação.

Informações gerais
O projeto deve ser desenvolvido individualmente;
Data de divulgação: 11/01/2022;
Aula de monitoria: 19/01/2022;
Data de entrega: 26/01/2022;
Entrega através do Class: Árvore de Decisão -> Exercícios -> Projeto 2
Anexar, na entrega, o notebook de desenvolvimento e o arquivo .csv de submissão, da seguinte forma:

notebook: <nome>_<sobrenome>_<númeroTurma>_projeto_2.ipynb
csv: <nome>_<sobrenome>_<númeroTurma>_projeto_2_submissao.csv

Dicas
Base de treino e submissão
A base de submissão não possui a variável de saída, portanto ela será utilizada apenas para gerar o arquivo que acompanha a submissão do projeto.

Tente encontrar possíveis vieses
É muito comum que modelos de NLP possuam fortes vieses, como a tendência de relacionar palavras específicas com alguma classe de saída. Tente encontrar vieses no seu estudo, isso pode ajudar a tirar boas conclusões. o campo "query_used" pode ser útil para essa análise.

O pré-processamento é a chave para um bom desempenho
Essa é a etapa que mais vai contribuir para o desempenho do seu modelo. Seja criativo e desenvolva essa etapa de uma maneira que seja fácil de aplicar o mesmo processamento para uma nova base, você terá que fazer isso para gerar a base de submissão.

Um termômetro para o seu desenvolvimento
Após a correção do seu projeto, o professor irá disponibilizar a sua acurácia obtida na base de submissão. Você pode interpretar esse resultado como a simulação do resultado do seu modelo em produção. Uma diferença entre o resultado do estudo e o resultado de submissão indica um grau de overfitting no seu modelo.