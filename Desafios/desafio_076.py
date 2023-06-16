# DESAFIO 076 - Tabela de Produtos:

listagem = ('Lápis', 1.75,
			'Borracha', 2,
			'Caderno', 15.90,
			'Estojo', 25,
			'Transferidor', 4.20,
			'Compasso', 9.99,
			'Mochila', 120.32,
			'Canetas', 22.30,
			'Livro', 34.90)
print('-'*42)
print(f'{"LISTAGEM DE PREÇOS":^42}')
print('-'*42)
for i in range(0,len(listagem),2):
	print(f' {listagem[i]:.<30} R$ {listagem[i+1]:>6.2f}')
print('-'*42)
