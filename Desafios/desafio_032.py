#DESAFIO 032:
from datetime import date
print("Olá, vamos analisar se o ano é BISEXTO.")
ano = int(input("Digite o ano para ser analisado:  "))
if ano==0:
    ano = date.today().year
M4 = ano%4
M100 = ano%100
M400 = ano%400
if M4 == 0 and M100 != 0 or M400 == 0:
    res = "É BISEXTO"
else:
    res = "NÃO É BISEXTO"
print(F'O ano de {ano}, {res}!')
