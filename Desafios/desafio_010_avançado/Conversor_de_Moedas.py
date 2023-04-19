import requests
from BeautifulSoup import *
url = "https://economia.uol.com.br/cotacoes/cambio/"
req = requests.get(url)
print(req.content)

soup = BeautifulSoup(req.content, 'html.paser')
preco = soup.find_all('div', class_='value')
