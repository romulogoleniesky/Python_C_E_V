# Desafio 16: usando módulos.
import math
# primeira maneira:
num = float(input('Digite um número: '))
inteiro = math.floor(num)
print(f"O valor digitado foi {num} e a sua porção inteira é {inteiro}!")

# segunda maneira:
num = float(input('Digite um número: '))
inteiro = math.trunc(num)
print(f"O valor digitado foi {num} e a sua porção inteira é {inteiro}!")
