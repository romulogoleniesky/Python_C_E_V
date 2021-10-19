#DESAFIO-37:
num = int(input("Digite um número inteiro: "))
opcao = "[ 1 ]-Converter para BINÁRIO \n[ 2 ]-Converter para OCTAL\n[ 3 ]-Converter para HEXADECIMAL"
print(opcao)
modo = int(input("Sua opção: "))
if modo == 1:
    print(f"{num} em BINÁRIO é {bin(num).strip('0b')}")
elif modo == 2:
    print(f"{num} em OCTAL é {oct(num).strip('0o')}")
elif modo == 3:
    print(f"{num} em HEXADECIMAL é {hex(num).strip('0x')}")
else:
    print("Opção invalida!")
