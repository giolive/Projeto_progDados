## Modulo para calculo de porcentagem para jogos de idioma portugues.
## Reutilizei ideias do modulo percentage

def idioma_percentages(games):
    languageP_count = 0
    port2020_count = 0

    for game in games:
        if 'Portuguese - Brazil' in game['language']:
            languageP_count += 1
            if game ['release_date']!= '':
                  year = game ['release_date'].split(',')[1].strip()
                  if year >= '2020':
                      port2020_count += 1

    total_games = len(games)
    if total_games == 0:
        return 0, 0

    languageP_percent = (languageP_count / total_games) * 100
    port2020_percent = (port2020_count / total_games) * 100
    
    return languageP_percent, port2020_percent
