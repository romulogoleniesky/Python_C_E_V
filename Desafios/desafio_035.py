# DESAFIO 35 - ANALISADOR DE TRIANGULOS:
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
    res = "FORMAM"
else:
    res = "NÃO FORMAM"
print("=-"*30)
print(f"OS SEGMENTOS {res} UM TRIÂNGULO.")
print("=-"*14, "FIM", "=-"*14)


