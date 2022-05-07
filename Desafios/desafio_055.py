# DESAFIO 55
maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input(f"Qual é o peso da {i}ª pessoa?(KG)"))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f" O maior peso foi {maior} e o menor peso foi {menor}.")
