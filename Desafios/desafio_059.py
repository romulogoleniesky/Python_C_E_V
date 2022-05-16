# DESAFIO 59
import time
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
opcao = 0
while opcao != 6:
    print("="*50,
        """
    ESCOLHA UMA OPÇÃO ABAIXO:
    [ 1 ] SOMAR
    [ 2 ] SUBTRAIR
    [ 3 ] MULTIPLICAR
    [ 4 ] DIVIDIR
    [ 5 ] NOVOS NÚMEROS
    [ 6 ] SAIR
    """)
    opcao = int(input("Digite a Opção: "))
    if opcao == 1:
        print(f"A soma entre {n1} e {n2} é {n1+n2} .")
    elif opcao == 2:
        print(f"A subtração entre {n1} e {n2} é {n1-n2} .")
    elif opcao == 3:
        print(f"A multiplicação entre {n1} e {n2} é {n1*n2} .")
    elif opcao == 4:
        print(f"A divisão entre {n1} e {n2} é {n1/n2:.2f} .")
    elif opcao == 5:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
    elif opcao == 6:
        print("Volte sempre!!!")
    else:
        print("Opção inválida.")
    time.sleep(5)
print("FIM!!!")
