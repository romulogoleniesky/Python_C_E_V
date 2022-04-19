# DESAFIO 053.
frase = input("Digite uma frase: ").strip().upper()
palavras = frase.split()
n = "".join(palavras)
palavras2 = []
for i in range(len(n)-1, -1, -1):
    palavras2 += n[i]
n2 = "".join(palavras2)
if n == n2:
    print(f"A frase é um Palindromo: {n} e {n2}.")
else:print(
    f" A Frase não é um Palindromo: {n} e {n2}."
)
