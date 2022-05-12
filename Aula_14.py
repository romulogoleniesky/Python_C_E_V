# Aula 14 - While
import time

c = int (input("DIGITE UM NÚMERO: "))
while c != 0:
    print(f" ({c}) zerando .. .")
    c -= 1
    time.sleep(1)
print("ZEROOU!!! FIM!")
