# DESAFIO 088 : FAZENDO JOGOS DA MEGA SENA.
from random import randint
from time import sleep
numeros = []


print("$$"*20)
print(f"{'JOGOS DA MEGA-SENA':^38}")
print("$$"*20)
num_jogos = int(input("      Quantos jogos você deseja?: "))
print(f"-----------SORTEANDO {num_jogos} JOGOS!-----------")
while True:
	for jogo in range(num_jogos):
		print(f'JOGO {jogo+1}: ',end='')
		while len(numeros) <= 5:
			numero = randint(1,60)
			if numero not in numeros:
				numeros.append(numero)
		numeros.sort()
		sleep(1)
		print(numeros)
		numeros.clear()
	break
print(f"{'BOA SORTE':-^40}")
