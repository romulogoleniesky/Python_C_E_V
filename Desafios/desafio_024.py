# DESAFIO 24
""" PRIMEIRA IDEIA
cidade = input('Em qual cidade você nasceu? ').strip().lower()
n = cidade.find(' ')
firstname = cidade[0:n]
print(firstname == "santo")"""

cid = input('Em que cidade você nasceu? ').strip().lower()
print(cid[:5]=='santo')
