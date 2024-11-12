# Sistema de Gestão de Alunos

Este projeto é uma aplicação de gestão de alunos que permite criar turmas, adicionar alunos a essas turmas, listar informações de turmas e alunos, e salvar e recuperar turmas de um arquivo. A aplicação é executada em um menu interativo e insensível a letras maiúsculas e minúsculas.



### Estrutura de Dados
- Escola: É uma lista de turmas, onde cada turma é uma tupla que contém o nome da turma e uma lista de alunos.
- Aluno: Cada aluno é representado por uma tupla contendo o nome, o ID, e uma lista de três notas.

### Funções

1. MostrarMenu(): Exibe as opções do menu para o usuário. Este menu permite navegar pelas funcionalidades principais da aplicação, como criar turmas, listar alunos, consultar alunos por ID, entre outros.

2. existeturma(nome_turma, escola): Verifica se uma turma já existe na lista de turmas. Essa função é insensível a maiúsculas e minúsculas.

3. CriarTurma(nome_turma, escola): Adiciona uma nova turma à escola, caso a turma não exista. Utiliza `existeturma()` para garantir que não haverá duplicatas.

4. `inserir_aluno(nome_turma, aluno)`: Insere um aluno em uma turma específica. Verifica se o ID do aluno já existe na turma antes de adicionar o novo aluno. Se o ID for único, ele adiciona o aluno à lista.

5. `listar(nome_turma)`: Lista todos os alunos em uma turma específica, exibindo o nome, ID e notas de cada aluno. Exibe uma mensagem de erro se a turma não for encontrada.

6. `consultar_aluno(id_aluno, nome_turma)`: Procura um aluno pelo seu ID em uma turma específica. Se o aluno for encontrado, exibe suas informações; caso contrário, informa que o aluno não foi encontrado.

7. `guardar_turma(nome_turma, fnome)`: Salva os dados de uma turma em um arquivo de texto. Cada aluno é salvo com nome, ID e suas três notas.

8. `recuperar_turma(fnome)`: Recupera os dados de uma turma de um arquivo de texto e retorna uma lista de alunos com seus respectivos dados.

9. `Menu()`: Controla o fluxo principal da aplicação, chamando as funções apropriadas de acordo com a escolha do usuário. Permite ao usuário navegar pelas funcionalidades de criação, inserção, listagem, consulta, armazenamento e recuperação de turmas e alunos.

## Instruções de Uso

1. **Executar o Programa**: Execute o código para iniciar a aplicação. O menu será exibido com as opções disponíveis.

2. **Navegar pelo Menu**:
    - **Criar Turma**: Digite o nome de uma nova turma para adicioná-la à escola.
    - **Inserir Aluno**: Escolha uma turma e insira os dados de um aluno (nome, ID e notas).
    - **Listar Turma**: Liste todos os alunos de uma turma específica.
    - **Consultar Aluno por ID**: Encontre um aluno pelo ID em uma turma específica.
    - **Guardar Turma em Ficheiro**: Salve os dados de uma turma em um arquivo.
    - **Carregar Turma de um Ficheiro**: Carregue uma turma de um arquivo para a memória.
    - **Sair**: Encerre a aplicação.

## Exemplo de Uso

Ao escolher a opção de menu **3** e fornecer o nome da turma `turmaA`, o programa exibirá todos os alunos de `turmaA` (caso existam) e suas respectivas notas. A aplicação verifica automaticamente a turma e o ID dos alunos sem considerar maiúsculas e minúsculas, garantindo que `turmaa` e `TURMAA` sejam tratados igualmente.

## Estrutura do Arquivo

O arquivo em que as turmas são salvas armazena as informações de cada aluno em uma linha com o formato `Nome,ID#NotaTPC,NotaProj,NotaTeste`. Esse formato é usado tanto para gravar quanto para ler as informações.

## Observações

- **Insensibilidade a Maiúsculas e Minúsculas**: Todos os nomes de turmas são convertidos para minúsculas antes de serem armazenados ou comparados, facilitando o uso.
- **Gestão de IDs Únicos**: Cada aluno tem um ID exclusivo dentro de sua turma para evitar duplicações.

## Conclusão

Este sistema de gestão de alunos foi desenvolvido para ser simples e fácil de usar, oferecendo uma maneira eficiente de organizar informações escolares. A implementação modular facilita futuras expansões e melhorias no código.