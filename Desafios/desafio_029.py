#DESAFIO 29

import time

vel = int(input('Qual a velocidade do seu carro? '))
with open("texto.txt") as file:
    texto = file.read().splitlines()
    for linha in texto:
        print(linha)
        time.sleep(1)
if vel <= 80:
    print('OK, velocidade dentro do permitido, siga sua viagem.')
else:
    print(f'Você ultrapassou a velocidade permitida de 80km/h, pagará multa de R${(vel-80)*7.00:.2f}. ')

