# DESAFIO 57;
sexo = str(input("DIGITE O SEU SEXO[M/F]: ")).strip().upper()[0]
while sexo not in "MF":
    sexo = str(input(f"{sexo}... DADOS INVALIDOS, TENTE NOVAMENTE [M/F]: ")).strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso!")
