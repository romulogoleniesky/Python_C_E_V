# DESAFIO 87:

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for n in range(3):
    for m in range(3):
        valor = int(input(f'Digite um valor para [{n},{m}]: '))
        matriz[n][m] = valor
print('=-'*30)
pares = []

for n in range(3):
    for m in range(3):
        print(f'[ {matriz[n][m]:^4} ] ', end=' ')
        if matriz[n][m] % 2 == 0:
            pares.append(matriz[n][m])
    print()

terceirac = []
for n in range(3):
    terceirac.append(matriz[n][2])

maior = 0
for m in range(3):
    if matriz[1][m] > maior:
        maior = matriz[1][m]

print("=-"*30)
print(f'A Soma dos valores par é {sum(pares)}!')
print(f'A Soma dos valores da terceira coluna é {sum(terceirac)}!')
print(f'O maior valor da segunda linha é {maior}!')
