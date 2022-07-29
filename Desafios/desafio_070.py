# DESAFIO 070:
print("*"*50)
print('{:-^50}'.format(" Loja Super Baratão "))
print("*"*50)
total_da_compra = mais_de_mil = prec_barato = 0
prod_barato = " "
while True:

    nome = str(input("Nome do Produto: "))
    preco = float(input("Preço: "))
    if total_da_compra == 0:
        prec_barato = preco
    else:
        if preco < prec_barato:
            prec_barato = preco
            prod_barato = nome
    total_da_compra += preco
    if preco > 1000:
        mais_de_mil += 1

    continuar = " "
    while continuar not in "sSnN":
        continuar = str(input("Deseja continuar? [S/N]" )).strip().upper()[0]
    if continuar == "N":
        break
print(f"""Total da compra R${total_da_compra:.2f}
Temos {mais_de_mil} produtos custando mais de R$1000.00
O produto mais barato foi {prod_barato} custando R${prec_barato:.2f} 
""")
