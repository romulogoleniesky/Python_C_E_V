#DESAFIO - 048:
acumulador = 0
contador = 0
print("Os números ímpas e multiplos de 3, de 1 até 500 são:")
for n in range(1, 501, 2):
    if n%3==0:
        contador = contador+1
        acumulador = acumulador+n
        print(n, end=" ")
print(f"\n Foram contados {contador} números.")
print(f"\n A soma de todos o números é {acumulador}")
