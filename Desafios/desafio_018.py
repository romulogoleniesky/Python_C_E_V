# Desafio 18:

import math

ang = float (input("Digite o ângulo que você deseja? "))
rang = math.radians(ang) #tranformando o ângulo para radiano#
print(f"O ângulo {ang:.2f} tem o Seno {math.sin(rang):.2f}")
print(f"O ângulo {ang:.2f} tem o Cosseno {math.cos(rang):.2f}")
print(f"O ângulo {ang:.2f} tem o Tangente {math.tan(rang):.2f}")
