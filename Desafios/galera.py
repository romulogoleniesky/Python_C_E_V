dados = []
galera = []
for p in range(5):
	dados.append(input('Digite o nome da pessoa: '))
	dados.append(input('Digite a idade da pessoa: '))
	galera.append(dados[:])
	dados.clear()
print(f'{"Relação de Pessoas":.^50}')
for n in galera:
	print(f'{n[0]} tem {n[1]} anos!')
print('FIM!')
