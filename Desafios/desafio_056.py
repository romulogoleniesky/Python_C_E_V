# DESAFIO 056:
somaidade = 0
homvelho = 0
mulvinte = 0
nomevelho = str
for i in range(1, 5):
    print(f"-----{i}ª PESSOA-----")
    nome = str(input("NOME: "))
    idade = int(input("IDADE: "))
    sexo = str(input("SEXO[M/F]")).upper()
    if sexo == "M":
        if i == 1:
            homvelho = idade
        elif idade > homvelho:
            homvelho = idade
            nomevelho = nome
    elif sexo == "F":
        if idade < 20:
            mulvinte += 1
    somaidade += idade

print(f"A média de idade do grupo é {(somaidade)/4} anos.")
print(f"O homem mais velho tem {homvelho} anos e se chama {nomevelho}.")
print(f"Ao todo são {mulvinte} mulheres com menos de 20 anos.")
