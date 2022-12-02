f = open("input.txt", 'r')
game = f.read().splitlines()
f.close()

game = [game_round.split() for game_round in game]
game = [(ord(player1) - ord('A') + 1, ord(player2) - ord('X') + 1) for player1, player2 in game]

scored_points = 0
scored_points_part_2 = 0
game_conditions_part1 = {(1, 2), (2, 3), (3, 1)}
game_conditions_part2 = [[2, 3, 1], [3, 1, 2]]

for p1, p2 in game:
    scored_points += p2
    if p1 == p2:
        scored_points += 3
    elif (p1, p2) in game_conditions_part1:
        scored_points += 6
    if p2 == 1:
        scored_points_part_2 += game_conditions_part2[1][p1 - 1]
    elif p2 == 2:
        scored_points_part_2 += 3 + p1
    elif p2 == 3:
        scored_points_part_2 += 6 + game_conditions_part2[0][p1 - 1]

print('Final score Part 1:', scored_points)
print('Final score Part 2:', scored_points_part_2)
