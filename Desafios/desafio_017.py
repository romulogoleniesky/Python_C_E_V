# Trigonometria com python
import math
# primeira forma.
CO= float(input('Comprimento do cateto oposto: '))
CA= float(input('Comprimento do cateto adjacente: '))
hip= math.sqrt(CO**2+CA**2)
print(f'A hipotenusa vai medir : {hip:.2f}')

# segunda forma.
CO= float(input('Comprimento do cateto oposto: '))
CA= float(input('Comprimento do cateto adjacente: '))
hi= math.hypot(CO, CA)
print(f'A hipotenusa vai medir : {hi:.2f}')