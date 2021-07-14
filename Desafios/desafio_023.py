# DESAFIO 023:
"""   Este bloco não funcionou com números sem milhar.

n = input("DIGITE UM NÚMERO DE 0 A 9999: ")
print(f"O número digitado foi: {n} ")
print(f"Seu milhar é: {n[0]}")
print(f"Sua Centena é: {n[1]}")
print(f"Sua Dezena é: {n[2]}")
print(f"Sua Unidade é: {n[3]}") """

n = int(input("Digite um número de 0 à 9999: "))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f"Sua unidade : {u}")
print(f"Sua dezena : {d}")
print(f"Sua centena : {c}")
print(f"Sua milhar : {m}")
