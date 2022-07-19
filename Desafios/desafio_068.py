# DESAFIO 68:
from random import randrange
c = 0
while True:
    print("*"*40)
    print("""
    JOGO PAR OU ÍMPAR
    """)
    print("*"*40)
    n = int(input("ESCOLHA UM NÚMERO:  "))
    a = str(input("AGORA ESCOLHA PAR OU ÍMPAR: [P/I] ")).strip().upper()[0]
    while a not in "pPiI":
        a = input("PAR[P] OU ÍMPAR[I]???:  ")
    r = randrange(0, 11)
    res = (n + r) % 2
    print("*"*40)
    if a in "pP":
        print(f"Você apostou PAR e escolheu o número {n}.")
        print(" ")
        if res == 0:
            print(f"O sistema jogou {r}, o total foi {n+r}, deu PAR, PARABÉNS VOCÊ GANHOU!!!")
            c += 1
        elif res == 1:
            print(f"O sistema jogou {r}, o total foi {n+r}, deu ÍMPAR, Você PERDEU!!!")
    elif a in "iI":
        print(f"Você apostou ÍMPAR e escolheu o número {n}.")
        print(" ")
        if res == 0:
            print(f"O sistema jogou {r}, o total foi {n+r}, deu PAR, Você PERDEU!!! ")
        elif res == 1:
            print(f"O sistema jogou {r}, o total foi {n+r}, deu ÍMPAR, PARABÉNS VOCÊ GANHOU!!!")
            c += 1

    sair = str(input("\nDeseja SAIR ou CONTINUAR??? [S/C] ")).strip().upper()[0]
    while sair not in "sScC":
        sair = str(input("SAIR[S] OU CONTINUAR[C]???:  "))
    if sair in "sS":
        break
print(f"Você ganhou {c} vezes.")
print("FIM!!")
