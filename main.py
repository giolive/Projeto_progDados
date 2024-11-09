import csv

##Iniciando importação do arquivo csv com o csv reader
##comecei com um arquivo com apenas 30 linhas pois o csv inteiro é muito grande.
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
      'price': line[7],
      'supLanguage': line[10],
      'audio': line[11]
  }
  for line in lines
]

# Testando com o primeiro jogo
primeiro = games[0]['name'] if len(games) > 0 else "No game available"
print("First game: ", primeiro)

