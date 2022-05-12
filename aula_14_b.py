# Aula 14 :
n = 1
impar = par = 0
while n != 0:
    n = int (input("Digite um valor: "))
    if n % 2 == 0:
        par += 1
    else: impar += 1
print(" Você digitou {} pares e {} ímpares.".format(par,impar))
