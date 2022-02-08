#Desafio 044: Gerenciador de Pagamentos.
print('{:=^40}'.format(" LOJA FILGUEIRA "))
valor = float(input("Digite o valor da compra: R$  "))
forma= int(input("ESCOLHA A FORMA DE PAGAMENTO:\n[ 1 ] à vista em dinheiro/cheque \n[ 2 ] à vista no débito\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão "))
if forma == 1:
    print(f"Você ganhou um desconto e sua compra fica por R${valor*0.9:.2f}")
elif forma == 2:
    print(f"Você ganhou um desconto e sua compra fica por R${valor*0.95:.2f}")
elif forma == 3:
    print(f"O valor da sua compra fica por R${valor:.2f} parcelado em 2X de R${valor/2:.2f}")
elif forma == 4:
    parc = int(input("Digite a quantidade de parcelas: "))
    n_valor = valor*1.2
    print(f"O valor da sua compra é R${n_valor:.2f} e estar parcelado em {parc}X de R${(n_valor/parc):.2f}")
else:
    print("Digite apenas as opções : 1, 2, 3 ou 4.")
