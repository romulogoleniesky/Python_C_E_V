# Aula - 15 : While Infinito.
from time import sleep
num = 0
while True: # While Verdadeiro/Infinito.
    print(f'{num:^3} > ', end='')
    num += 1
    sleep(1)
    if num == 11:
        break # Para interromper o While infinito precisa de um Break.
