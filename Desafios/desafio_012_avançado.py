# DESAFIO 12 AVANÇADO
preco = float(input('Qual é o preço do produto? R$'))
desconto = float(input('Qual é o desconto? %'))
pfinal = preco - (preco*desconto)/100
print(f'Preço com desconto de {desconto:.0f}% é R${pfinal:.2f} ')
