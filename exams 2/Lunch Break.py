import math

# Вход
serial_name = input()
episode_duration = int(input())
break_duration = int(input())

# Изчисляваме времето за обяд и времето за отдих
lunch_time = break_duration / 8
rest_time = break_duration / 4

# Общото време, което ще отделите за гледане на епизода
total_watch_time = break_duration - (lunch_time + rest_time)

# Проверка дали имате достатъчно време за гледане на епизода
if total_watch_time >= episode_duration:
    left_time = math.ceil(total_watch_time - episode_duration)
    print(f"You have enough time to watch {serial_name} and left with {left_time} minutes free time.")
else:
    needed_time = math.ceil(episode_duration - total_watch_time)
    print(f"You don't have enough time to watch {serial_name}, you need {needed_time} more minutes.")
