# DESAFIO 25:

# primeira forma:
nome = input('Qual é o seu nome completo?').strip().lower()
print(f'Seu nome tem Silva? ', nome.find('silva') != -1)

#segunda forma:
n = input('Escreva seu nome completo: ').strip().lower()
print(f'Seu nome tem Silva? ', ('silva' in n))
