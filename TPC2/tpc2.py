import random

print('''  ADIVINHA O NÚMERO
         --------------------
         --------MENU--------
         --------------------
         --MODO COMPUTADOR---
         --------------------
         ----MODO NORMAL-----
         --------------------
         --------SAIR--------''')

N = int(input('''Qual modo deseja jogar?
              Opção 1- MODO COMPUTADOR
              Opção 2- MODO NORMAL
              Opção 0- SAIR
              Escolha: '''))

# Opção 0- Sair
if N == 0:
    print("Adeus!")

# Opção 1- MODO COMPUTADOR
elif N == 1:
    i = 0
    num = random.randint(0, 100)  # Gera um número entre 0 e 100

    while True:
        tent = int(input("Qual o número que o computador está a pensar? "))
        i += 1

        if tent == num:
            print(f"Parabéns! Acertaste no número! Em apenas {i} tentativa(s)!")
            break
    
        elif tent > num:
            print(f"Errado! O número que pensou foi {tent}, o que eu pensei é menor.")

        else:
            print(f"Errado! O número que pensou foi {tent}, o que eu pensei é maior.")

# Opção 2- MODO NORMAL
elif N == 2:
    i = 0
    menor = 0
    maior = 100
    print("Pense num número entre 0 e 100!")

    while True:
        tenta = (maior + menor) // 2  # Calcula o palpite
        print(f"O seu número será {tenta}?")
     
        res = input("Responda: Acertou, Maior ou Menor? ").lower()  # Converte resposta para minúsculas
        i += 1

        if res == "acertou":
            print(f"Acertei em apenas {i} tentativa(s)!")
            break
                    
        elif res == "maior":
            menor = tenta + 1

        elif res == "menor":
            maior = tenta - 1

        else:
            print("Resposta inválida, tente novamente")
