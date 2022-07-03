# DESAFIO 66 : While com Loop infinito.
valor = soma = cont = 0
while True:
    valor = int(input("Digite um valor(ou 999 para parar):"))
    if valor == 999:
        break
    cont += 1
    soma += valor
print(f"Você digitou {cont} valores e a soma deles é {soma}.")
