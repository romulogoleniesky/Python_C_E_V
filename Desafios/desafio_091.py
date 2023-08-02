# DESAFIO 91:
from random import randint
from operator import itemgetter
from time import sleep
jogadores = {"Jogador_1":0, "Jogador_2":0, "Jogador_3":0, "Jogador_4":0}
print(' Valores sorteados: ')
for k, v in jogadores.items():
	jogadores[k] = int(randint(1,6))
	print(f' O {k} tirou {jogadores[k]} no dado !')
	sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(f'{"RANKING":-^30}')
for i, n  in enumerate(ranking):
	print(f" Em {i+1}º Lugar ficou {n[0]} com {n[1]} !")
