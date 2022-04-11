# DESAFIO - 050:

# primeira maneira.
s = []
t = 0
for i in range(1, 7):
    n = int(input(f"Digite o {i}º número: "))
    if n % 2 == 0:
        s.append(n)
for i in s:
    t = t + i

print(f"Os números PARES são: {s}, que totalizam: {t}")

print("""
                     
""")

# segunda maneira:
soma = 0
cont = 0
for i in range(1, 7):
    num = int(input(f"Digite o {i}º número: "))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f"Você informou {cont} números pares e a soma é {soma}.")
