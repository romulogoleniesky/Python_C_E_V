# DESAFIO 42 - ANALISADOR DE TRIANGULOS-parte 2:
import time
print("=-"*30)
print("              ANALISADOR DE TRIÂNGULOS ")
print("=-"*30)
a = float(input("Entre com o primeiro segmento de reta: "))
b = float(input("Entre com o segundo segmento de reta: "))
c = float(input("Entre com o terceiro segmento de reta: "))
print("Analisando os segmentos...")
time.sleep(2)
if a+b > c and b+c > a and a+c > b:
    res = "FORMAM UM TRIÂNGULO"
    if a == b == c:
        res = "FORMAM UM TRIÂNGULO EQUILÁTERO"
    elif a != b != c != a:
        res = "FORMAM UM TRIÂNGULO ESCALENO"
    else:
        res = "FORMAM UM TRIÂNGULO ISOCELES"

else:
    res = "NÃO FORMAM UM TRIÂNGULO."
print("=-"*30)
print(f"OS SEGMENTOS {res}.")
print("=-"*14, "FIM", "=-"*14)
