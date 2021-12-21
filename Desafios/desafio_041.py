import datetime
ano = (datetime.datetime.now()).year
nasc = int(input("Digite o seu ano de nascimento: "))
categoria = 0
if (ano - nasc) <= 9:
    categoria = str("MIRIM")
elif 9 < (ano - nasc) <= 14:
    categoria = str("INFANTIL")
elif 14 < (ano - nasc) <= 19 :
    categoria = str("JUNIOR")
elif 19 < (ano - nasc) <= 25:
    categoria = str("SÊNIOR")
else:
    categoria = str("MASTER")
print(f"A categoria do atleta é {str(categoria)}.")

