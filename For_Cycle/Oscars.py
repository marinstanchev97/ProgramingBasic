actor_name = input()
academy_points = float(input())
judges_count = int(input())

total_points = academy_points

for _ in range(judges_count):
    judge_name = input()
    judge_points = float(input())

    current_points = len(judge_name) * judge_points / 2
    total_points += current_points

    if total_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break

if total_points <= 1250.5:
    needed_points = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")
