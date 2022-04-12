# DESAFIO 052
n = int(input("Digite um número: "))
d = 0
b = 0
for i in range(1, (n+1)):
    b += 1
    if n % i == 0:
        print(f"\033[1;32m{i}", end=" ")
        d += 1
    else:
        print(f"\033[1;31m{i}", end=" ")
    if b == 30:
        b -= 30
        print("\n")
print("\033[m")
if d == 2:
    print(f"O número \033[1;32m{n}\033[m foi divisível \033[1;32m{d}\033[m vezes, logo é um Número Primo.")
else:
    print(f"O número \033[1;32m{n}\033[m foi divisível \033[1;32m{d}\033[m vezes e não é Primo.")
