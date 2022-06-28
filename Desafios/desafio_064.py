# DESAFIO 64:
contador = 0
total = 0
senha = int(input("Digite a senha 999 para sair:"))

while senha != 999:
    contador += 1
    senha = int(input("Digite a senha 123 para sair: "))
    total += senha

print(f"Você digitou {contador} números e a soma deles é {total}")
print("FIM!!!")
