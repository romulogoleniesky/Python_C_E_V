# DESAFIO 69:
print("--"*30)
print("CADASTRE UMA PESSOA")
print("--"*30)
tot18 = totH = totmulher20 = 0
while True:
    idade = int(input("IDADE: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("SEXO[M/F]: ")).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo in "mM":
        totH += 1
    if sexo in "fF":
        if idade < 20:
            totmulher20 += 1
    sair = " "
    while sair not in "SN":
        sair = str(input("Deseja CONTINUAR? [S/N] ")).strip().upper()[0]
    if sair == "N":
        break
print(f"Você cadastrou {totH} Homens, {tot18} são maiores de idade e {totmulher20} mulheres tem menos de 20 anos")
print("FIM!!")
