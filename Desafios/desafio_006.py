#DESAFIO - 006 : Peça um número e mostre alguns multiplos dele.
n = int ( input('Digite um número: '))
print('Você digitou {}, o dobro é {}, o triplo é {}, e a raiz é {}. '.format(n, n*2, n*3, n**(1/2)))


# Segunda maneira:
print(f"Você digitou {n}, o dobro é {n*2}, o triplo é {n*3}, e a raiz é {n**(1/2)}.")
