#DESAFIO 038:
import time
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
print("Calculando.. .")
time.sleep(2)
if n1 > n2:
    print("O primeiro número é maior!")
elif n2 > n1:
    print("O segundo número é maior!")
else:
    print("Os números são iguais!")
