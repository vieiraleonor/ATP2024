README


1. Função MostrarMenu()
Esta função exibe um menu principal com três opções:

Modo Normal (jogador joga primeiro, e o computador sempre vence)
Modo Computador (computador joga primeiro)
Sair do jogo


2. Função sair()
Esta função imprime uma mensagem de despedida, quando o usuário escolhe sair do jogo no menu.

3. Função modonormal()
Esta função implementa o modo normal do jogo, no qual o jogador joga primeiro e o computador sempre garante a vitória seguindo uma estratégia específica.

Passos:
Inicializa o jogo com 21 fósforos.
Vez do jogador:
O jogador escolhe quantos fósforos quer remover (1, 2, 3 ou 4). O código garante que a entrada seja válida: se o jogador digitar um valor inválido (como um número fora de 1-4 ou mais do que os fósforos restantes), o jogo pede que ele tente de novo.
Depois de uma jogada válida, o número de fósforos restantes é atualizado.
O código verifica se o número de fósforos chegou a zero. Se sim, o jogador perde o jogo.
Vez do computador:
Se ainda houver fósforos, o computador faz sua jogada. Para garantir que o computador sempre vença, ele remove fósforos de forma que a soma de fósforos removidos pelo jogador e pelo computador seja igual a 5 (sempre que possível). Isso força o jogador a ficar com o último fósforo.
Se houver menos de 5 fósforos restantes, o computador simplesmente remove todos os fósforos restantes, exceto o último fósforo.
Após a jogada do computador, o número de fósforos restantes é atualizado e novamente verifica se o jogo terminou.
Essa estratégia garante que o computador nunca perde, desde que o jogador comece primeiro.

4. Função modocomputador()
Esta função implementa o modo computador, onde o computador joga primeiro. A principal diferença é que, agora, o computador começa a remover os fósforos.

Passos:
Inicializa o jogo com 21 fósforos.
Vez do computador:
O computador escolhe aleatoriamente quantos fósforos tirar (entre 1 e 4). Esta escolha é feita pela função random.randint(), que retorna um número aleatório entre 1 e 4.
O número de fósforos restantes é atualizado, e o jogo verifica se o número de fósforos chegou a zero. Se sim, o computador vence.
Vez do jogador:
O jogador escolhe quantos fósforos quer remover (1, 2, 3 ou 4), com a mesma validação de entrada que no modo normal.
O número de fósforos restantes é atualizado e o jogo verifica se o jogador perdeu (ou seja, se ele retirou o último fósforo).
Neste modo, o computador não segue uma estratégia específica para vencer, e o jogador pode vencer dependendo das suas jogadas.

5. Função menu()
Esta função controla o fluxo do jogo, permitindo ao jogador escolher entre:

Jogar o modo normal
Jogar o modo em que o computador joga primeiro
Sair do jogo
Passos:
Mostra o menu principal através da função MostrarMenu().
Solicita ao jogador que escolha uma opção (1, 2 ou 0) e, de acordo com a entrada:
Chama a função modonormal() se o jogador escolher 1.
Chama a função modocomputador() se o jogador escolher 2.
Chama a função sair() se o jogador escolher 0.
Valida a entrada do usuário para evitar entradas inválidas. Se for inválida, o jogador vê uma mensagem de erro.