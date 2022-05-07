# DESAFIO 054:
import datetime
data = datetime.datetime.now()
maior = 0
menor = 0
ano = []
for n in range(1, 8):
    ent = int(input(f"Em que ano a {n}ª pessoa nasceu? "))
    ano.append(ent)
for i in ano:
    if (data.year - i) >= 18:
        maior += 1
    else:
        menor += 1
print(f"Temos {maior} pessoas maiores de idade e {menor} de menor.")