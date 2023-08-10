# DESAFIO 94:
pessoa = {"Nome": "", "Sexo": "", "Idade": 0}
pessoas = []
quit = ""
homens = mulheres = tot_idade = 0
while quit in "sS":
    pessoa["Nome"] = input("Nome:  ")
    pessoa["Sexo"] = input("Sexo: (M/F)  ").upper()[0]
    if pessoa["Sexo"] not in "MF":
        pessoa["Sexo"] = input("Digite M para Masculino ou F para Feminino:   ").upper()[0]
    pessoa["Idade"] =  int(input("Idade:  "))
    tot_idade += pessoa["Idade"]
    pessoas.append(pessoa.copy())
    pessoa.clear()
    while True:
        quit = input("Deseja continuar? [S/N]").upper()[0]
        if quit in "SN":
            break
media = tot_idade / len(pessoas)
print("=-"*40)
print(f"  A)  Ao todo temos {len(pessoas)} pessoas cadastradas. ")
print(f"  B)  A média de idade é {media:.0f} anos.  ")
print("  C)  As mulheres cadastradas foram: ", end='')
for p in pessoas:
    if p["Sexo"] == "F":
        print(f" {p['Nome']}, ", end='')
print("")
print("  D)  Lista de pessoas que estão acima da média: ")
for i in pessoas:
    if i["Idade"] > media:
        print(f"    Nome = {i['Nome']} ;  Sexo = {i['Sexo']} ;   Idade = {i['Idade']} ;")
print("<<<< ENCERRADO >>>>")
