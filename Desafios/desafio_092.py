# DESAFIO 92:
from datetime import datetime
trabalhador = dict()
trabalhador["Nome"] = input(" Nome: ")
ano_nasc = int(input(" Ano de nascimento: "))
idade = datetime.now().year - ano_nasc
trabalhador["Idade"] = idade
trabalhador["CTPS"] = input(" Carteira de trabalhado: (0 se não ouver)")


if trabalhador["CTPS"] != 0:
	trabalhador["Contratação"] = int(input(" Ano de Contratação: "))
	trabalhador["Salário"] = float(input(" Salário: R$  "))
	trabalhador["Aposentadoria"] = trabalhador["Idade"] + ((trabalhador["Contratação"]+35) - datetime.now().year)

print("=-"*30)

for k, v in trabalhador.items():
	print(f' - {k} ígual a {v} !')

