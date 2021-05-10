# Desafio 2:
import random
#from random import shuffle -- para importar somente o shuffle#
print("Vamos organizar a ordem de apresentação dos trabalho:")
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))
lista = [n1, n2, n3, n4]
random.shuffle(lista) # embaralha a lista#
print("A ordem de apresentação dos alunos será: ")
for name in lista:
    print(f'Aluno(a):{name}')
