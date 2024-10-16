README

Esse código é uma aplicação simples de cinema, que gerencia salas de cinema, filmes e a venda de bilhetes.

**Salas de cinema**: Cada sala é uma lista que contém:
   - Capacidade máxima de lugares.
   - Lista de lugares vendidos (inicialmente vazia).
   - Nome do filme exibido na sala.
   


1. **MostrarMenu**: Exibe um menu com as opções disponíveis para o usuário, como listar filmes, comprar bilhete, etc.

2. **reset**: Limpa a lista de cinemas (reinicia o sistema).

3. **existesala(cinema, sala)**: Verifica se já existe uma sala no cinema exibindo o mesmo filme.

4. **inserirsala(cinema, sala)**: Insere uma nova sala no cinema, desde que o filme ainda não esteja em exibição.

5. **listar(cinema)**: Lista todos os filmes que estão em exibição, junto com a capacidade máxima das salas.

6. **disponivel(cinema, filmecin, lugar)**: Verifica se há disponibilidade de um determinado lugar para um filme específico (se o lugar ainda não foi vendido).

7. **venderBilh(cinema, filmecin, lugar)**: Registra a compra de um bilhete para um filme em uma sala específica, verificando se o lugar está disponível.

8. **listardisponibilidades(cinema)**: Lista a quantidade de lugares disponíveis para cada filme em exibição.

9. **cria_sala(cinema, filmecin, lugares)**: Cria uma nova sala com um filme e uma capacidade específica de lugares.

10. **sair**: Simplesmente imprime uma mensagem de saída.

A função principal **Menu()** exibe o menu e permite ao usuário escolher uma ação (exibir filmes, comprar bilhete, adicionar salas, etc.). Dependendo da opção, ela chama outras funções para realizar as ações.

- O sistema gerencia um conjunto de salas de cinema e seus filmes.
- O usuário pode ver filmes em exibição, comprar bilhetes (se o lugar estiver disponível), criar novas salas e filmes, e verificar a disponibilidade de assentos.
- O código também permite "resetar" o cinema (limpar as salas e os filmes).

Se precisar de mais detalhes sobre qualquer parte específica, estou à disposição!