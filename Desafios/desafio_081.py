numeros = []
quit = 's'
while quit in 'sS':
    valor = int(input('Digite um valor: '))
    if valor in numeros:  # ou poderia usar'not in'.
        print(f'VALOR INVÁLIDO, O VALOR {valor} JÁ FOI ADICIONADO.')
    else:
        numeros.append(valor)
    quit = str(input('Deseja continuar? (S/N) '))
numeros.sort(reverse=True)
print("=-"*30)
print(f'Você digitou {len(numeros)} elementos.')
print(f'O valores em ordem decrescente são: {numeros}')
if 5 in numeros:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
print('FIM!')
