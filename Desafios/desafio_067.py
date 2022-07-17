# DESAFIO 067
n = int(input("Quer ver a tabuada de qual valor? "))
while True:
    if n < 0:
        break
    for i in range(1, 11):
        print(f"{i} x {n} = {i*n}")
    n = int(input("Quer ver a tabuada de qual valor? "))
print("Valor Negativo! "
      "FIM!")
