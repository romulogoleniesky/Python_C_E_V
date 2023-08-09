# DESAFIO 93
jogador = {
    "Nome": '',
    "Gols": [],
    "Total de Partidas": 0}
jogador["Nome"] = input("Nome do jogador:  ")
jogador["Total de Partidas"] = int(input(f"Quantas partidas {jogador['Nome']} jogou?  "))
for n in range(jogador["Total de Partidas"]):
    jogador["Gols"].append(int(input(f"Quantos gols na {n+1}ª partida ?  ")))
print("-="*30)
print(jogador)
print("=-"*30)
for k, v in jogador.items():
    print(f"  -- No campo {k} tem o valor {v} ! --")
print(
    f" -- O jogador {jogador['Nome']} jogou {jogador['Total de Partidas']} partidas --")
for k, v in enumerate(jogador["Gols"]):
    print(f"    => Na {k+1}ª partida, fez {v} gols! ")
print(f" -- Houve um total de {sum(jogador['Gols'])} gols! --")
