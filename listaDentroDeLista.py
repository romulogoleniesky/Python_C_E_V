# MUNDO 3 - AULA 17 : Exemplo de lista dentro de lista.
pessoas = []
dados = ('Pedro',25)
pessoas.append(dados[:]) # Fatiamento completo da extrutura.
print(dados)
print(pessoas)
pessoas.append(['Maria',53])
pessoas.append(['João',30])
print(pessoas)
print(pessoas[2][1])

