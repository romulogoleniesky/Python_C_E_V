# DESAFIO 045 - GAME: PEDRA,PAPEL E TESOURA.
from random import randint
import time
print(
    """SUAS OPÇÕES:
    ( 0 ) PEDRA
    ( 1 ) PAPEL
    ( 2 ) TESOURA
    """
)
opcoes = ["PEDRA", "PAPEL", "TESOURA"]
jogador = int(input("Qual é a sua jogada? "))
computador = randint(0, 2)
jogada = (f"{opcoes[jogador]},{opcoes[computador]}")
print(jogada)
# print("JO")
# time.sleep(0.5)
# print("KEN")
# time.sleep(0.5)
# print("PO!!!")
