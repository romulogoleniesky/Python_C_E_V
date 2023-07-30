# DESAFIO 89 - BOLETIM ESCOLAR:
alunos = list()
while True:
	nome = input("Nome : ")
	n1 = float(input("Nota 1: "))
	n2 = float(input("Nota 2: "))

	aluno = [nome, n1, n2]
	alunos.append(aluno[:])
	quit = input("Deseja continuar [S/N]? ")
	if quit in 'nN':
		break
print("-"*30)
print("__Nº_______NOME_________MÉDIA_")

for  n, x in enumerate(range(len(alunos))):
	print(f"  {n+1} - {alunos[x][0]:^17} - {(alunos[x][1]+alunos[x][2])/2}")
print("__"*35)
while True:
	show = int(input("Para mostrar a nota do aluno, digite o número dele: (ou zero para sair) "))
	if show == 0:
		break
	else:
		print("__"*35)
		print(f" O aluno {alunos[show-1][0]}, tirou as notas {alunos[show-1][1]} e {alunos[show-1][2]} !")
		print("__"*35)
print('  <<<<<  FIM  >>>>>>')
