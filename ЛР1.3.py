list_players = ["Даша", "Витя", "Саша", "Оля", "Кирилл", "Толя"]

#индекс середины
middle_index = len(list_players) // 2

first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

print(first_team)
print(second_team)