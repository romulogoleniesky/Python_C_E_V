#DESAFIO 73:
times = ('Palmeiras', 'Fluminense', 'Internacional', 'Flamengo', 'Corinthians', 'Athletico-PR', 'América-MG', 'Atlético-MG', 'São Paulo', 'Fortaleza', 'Botafogo', 'Santos', 'Bragantino', 'Goiás', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
def colocacao():
    print("Classificação do Campeonato Brasileiro:")
    for num, i in enumerate(times):
        print(f"{num+1}°-{times[num]}", end=", ")
def cinco():
    print("Os 5 primeiros são: ")
    for i in range(0, 5):
        print(f"{i+1}º-{times[i]}", end=", ")
def lanterna():
    print("Os 4 times na Lanterna são: ")
    for a in range(-1, -5, -1):
        print(f"{len(times)+(a+1)}º-{times[a]}", end=", ")
def ordem():
    print("Classificação em Ordem Alfabética:")
    for t in (sorted(times)):
        print(f"{t}", end=", ")

colocacao()
print("\n"+"**"*30)
cinco()
print("\n"+"**"*30)
lanterna()
print("\n"+"**"*30)
ordem()
print("\n"+"**"*30)
print(f"O São Paulo está na {times.index('São Paulo')+1}ª Posição")
