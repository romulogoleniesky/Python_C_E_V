#DESAFIO 031.
# PRIMEIRA MANEIRA:
d = float(input('Qual a distância da sua viagem? '))
preco = 0
if d <= 200:
    preco = d * 0.5
else:
    preco = d * 0.45

print(f'Você está prestes a começar uma viagem de {d:.2f}KM.')
print(f'O preço da passagem será de R${preco:.2f}:')

#SEGUNDA MANEIRA:
dis=float(input("Qual a distância da sua viagem? "))
valor= dis*0.5 if dis <=200 else dis*0.45

print(f'Você está prestes a começar uma viagem de {dis:.2f}KM.')
print(f'O preço da passagem será de R${valor:.2f}:')
