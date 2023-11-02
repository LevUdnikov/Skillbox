players = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]

first_day = []
for player_id in range(0, len(players), 2):
    first_day.append(players[player_id])

print(first_day)
