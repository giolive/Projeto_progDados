## Modulo para calculo de porcentagem para jogos de idioma portugues.
## Reutilizei ideias do modulo percentage
def idioma_percentages(games):
  audioP_count = 0
  languageP_count = 0

  for game in games:
      if 'Portuguese - Brazil' in game['supLanguage']:
          languageP_count += 1
      if 'Portuguese - Brazil' in game['audio']:
          audioP_count += 1

  total_games = len(games)
  if total_games == 0:
      return 0, 0

  languageP_percent = (languageP_count / total_games) * 100
  audioP_percent = (audioP_count / total_games) * 100

return languageP_percent, audioP_percent
