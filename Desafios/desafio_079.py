numeros =[]
quit = 's'
while quit == 's':
	valor = int(input('Digite um valor: '))
	if valor in numeros:
		print(f'VALOR INVÁLIDO, O VALOR {valor} JÁ FOI ADICIONADO.')
	else:
		numeros.append(valor)
	quit = str(input('Deseja continuar? (S/N) '))
numeros.sort()
print(f'Os números digitados foram {numeros} .')
print('FIM!')
