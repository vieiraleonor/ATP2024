

### Funções principais:

1. **`Mostrarmenu`**: Exibe o menu com as opções disponíveis, que vão desde criar uma lista até sair da aplicação.
   
2. **`criarLista`**: Gera uma lista de números aleatórios com um tamanho especificado pelo usuário.

3. **`lerLista`**: Permite ao usuário criar uma lista manualmente, fornecendo números através de inputs.

4. **Operações de cálculo**:
   - **`soma`**: Calcula a soma de todos os elementos da lista.
   - **`media`**: Calcula a média dos elementos da lista.
   - **`maior`**: Encontra o maior valor na lista.
   - **`menor`**: Encontra o menor valor na lista.

5. **Verificação de ordenação**:
   - **`estaOrdCres`**: Verifica se a lista está ordenada em ordem crescente.
   - **`estaOrdDecres`**: Verifica se a lista está ordenada em ordem decrescente.

6. **`procura`**: Permite ao usuário procurar um número específico na lista e exibe a posição desse número, se ele for encontrado.

7. **`sair`**: Função para fechar o programa quando o usuário escolhe sair (opção 0).

### Estrutura de controle (Função `Menu`):

A função principal `Menu` entra em um loop infinito que exibe o menu e aguarda a escolha do usuário. Dependendo da opção escolhida, a função correspondente é chamada:

- Se o usuário escolher "Criar Lista" ou "Ler Lista", uma nova lista será gerada.
- Se optar por realizar operações como soma, média, maior ou menor valor, os cálculos serão feitos na lista atual.
- Se o usuário quiser verificar se a lista está ordenada, as funções de verificação serão chamadas.
- Também há a opção de procurar por um número específico na lista.

Quando o usuário escolhe "Sair" (opção 0), o loop é encerrado e o programa exibe uma mensagem de despedida.