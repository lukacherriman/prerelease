def process(p, table):
    print(p)
    if table[p-1][1] != 0:
        process(table[p-1][1], table)

    print(table[p-1][0])
    if table[p-1][2] != 0:
        process(table[p-1][2], table)


table = [["Jones", 3, 2],
         ["Smith", 0, 0],
         ["Bremner", 5, 4],
         ["Fortune", 0, 0],
         ["Bird", 0, 0]]

player_one_score = 0
player_two_score = 0
no_of_games_in_match = int(input("How many games? "))

for no_of_games_played in range(1, no_of_games_in_match + 1):
    player_one_wins_game = input("Did player one win the game (enter Y or N): ")
    if player_one_wins_game == "Y":
        player_one_score += 1
    else:
        player_two_score += 1
print(player_one_score)
print(player_two_score)

