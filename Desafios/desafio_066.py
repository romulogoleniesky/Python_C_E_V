# DESAFIO 66 - Parando um While com uma Flag.

valor = cont = soma = 0
while valor != 999: # O 999 está sendo usado como uma Flag.
    soma += valor
    valor = int(input("Digite um valor: (ou 999 para parar)"))
    cont += 1
print(f"Você informou {cont-1} valores e a soma deles é {soma}")
