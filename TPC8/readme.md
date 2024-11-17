
TPC1 a)
Este codigo junta elmentos nao comuns a ambas as listas simultaneamente:
ncomuns: Combina duas compreensões de lista para incluir:
Elementos de lista1 que não estão em lista2.
Elementos de lista2 que não estão em lista1.
nao_comuns: Cria uma única lista com todos os elementos de ambas as listas (lista1 + lista2), mas inclui apenas aqueles que não pertencem a ambas ao mesmo tempo.
Ambas as abordagens retornam os elementos que aparecem apenas em uma das listas, sem duplicatas. 

b) 
Divide o texto apartir do split. Palavras com mais de 3 letras ficam na lista: lista. 

c) 
Recebe as palavras de lista e dá print ao seu index+1(para evitar o 0) e á respetiva palavra. 

TPC2 a) 
recebe strings e substrings e o objetivo é verificar quantas vezes a sub aparece na string.

b)
recebe uma lista de números e organiza-a de menor para maior(sort), calcula o produto entre os 3 menores e devolve o resultado 

c)
O código reduz um número inteiro a um único dígito, somando repetidamente os dígitos do número até que reste apenas um dígito.
Enquanto o número tiver mais de um dígito (num >= 10), continua o processo.
Para cada passo:
Calcula a soma dos dígitos do número.
Atualiza num com o valor dessa soma.

d) 
A função myIndexOf(s1, s2) procura a posição de uma substring (s2) dentro de uma string (s1) e funciona assim:
Se s2 estiver presente em s1: Usa o método index para retornar a posição da primeira ocorrência de s2 em s1.
Se s2 não estiver em s1: Retorna -1, indicando que a substring não foi encontrada. 

TPC3a) 
Verifica quantos posts existem. 

b)verifica quantos posts de certo autor existem pesquisando pelo seu nome. 

c)adiciona autor de posts que ainda nao estao incluidos na lista. 

d)insPost:
Recebe como parâmetros:
redeSocial: Lista que armazena os posts.
conteudo: O texto do post.
autor: Nome do autor do post.
dataCriacao: Data de criação do post.
comentarios: Número inicial de comentários.
Criação do novo post:
O post é representado por um dicionário com as seguintes chaves:
'id': Gera um identificador único para o post, no formato 'pX', onde X é o número total de posts incrementado em 1 (assumindo que a função quantosPost retorna o total de posts atuais).
'conteudo': Texto do post.
'autor': Nome do autor.
'dataCriacao': Data em formato string.
'comentarios': Quantidade inicial de comentários.
Adiciona o post à rede social:
O novo post é adicionado à lista redeSocial com o método .append().
Retorno:
A função retorna a lista redeSocial atualizada. 

e)Parâmetros:
redeSocial: Uma lista de dicionários, onde cada dicionário representa um post com uma chave 'id'.
id: O identificador ('id') do post que deve ser removido.
Iteração pela lista:
A função percorre cada elemento (post) em redeSocial.
Compara a chave 'id' do post atual com o valor fornecido em id.
Remoção do post: Se o 'id' do post corresponder ao valor especificado, o post é removido da lista usando o método .remove(post).
Retorno:A função retorna a lista atualizada (redeSocial) com o post removido. 

f)Parâmetros:
redeSocial: Uma lista de dicionários, onde cada dicionário representa um post com várias informações, incluindo o autor (chave 'autor').
Processo: Cria uma lista vazia chamada lista.
Percorre cada post na lista redeSocial.
Para cada post, adiciona à lista lista uma tupla contendo:
O autor do post (post['autor']).
O post inteiro.
Retorno: A função retorna a lista de tuplas, onde cada tupla tem a forma (autor, post). 

g)Parâmetros:
redeSocial: Uma lista de dicionários, onde cada dicionário representa um post e inclui uma lista de comentários (na chave 'comentarios').
autor: Nome do autor dos comentários que você deseja buscar.
Processo: Inicializa uma lista vazia lista para armazenar os posts relevantes.
Percorre cada post em redeSocial.
Dentro de cada post, percorre a lista de comentários (post['comentarios']).
Verifica se o autor do comentário (comentario['autor']) corresponde ao autor fornecido.
Se encontrar um comentário do autor especificado, adiciona o post à lista lista.
Retorno: A função retorna a lista lista, contendo os posts nos quais o autor especificado fez comentários.