numeros = []
quit = 's'
while quit in 'sS':
    valor = int(input('Digite um valor: '))
    if valor in numeros:  # ou poderia usar'not in'.
        print(f'VALOR INVÁLIDO, O VALOR {valor} JÁ FOI ADICIONADO.')
    else:
        numeros.append(valor)
    quit = str(input('Deseja continuar? (S/N) '))
pares = []
impares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("=-"*30)
print(f'A lista completa é {numeros}.')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
print('FIM!')
