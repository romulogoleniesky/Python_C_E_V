# Fatiando strings

frase = str(input('Escreva uma frase: '))
print(f'Temos na posição 5 o caractere: {frase[4]}')
print(f'Entre o segundo e quinto caractere temos: {frase[2:6]}')
print(f'Todos os caracteres pulando de 2 em 2 são:{frase[0::2]}')
print(f'Essa frase tem {frase.count("a")} letras "a".')
print(f'Essa frase tem {len(frase)} caracteres.')
print(f'O trecho "ão" está em: {frase.find("ão")}')
print(f'Temos a palavra maçã? {frase.find("maçã")}')
print(f'Vamos trocar a palavra laranja por maçã: {frase.replace("laranja","maçã")}')
print(f'Temos a palavra maçã?{"maçã" in frase}')
print(f'A frase toda em maiúsculo: {frase.upper()}')
print(f'A frase toda em minúsculo: {frase.lower()}')
print(f'Capitalizando{frase.capitalize()}')
print(f'Titulos: {frase.title()}')