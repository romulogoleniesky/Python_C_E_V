
# SEGUNDO FORMATO

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for n in range(3):
    for m in range(3):
        valor = int(input(f'Digite um valor para [{n},{m}]: '))
        matriz[n][m] = valor
print('=-'*30)
for n in range(3):
    for m in range(3):
        print(f'[ {matriz[n][m]:^4} ] ', end=' ')
    print()
