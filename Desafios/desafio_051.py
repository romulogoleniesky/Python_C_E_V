#Desafio 015

# PRIMEIRA MANEIRA:
print("=="*20), print("       Os 10 termos de uma PA "), print("=="*20)
p = int(input("Digite o Primeiro Termo: "))
r = int(input("Digite a Razão: "))
for i in range(1, 11):
    print(p, end=" > ")
    p += r
print("ACABOU")

print("  ")

#SEGUNDA MANEIRA:
print("=="*20), print("       Os 10 termos de uma PA "), print("=="*20)
p = int(input("Digite o Primeiro Termo: "))
r = int(input("Digite a Razão: "))
d = p + (10-1)* r
for i in range(p, d, r):
    print(i, end=" > ")
print("ACABOU")

