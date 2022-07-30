# DESAFIO 71:
print("$"*50)
print("{:-^50}".format(" NowBank "))
print("$"*50)
valor = int(input("Qual valor você quer sacar?"))
ced = 50
cont = 0
while True:
    if valor >= ced:
        valor -= ced
        cont += 1
    else:
        if cont > 0:
            print(f"Total de {cont} cédulas de {ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cont = 0
        if valor == 0:
            break
print("Saque realizado!")
