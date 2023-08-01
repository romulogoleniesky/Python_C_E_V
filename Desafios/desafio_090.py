# DESAFIO 90:

"""  --------------PRIMEIRA FORMA--------
aluno = { 'nome':'', 'media':0}
aluno['nome'] = input("Nome: ")
aluno['media'] = float(input("Média: "))
print("=-"*35)
print(f" - O nome do aluno é {aluno['nome']} !")
print(f" - A média do aluno é {aluno['media']} !")
if aluno['media'] >= 7:
	print(' - Aluno APROVADO!')
else:
	print(' - Aluno REPROVADO!')
"""
#   --------- SEGUNDA FORMA: ------

aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Qual a media de {aluno["nome"]}? :'))
if aluno['media'] >= 7:
	aluno['status'] = 'APROVADO'
else:
	aluno['status'] = 'REPROVADO'
print('=-'*35)
for k, v in aluno.items():
	print(f' - A {k} é igual a {v} !')


