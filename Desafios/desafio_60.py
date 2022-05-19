# DESAFIO 60:
n = int(input("Deseja o Fatorial de qual número? "))
print(f"{n}!= {n}", end=" ")
t = n
while n != 1:
    n -= 1
    print(f"X {n}", end=" ")
    t *= n
print(f"= {t}")
