# DESAFIO 60, Com "For":
n = int(input("Deseja o Fatorial de qual número? "))
t = 1
print(f"{n}! = ", end="")
for i in range(n, 0, -1):
    t *= i
    print(f"{i}", "X " if i > 1 else "= ", end="")
print(f"{t}")
