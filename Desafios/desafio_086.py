# DESAFIO 086 - MATRIZ

# PRIMEIRO FORMATO:

matriz = [
    [[], [], []],
    [[], [], []],
    [[], [], []]
]
for n in range(3):
    for m in range(3):
        valor = int(input(f'Digite um valor para [{n},{m}]: '))
        matriz[n][m].append(valor)
print('=-'*30)
print(f"""
[ {matriz[0][0]} ][ {matriz[0][1]} ][ {matriz[0][2]} ]
[ {matriz[1][0]} ][ {matriz[1][1]} ][ {matriz[1][2]} ]
[ {matriz[2][0]} ][ {matriz[2][1]} ][ {matriz[2][2]} ]
""")
