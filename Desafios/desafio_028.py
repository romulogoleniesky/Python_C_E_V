# DESAFIO 028.
import random

num_jogador = int(input('Qual o número o computador escolheu de 1 à 5? '))
num = random.randrange(1, 5)

if num == num_jogador:
        print('Parabéns, você acertou!')
else:
        print('Você errou!')

print(f'Computador: {num}, seu número: {num_jogador}')
