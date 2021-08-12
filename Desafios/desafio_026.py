# DESAFIO 26.

frase = input('Digite uma frase: ').strip().lower()
print(f'Nesta frase temos {frase.count("a")} a.')
print(f'O primeiro a se encontra na posição {frase.find("a")+1}')
print(f'O último a se encontra na posição {frase.rfind("a")+1}')
