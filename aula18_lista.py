# LISTAS:

# Ítens da lista ficam dentro de colchetes.
frutas = ['maca', 'pera', 'goiaba']
print(frutas)
frutas.append('manga')  # Listas são mutáveis.
print(frutas)
frutas.pop()  # Remove o último ítem.
print(frutas)
frutas.pop(1)  # Remove o ítem passando seu índice.
print(frutas)
numeros = list(range(5, 100, 5))  # Atribuíndo através de um range.
print(numeros)
num_aleatorios = [23, 45, 34, 56, 89, 65, 454, 22, 11, 2, 32, 1, 9, 8]
print(f'Números aleatórios: {num_aleatorios}')
num_aleatorios.sort()
print(f'Números aleatórios organizados: {num_aleatorios}')
num_aleatorios.sort(reverse=True)
print(f'Agora em ordem contrária: {num_aleatorios}')
print(len(num_aleatorios))  # O Len() conta o total de elementos.
# O Insert permite indicar o indice da posição a ser adcionado o novo item.
num_aleatorios.insert(7, 666)
print(num_aleatorios)

for c, f in enumerate(frutas): # indice e valor.
    print(f'A fruta {f} esta na posição {c}')

