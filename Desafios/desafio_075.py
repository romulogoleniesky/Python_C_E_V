#DESAFIO 075:
numeros = (int(input('Digite um numero: ')), 
                    int(input('Digite outro numero: ')), 
                    int(input('Digite mais um numero: ')), 
                    int(input('Digite o ultimo numero: '))
                    )
print(f'Voce digitou os numeros {numeros} !')
if 9 in numeros:
    print(f'O numero 9 apareceu {numeros.count(9)} vezes.')
    print(f'O numero 9 apareceu na {numeros.index(9) + 1}ª posicao.')
else:
    print(f'O numero 9 não está na lista de numeros.')
for n in numeros :
    if n % 2 == 0:
        print(f'\nO {n} é par !', end=' ')
