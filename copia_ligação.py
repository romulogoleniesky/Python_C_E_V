
def ligação():
	num1 = [20]
	num2 = num1 # Faz uma ligação entre as listas.
	print(f'Primeira vez num1 :{num1} e num2: {num2}')
	num2.append(30)
	print('Adicionando 30 ao num2')
	print(f'Segunda vez num1 :{num1} e num2: {num2}') # Muda as duas Listas.

def copia():
	num1 = [20]
	num2 =[]
	num2.append(num1[:]) # Faz uma cópia da lista.
	print(f'Primeira vez num1 :{num1} e num2: {num2}')
	num2.append(30)
	print('Adicionando 30 ao num2')
	print(f'Segunda vez num1 :{num1} e num2: {num2}') # Muda somente a lista adicionada.

#ligação()
copia()
