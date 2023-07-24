# DESAFIO 84:


""" # PRIMEIRA FORMA
pessoas = []
maior_peso = 0
menor_peso = 200
mais_pesado = ''
mais_leve = ''
quit = 's'
while quit in 'sS':
    nome = input('Nome: ')
    peso = int(input('Peso: '))
    if maior_peso < peso:
        maior_peso = peso
        mais_pesado = nome
    elif menor_peso > peso:
        menor_peso = peso 
        mais_leve = nome
    pessoas.append([nome,peso])
    quit = str(input('Deseja continuar? (S/N) '))
print(f'{"PESSOAS":-^60}')
print(pessoas)
print('=-'*30)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O menor peso foi de {mais_leve} com {menor_peso} Kg.')
print(f'O maior peso foi de {mais_pesado} com {maior_peso} Kg.')     """

temp = []
princ = []
mai = men = 0 
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ)==0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer Continuar? [S/N]'))
    if resp in 'nN':
        break
print(f'{"PESSOAS":-^60}')
print(f'Ao todo foram cadastradas {len(princ)} pessoas.')
print(f'O maior pesso foi de {mai} kg. de', end='')
for p in princ:
    if p[1] == mai:
        print(f' {p[0]},', end='')
print('')
print(f'O menor peso foi de {men} kg. de', end='')
for p in princ:
    if p[1] == men:
        print(f' {p[0]},',end='')
