import csv
from calculos.percentage import game_percentages
from idioma.idioma import idioma_percentages
from collections import Counter

## Iniciando importação do arquivo csv com o csv reader
## Após multiplas tentativas, precisei deixar apenas os primeiros 80 jogos pois o csv inteiro é muito grande.

with open('steam_games.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  next(csv_reader)
  lines = [[element.strip() for element in row] for row in csv_reader]

#print(lines)

## Lista com as categorias que preciso para as perguntas
games = [
  {
      'id': line[0],
      'name': line[1],
      'release_date': line[2],
      'price': float(line[6]),
      'language' : line[9]
  }
  for line in lines
]

## Testando com o primeiro jogo e colocando exceção caso a lista não esteja funcionando

if len(games) > 0:
  primeiro = games[0]['name']
  preco1 = games[0]['price']
  lang = games[0]['language']
  print("Primeiro da lista: ", primeiro, "Preço: ", preco1, "Idiomas: ", lang)
else:
  raise Exception ("No game available")

## Perguntas
## Qual o percentual de jogos gratuitos e pagos na plataforma?

free_percentage, pago_percentage = game_percentages(games)
print(f"Percentual de jogos gratuitos: {free_percentage:.2f}%")
print(f"Percentual de jogos pagos: {pago_percentage:.2f}%")

## Qual o ano com maior número de jogos novos?
year_count = Counter()

for game in games:
  #print (game['release_date']) ##Teste so pra ver se aparecem as datas
  
  release_date = game['release_date']
  if release_date != '':
      year = release_date.split(',')[1].strip()  
      year_count[year] += 1
  else:
    if not games:
        raise Exception("No game available")

if year_count:
  most_common_years = [year for year, count in year_count.most_common() if count == year_count.most_common(1)[0][1]]
  print("O(s) ano(s) com maior número de jogos novos:", ", ".join(most_common_years))
else:
  print("ERRO, nenhum ano encontrado na contagem")

## Percentual de jogos que possuem Portugues ( Portuguese - Brazil) como idioma suportado. Considerando principalmente os últimos 5 anos.
languageP_percent, port2020_percent = idioma_percentages(games)
print(f"Percentual do total de jogos com Portugues como idioma suportado: {languageP_percent:.2f}%")
print(f"Percentual de jogos com Português, lançados nos últimos 5 anos: {port2020_percent:.2f}%")
