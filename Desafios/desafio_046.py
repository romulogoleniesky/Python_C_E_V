# CONTAGEM REGRESSIVA:
import time
import emoji
print("@*"*20)
print(" "*10,"CRONOMETRO")
print("@*"*20)
n = int(input("QUANTOS SEGUNDOS? "))
for i in range(n, 0, -1):
    print(emoji.emojize(f'{i}:bomb:'))
    time.sleep(0.9)
print(emoji.emojize(":anger_symbol:"))
