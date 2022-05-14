# DESAFIO 58:
import random
tent = 1
print("#*"*10, "JOGO DA ADVINHAÇÃO", "#*"*10)
jog = int(input("Pense em um número entre 0 e 10"))
n = int(random.randint(0, 10))
while n != jog:
    if jog < n:
        jog = int(input("Mais... Tente novamente: "))
    else:
        jog = int(input("Menos... Tente novamente: "))
    tent += 1
print(f"Parabéns, você acertou com {tent} tentativas, o número foi {n}!!")
