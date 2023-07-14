# DESAFIO 83:

def forma1():
    expressao = input('Digite uma expressão')
    parentesesa = expressao.count('(')
    parentesesb = expressao.count(')')
    if parentesesa == parentesesb:
        print("Expressão Válida!")
    else:
        print("Expressão inválida!")


# forma1()

def forma2():
    lista = str(input('Digite uma Expressão'))
    pilha = []
    for simbolo in lista:
        if simbolo == '(':
            pilha.append(simbolo)
        elif simbolo == ')':
            if len(simbolo) > 0:
                pilha.pop()
    if len(pilha) == 0:
        print('Expressão Válida!')
    else:
        print('Expressão inválida')


forma2()
print('Fim!')
