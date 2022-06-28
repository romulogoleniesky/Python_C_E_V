# DESAFIO 065:
resp = "S"
cont = total = maior = menor = 0
while resp in "Ss":
    num = int(input("Digite um número: "))
    cont += 1
    total += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

    resp = input("Deseja continuar ? [S/N]")
print(f"Você digitou {cont} números e a média deles é {total/cont}")
print(f"O maior número foi {maior} e o menor número foi {menor}.")
print("Acabou")
