# DESAFIO 036 - APROVAÇÃO DE FINANCIAMENTO:
print('Olá, vamos simular um Financiamento? ')
casa = float(input('Qual o valor da casa? '))
sal = float (input('Qual o valor do seu salário? '))
anos = int(input('Em quantos anos você gostaria de pagar? '))
parcela = casa / (anos*12)
print(f'As parcelas ficaram em {anos*12}x de R${parcela:.2f}')
if parcela <= sal*0.3:
    print('Seu Financiamento foi aprovado!!')
else:
    print('Infelizmente seu Financiamento não foi aprovado!')
