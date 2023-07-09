# DESAFIO 078 - Retornando valores maiores e menores de uma lista.

lista = []
for i in range(5):
	lista.append(int(input(f'Digite um valor para a posição {i} da lista: ')))
print("=-"*30)
lista.sort()
print(f'Você digitou os seguintes valores: {lista}')

maior = 0
for m in lista:
	if maior < m:
		maior = m
print(f'O maior valor digitado é {maior} !')

menor = 110
for n in lista:
	if menor > n:
		menor = n
print(f'O menor valor digitado é {menor} !')
