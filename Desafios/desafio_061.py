# DESAFIO 61:
print("""
###############################
     PROGRESSÃO ARITIMÉTICA
###############################
""")
pt = int(input("Defina o 1° Termo: "))
r = int(input("Defina a Razão: "))
nt = int(input("Defina a quantidade de termos: "))
c = 0
while c != nt:
    print(f"{pt} ↦ ", end="")
    c += 1
    pt += r
print("FIM!!")

