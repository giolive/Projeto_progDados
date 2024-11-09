## Colocar o calculo em módulo para melhorar a reutilização e compreensão.

def game_percentages(games):
  free_games_count = 0
  pago_games_count = 0

  for game in games:
      if game['price'] == 0:
          free_games_count += 1
      else:
          pago_games_count += 1
  total_games = len(games)
  if total_games == 0:
      return 0, 0  # divisão por 0

  free_percentage = (free_games_count / total_games) * 100
  pago_percentage = (pago_games_count / total_games) * 100

  return free_percentage, pago_percentage
