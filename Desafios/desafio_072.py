# DESAFIO 72:
num = ("ZERO", "UM", "DOIS", "TRÊS", "QUATRO", "CINCO",
       "SEIS", "SETE", "OITO", "NOVE", "DEZ", "ONZE",
       "DOZE", "TREZE", "QUATORZE", "QUINZE", "DEZESSEIS",
       "DEZESETE", "DEZOITO", "DEZENOVE", "VINTE")
print("#*"*20)
print(f"         NÚMEROS POR EXTENSO")
print("#*"*20)

while True:
    while True:
        opcao = int(input("DIGITE UM NÚMERO DE 0 A 20:"))
        if 0 <= opcao <= 20:
            break
        print("TENTE NOVAMENTE!")
    print(f"O NÚMERO É {num[opcao]} !")
    sair = input("DESEJA CONTINUAR?[S/N]")
    if sair in "Nn":
        break
print("FIM!")
