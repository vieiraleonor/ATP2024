Neste exercio era pedido para criar em Python um jogo interativo de "Adivinhar o número". Este jogo tem 2 modos: MODO COMPUTADOR, no qual consiste no computador gerar um número aleatório e o jogador tenta o adivinhar, e o MODO NORMAL, onde o jogador pensa num número e o computador tenta adivinhar. 

### 1. **Menu:**
O jogo começa apresentando um menu com três opções:

- **Opção 1:** Modo Computador – o jogador tenta adivinhar o número.
- **Opção 2:** Modo Normal – o computador adivinha o número do jogador.
- **Opção 0:** Sair – para encerrar o jogo.

A escolha do modo é feita por meio de um `input`, armazenado na variável `N`.

### 2. **Opção 0 - Sair**
Se o jogador selecionar a **Opção 0**, o jogo simplesmente imprime "Adeus!" e encerra a execução.


### 3. **Opção 1 - Modo Computador**
Neste modo, o computador gera um número aleatório entre 0 e 100, e o jogador tem que adivinhar qual número foi escolhido.

- O número aleatório é gerado pela função `random.randint(0, 100)` e armazenado na variável `num`.
- Um contador de tentativas, `i`, começa em 0 e é incrementado a cada tentativa do jogador.
- O jogador insere seu palpite usando o comando `input`, convertido para inteiro.
- A cada palpite, o programa verifica se o palpite do jogador é:
  - **Igual ao número**: Se o jogador acertar, o programa exibe uma mensagem de parabéns com o número de tentativas e termina o jogo.
  - **Maior que o número**: Se o palpite for maior, o jogo informa que o número pensado pelo computador é menor.
  - **Menor que o número**: Se o palpite for menor, o jogo informa que o número pensado é maior.

O jogo continua até que o jogador acerte o número.

### 4. **Opção 2 - Modo Normal**
Aqui, o jogador pensa em um número entre 0 e 100, e o computador tenta adivinhar esse número. Este modo usa um **algoritmo de busca binária**, que permite ao computador fazer palpites eficientes ajustando o intervalo de possibilidades.

- O jogador pensa em um número, e o intervalo de possibilidades inicialmente é de 0 a 100, representado pelas variáveis `menor` e `maior`.
- O palpite do computador é calculado como a média do intervalo atual: `(maior + menor) // 2`. Este valor, `tenta`, é o que o computador acredita ser o número.
- O jogador deve responder com "Acertou", "Maior" ou "Menor" para orientar o computador:
  - Se o jogador disser **"Acertou"**, o jogo termina e o computador exibe o número de tentativas que levou para adivinhar.
  - Se o jogador disser **"Maior"**, significa que o número que o computador pensou é menor do que o real, então o limite inferior do intervalo (`menor`) é atualizado para `tenta + 1`.
  - Se o jogador disser **"Menor"**, significa que o número que o computador pensou é maior do que o real, então o limite superior do intervalo (`maior`) é atualizado para `tenta - 1`.
- O jogo continua até que o computador acerte o número.


### 5. **Estrutura de Repetição**
Ambos os modos do jogo usam um loop `while True` para continuar as tentativas até que a condição de vitória seja satisfeita:
- No **Modo Computador**, o loop só termina quando o jogador acerta o número.
- No **Modo Normal**, o loop só termina quando o computador adivinha o número pensado pelo jogador.

### 6. **Contador de Tentativas**
Em ambos os modos, existe um contador (`i`) que registra o número de tentativas feitas até que o número seja adivinhado corretamente. Esse contador é incrementado a cada nova tentativa e mostrado no final do jogo.