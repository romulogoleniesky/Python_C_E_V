# DESAFIO 62:
print("""
#################################
    PROGRESSÃO ARITIMÉTICA 2.0
#################################
""")
pt = int(input("Defina o 1° Termo: "))
r = int(input("Defina a Razão: "))
nt = int(input("Defina a quantidade de termos: "))
c = 0
com = 0
while com != 1:
    while c != nt:
        print(f"{pt} ↦ ", end="")
        c += 1
        pt += r
    print(" pausa...")
    comando = input('Deseja continuar a PA? [S-sim/N-não]').lower().strip()
    if comando == "s":
        nt += int(input("Mais quantos termos?"))
    else:
        com = 1
print(f"PA finalizada com {nt} termos mostrados.")
