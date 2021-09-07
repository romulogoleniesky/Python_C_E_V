# DESAFIO 34:

sal = float(input("Qual é o valor do seu salário?  "))
if sal > 1250:
    print(f"Seu novo salário com aumento de 10% é : R${sal*1.1:.2f}")
else:
    print(f"Seu novo salário com aumento de 15% é : R${sal*1.15:.2f} ")
