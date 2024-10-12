#TPC4 

import random

def Mostrarmenu():
    print('''-----------------MENU-----------------
             1- Cria Lista ------------------------
             2- Ler Lista -------------------------
             3- Soma ------------------------------
             4- Média -----------------------------
             5- Maior -----------------------------
             6- Menor -----------------------------
             7- estaOrdenada por ordem CRESCENTE --
             8- estaOrdenada por ordem DECRESCENTE-
             9- Procura um elemento ---------------
             0- SAIR-------------------------------''')



def criarLista():
    lista=[]
    n = int(input("Qual o tamanho da lista que deseja?"))
    while len(lista) < n:
        numeros = random.randint(1, 100)
        lista.append(numeros)

    return lista

    
def lerLista():
    n = int(input("QUe tamanho deseja que tenha a sua lista?"))
    lista = []
    i = 0
    while i < n:
        numero = int(input("Introduza os números que deseja na sua lista"))
        lista.append(numero)
        i = i +1

    return lista


def soma(lista):
    soma = 0
    for elem in lista:
        soma = soma + elem
    return soma

def media(lista):
    soma = 0
    for elem in lista:
        soma = soma + elem
    return (soma/ len(lista))

def maior(lista):
    i = 1
    maior = lista[0]
    while i < len(lista):
        if maior < lista[i]:
            maior = lista[i]
        i = i + 1
    return maior


def menor(lista):
    i = 1
    menor = lista[0]

    while i < len(lista):
        if menor > lista[i]:
            menor = lista[i]
        i = i + 1

    return menor

def estaOrdCres(lista):
    for i in range(len(lista)-1):
        if lista[i] >= lista [i+1]:
            print("A lista NÃO está ordenada por ordem crescente.")
        else:
            print("A lista está SIM ordenada por ordem crescente.")


def estaOrdDecres(lista):
    for i in range(len(lista)-1):
        if lista[i] <= lista[i + 1]:
            print("A lista NÃO está ordenada por ordem decrescente.")

        else:
            print("A lista está SIM odenada por ordem decrescente.")


def procura(lista):
    proc = int(input("QUe número deseja procurar na lista?"))
    if proc in lista:
        ind = lista.index(proc)
        print(f"O número que procura, {proc}, está na posição {ind}.")
    elif proc not in lista:
        ind = -1
        print(f"O número que procura não se encontra na lista.")


def sair():
    return


def Menu ():
    lista=[]
    while True:
        Mostrarmenu()
        opcao = int(input("Escolha o modo que deseja utilizar!"))

        if opcao == 0:
            print("Fechou a aplicação! Até breve!")
            print(f"Lista atual: {lista}")
            sair()
            break
        

        elif opcao == 1:
            print("Escolheu 'Criar Lista'.")
            lista = criarLista()
            print(f"O computador criou a seguinte lista: {lista}")


        elif opcao == 2:
            print("Escolheu 'Ler Lista'")
            lista = lerLista()
            print(f"= jogador criou a seguinte lista: {lista}")


        elif opcao == 3:
            print("Escolheu 'Soma'.")
            soma(lista)
            print("Soma dos elementos:", soma(lista))
            print(f"A lista ativa é a seguinte: {lista}")

        elif opcao == 4:
            print("Escolheu 'Média'.")
            media(lista)
            print("Média dos elementos:", media(lista))
            print(f"A lista ativa é a seguinte: {lista}")

        elif opcao == 5:
            print("Escolheu 'Maior'.")
            maior(lista)
            print("Maior elemento:", maior(lista))
            print(f"A lista ativa é a seguinte: {lista}")

        elif opcao == 6:
            print("Escolheu 'Menor'.")
            menor(lista)
            print("Menor elemento:", menor(lista))
            print(f"A lista ativa é a seguinte: {lista}")

        elif opcao == 7:
            print("Escolheu 'estaOrdenada por ordem crescente'.")
            estaOrdCres(lista)
            print(f"A lista ativa é a seguinte: {lista}")

        elif opcao == 8:
            print("Escolheu 'estaOrdenada por ordem decrescente'.")
            estaOrdDecres(lista)
            print(f"A lista ativa é a seguinte: {lista}")

        elif opcao == 9:
            print("Escolheu 'Procura um elemento'.")
            procura (lista)
            print(f"A lista ativa é a seguinte: {lista}")

        else:
            print("Resposta inválida! Tente novamente.")
            print(f"A lista ativa é a seguinte: {lista}")

Menu()