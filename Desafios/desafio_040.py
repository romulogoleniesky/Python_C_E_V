# DESAFIO 40 - Média Clássica.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota:"))
media = (nota1 + nota2) / 2
print(f"Tirando {nota1} e {nota2}, a média do aluno é {media:.1f}")
resultado = 0
if media < 5:
    resultado = "REPROVADO!"
elif media >= 5 and media < 7:
    resultado = " em RECUPERAÇÃO!"
else:
    resultado = "APROVADO!"
print(f"O Aluno está {resultado} ")
