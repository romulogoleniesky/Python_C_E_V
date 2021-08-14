# AULA 10 - CONDIÇÕES,  IF, ELSE, ELIF:

# BLOCO DE CONDIÇÕES - FORMA TRADICIONAL:

idade = int(input('Qual a sua idade? '))
if idade <= 17:
    print('Você é menor de idade!')
else:
    print('Você é maior de idade!')
print("____FIM____")

# BLOCO DE CONDIÇÕES - RESUMIDA EM UMA LINHA:

id = int(input('Qual é a sua idade? '))
print('Você é menor!' if id <= 17 else'Você é maior!')
