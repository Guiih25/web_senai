import random

print("Vamos jogar um jogo!😍😍")
nome = input("Para começar digite seu nome: ")
print("Olá", nome, 'vamos começar!')


while True:
    pergunta = input("Faça uma pergunta: ")
    num = random.randint(1, 10)
    if num == 1:
        print("Não")
        continuar = input("Deseja continuar(S/N)?")
        if continuar == "s":
            continue
        else:
            break
    elif num == 2:
        print("Sim")
        continuar = input("Deseja continuar(S/N)?")
        if continuar == "s":
            continue
        else:
            break
    elif num == 3:
        print("Talvez")
        continuar = input("Deseja continuar(S/N)?")
        if continuar == "s":
            continue
        else:
            break
    elif num == 4:
        print("Nem pensar")
        continuar = input("Deseja continuar(S/N)?")
        if continuar == "s":
            continue
        else:
            break
    elif num == 5:
        print("Pergunte para seu amigo")
        continuar = input("Deseja continuar(S/N)?")
        if continuar == "s":
            continue
        else:
            break
    elif num == 6:
        print("COM CERTEZA")
        continuar = input("Deseja continuar(S/N)?")
        if continuar == "s":
            continue
        else:
            break
    elif num == 7:
        print("olha essa ta difici...não sei te dizer.")
        continuar = input("Deseja continuar(S/N)?")
        if continuar == "s":
            continue
        else:
            break
    elif num == 8:
        print("Vai sim, basta bater na bunda do seu amigo")
        continuar = input("Deseja continuar(S/N)?")
        if continuar == "s":
            continue
        else:
            break
    elif num == 9:
        print("vixxxxx")
        continuar = input("Deseja continuar(S/N)?")
        if continuar == "s":
            continue
        else:
            break
    else:
        print("Olha gosto nem te dizer...")
        continuar = input("Deseja continuar(S/N)?")
        if continuar == "s":
            continue
        else:
            break