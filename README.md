 # 🐍Relatório das eplicaçõs de cada atividade:

 🚀Exercício 1 (Pares e Ímpares): Usei o laço for com a função range(101) para iterar de 0 a 100. Dentro do laço, apliquei uma estrutura condicional if/else junto com o operador de módulo % para verificar se o resto da divisão por 2 era zero (par) ou não (ímpar).

🚀Exercício 2 (Maior e Menor): Recebi os dados via input(), converti para float() e os armazenei em uma lista. Para evitar vários if/elif, utilizei as funções integradas max() e min(), que identificam os extremos de um conjunto de dados.

⚙️Exercício 3 (Nome em Escada): Utilizei o laço for combinado com o conceito de slicing (fatiamento) de strings. Usei a função len() para definir o limite da repetição, fazendo com que o Python imprimisse fatias progressivas do nome a cada volta.

⚙️Exercício 4 (Fibonacci): Apliquei um laço for para repetir o cálculo do termo definido pelo input(). A lógica central foi a atribuição múltipla de variáveis (a, b = b, a + b), que permite atualizar os valores da sequência sem precisar de variáveis auxiliares temporárias.

⚙️Exercício 5 (Validação de Dados): Usei um laço while True (loop infinito) para garantir que o usuário continuasse digitando até acertar. Dentro dele, usei o if com operadores lógicos (como and e in) para validar se o nome, idade, salário e sexo estavam nos padrões. Quando tudo estava correto, usei o comando break para sair do laço.

🔨Exercício 6 (Número Primo): Além do for e do if, utilizei o operador % para testar divisões sucessivas. Criei uma variável contadora para registrar quantas vezes o número era divisível; se ao final do laço essa contagem fosse zero, o número era identificado como primo.

🔨Exercício 7 (Fatorial): Usei o laço for para realizar multiplicações acumuladas. Comecei com uma variável valendo 1 e, a cada iteração, usei o operador de atribuição composta (*=) para multiplicar o valor atual pelo próximo número da sequência.

🐍Exercício 8 (Operações com Lista): Trabalhei com uma Lista [] pré-definida. Para extrair as informações, usei funções nativas como len() (tamanho), sum() (soma total) e a função sorted() para organizar os elementos em ordem crescente e decrescente (usando o parâmetro reverse=True).

🐍Exercício 9 (Dicionário): Construí uma estrutura de Dicionário {}, que organiza os dados através de pares de "chave: valor". Isso permite simular uma tabela onde cada informação pode ser recuperada pelo seu nome identificador em vez de apenas pela posição.

🐍Exercício 10 (Acesso com Senha): Utilizei o laço while com uma condição de comparação (tentativa != senha_correta). O programa repete o input() indefinidamente e só exibe a mensagem de sucesso e encerra a execução quando a condição do laço se torna falsa.

🐍Exercício 11 (Tabuada): Usei o input() para receber o número base e um laço for que vai de 1 a 10. Dentro do laço, realizei a operação aritmética de multiplicação e usei f-strings no print() para exibir o relatório da tabuada de forma organizada.
