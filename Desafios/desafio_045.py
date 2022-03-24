# DESAFIO 045 - GAME: PEDRA,PAPEL E TESOURA.
from random import randint
import time
print(
    """SUAS OPÇÕES:
    ( 0 ) PEDRA
    ( 1 ) PAPEL
    ( 2 ) TESOURA""")
opcoes = ["PEDRA", "PAPEL", "TESOURA"]
jogador = int(input("Qual é a sua jogada? "))
print("¨¨"*15)
computador = randint(0, 2)
print("JO")
time.sleep(0.5)
print("KEN")
time.sleep(0.5)
print("PO!!!")
print(f"O Computador jogou {opcoes[computador]}. ")
print(f"O Jogador jogou {opcoes[jogador]}")
print("¨¨"*15)

if computador == 0: # Computador jogou Pedra.
    if jogador == 0: # Jogador jogou Pedra.
        print("EMPATE!!!")
    elif jogador == 1: # Jogador jogou Papel.
        print("JOGADOR GANHOU!!!")
    elif jogador == 2: # Jogador jogou Tesoura.
        print("COMPUTADOR GANHOU!!!")
    else: print("JOGADA INVALIDA!!")
elif computador == 1: # Computador jogou Papel.
    if jogador == 0: # Jogador jogou Pedra.
        print("COMPUTADOR GANHOU!!!")
    elif jogador == 1: # Jogador jogou Papel.
        print("EMPATE!!!")
    elif jogador == 2: # Jogador jogou Tesoura.
        print("JOGADOR GANHOU!!!")
    else: print("JOGADA INVALIDA!!")
elif computador == 2: # Computador jogou Tesoura.
    if jogador == 0: # Jogador jogou Pedra.
        print("JOGADOR GANHOU!!!")
    elif jogador == 1: # Jogador jogou Papel.
        print("COMPUTADOR GANHOU!!!")
    elif jogador == 2: # Jogador jogou Tesoura.
        print("EMPATE!!!")
    else: print("JOGADA INVALIDA!!")
