# Preço do aluguel de carros:
dia = float(input('Quantos dias alugado?: '))
km = float(input('Quantos KM rodados?: '))
aluguel = (60*dia)+(0.15*km)
print(f'O total à pagar é : R$ {aluguel:.2f}')
