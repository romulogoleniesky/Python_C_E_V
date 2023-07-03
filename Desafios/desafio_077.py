# DESAFIO 077 : Crie uma tupla com uma lista de nomes, onde cada nome será verificado a existência de vogal.
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
vogais = ('a', 'e', 'i', 'o', 'u')
for palavra in palavras:
    print(f'Na palavra {palavra.upper()} temos', end=' ')
    for letra in palavra:
        if letra in vogais:
            print(f'{letra}', end=' ')
    print(' ')
