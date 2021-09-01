#DESAFIO 033.
import time as T
print('Digite alguns valores abaixo: ')
a = int(input("PRIMEIRO VALOR: "))
b = int(input("SEGUNDO VALOR:  "))
c = int(input("TERCEIRO VALOR: "))
print('Organizando tudo...')
T.sleep(2)
num = [a, b, c]
num.sort()
print(f'O menor valor foi {num[0]} e o maior valor foi {num[-1]}.')
