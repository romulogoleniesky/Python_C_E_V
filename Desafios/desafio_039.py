from datetime import date
ano = date.today().year
nasc = int(input("Qual o seu ano de nascimento? "))
if ano-nasc == 18:
    print("Você precisa se alistar imediatamente!")
elif ano-nasc > 18:
    print(f"Você esta atrasado {(ano-nasc)-18} anos, seu ano de alistamento foi em {nasc+18}")
elif ano-nasc < 18:
    print(f"Você vai se alistar em {nasc+18}, daqui à {18-(ano-nasc)}")
