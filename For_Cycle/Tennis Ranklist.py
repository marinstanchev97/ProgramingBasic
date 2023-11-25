number_of_tournaments = int(input())
start_points = int(input())
total_points = 0
tournaments_won = 0
for tournament in range(number_of_tournaments):
    position = input()
    if position == "W":
        total_points += 2000
        tournaments_won += 1
    elif position == "F":
        total_points += 1200
    elif position == "SF":  # else
        total_points += 720
average_points = total_points // number_of_tournaments
total_points += start_points
won_tournaments_percent = tournaments_won / number_of_tournaments * 100
print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{won_tournaments_percent:.2f}%")