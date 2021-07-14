# DESAFIO 022:
nome = input("Escreva seu nome completo:")
n_ok = nome.strip()
letras = len(n_ok) - n_ok.count(" ")
nomeSplitado = n_ok.split()
print(f"Nome todo em maiúsculo: ", n_ok.upper())
print(f"Nome todo em minúsculo: ", n_ok.lower())
print(f"Seu nome completo tem {letras} letras.")
print(f"Seu primeiro nome tem {len(nomeSplitado[0])} letras.")
