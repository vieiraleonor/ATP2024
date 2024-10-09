#TPC3
import random

def MostrarMenu():
    print('''JOGO DOS FÓSFOROS
            -------MENU--------
            -------------------
            ----MODO NORMAL----
            -------------------
            --MODO COMPUTADOR--
            -------------------
            -------SAIR--------''')

#função para sair do jogo
def sair():
    print("Saiu do Jogo! Até à próxima!")

#jogador joga primeiro - computador ganha sempre
def modonormal():
        
    print("Está a jogar no Modo Normal")
    fosforos = 21

    while fosforos > 0:                
            #vez do jogador
            while True:
                fosjog = int(input("Quanto fósforos queres tirar? 1, 2 ,3 ou 4?"))
                if  fosjog not in  [1, 2, 3, 4] or fosjog > fosforos: #garantir que jogador joga os números corretos
                    print("Inválido. Tente de novo.") 
                    break

                fosforos = fosforos - fosjog
                print(f"Tirou {fosjog} fósforos. Faltam {fosforos} fósforos!")
                    
            #ver se jogador perdeu
                if fosforos == 0:
                    print("Perdeu o jogo! Tirou o último fósforo!")
                    break
            
            #vez do computador- ganhar sempre
                if fosforos >= 5:
                    foscom = (5 - fosjog) 
                else: 
                    foscom = fosforos - 1 #se o número de fósforos for 1, 2,3 ou 4 
                
                fosforos = fosforos - foscom
                print(f"O computador tirou {foscom} fósforos. Restam {fosforos} fósforos.")

            # ver se o computador perdeu - desnecessário
                if fosforos == 0:
                    print("Parabéns! O computador perdeu.")
                    break
                     
             

#computador joga primeiro
def modocomputador():

    print("Está a jogar o Modo Computador")
    fosforos = 21

    while fosforos > 0:
            #computador

            foscom = random.randint(1,4)
            fosforos = fosforos - foscom
            print(f"O computador tirou {foscom} fósforos. Restam {fosforos} fósforos!")

            if fosforos == 0:
                print("O computador venceu! Tirou o último fósforo.")
                break 

            #jogador

            while True:

                fosjog = int(input("Quantos fosfóros queres tirar? 1, 2, 3 ou 4?"))

                if fosjog not in [1, 2, 3, 4] or fosjog > fosforos:
                    print("Inválido!Tente novamente!")
                    break

            fosforos = fosforos - fosjog
            print(f"Tirou {fosjog} fósforos. Restam {fosforos} fósforos!")

            if fosforos == 0:
                print("Acabou o jogo!")
                break
         


def menu():
    while True:
        MostrarMenu()
        opcao = int(input('''Bem-vindos ao 'JOGOS DOS FÓSFOROS'!
                            PRIMA 1- para jogar o modo mormal
                            PRIMA 2 -para jogar o modo computador
                            PRIMA 0 - para sair da aplicação'''))

        if opcao == 0:
            sair()
            break

        elif opcao == 1:
            modonormal()

        elif opcao == 2:
            modocomputador()

        else:
            print("ERRO")
            break

menu()