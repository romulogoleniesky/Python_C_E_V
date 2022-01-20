#DESAFIO 043 - CALCULANDO O IMC.
peso = float(input("Qual é o seu peso(Kg)? "))
alt = float(input("Qual é a sua altura(m)? "))
imc = peso / (alt**2)
if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}, e você está ABAIXO DO PESO!')
elif 25 > imc > 18.5:
    print(f'Parabéns, seu IMC é {imc:.2f} e você está no PESO IDEAL!')
elif 30 > imc > 25:
    print(f'Seu IMC é {imc:.2f} e você está no SOBREPESO!')
elif 40 > imc > 30:
    print(f'Seu IMC é {imc:.2f} e você está com OBESIDADE!')
else:
    print(f'Seu IMC é {imc:.2f} e você está com OBESIDADE MORBIDA!')
