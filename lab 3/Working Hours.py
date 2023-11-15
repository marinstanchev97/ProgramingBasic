hour = int(input())
day_of_week = input()
user_output = ''

if day_of_week == 'Sunday':
    user_output = 'closed'
else:
    if hour >= 10 and hour <= 18:
        user_output = 'open'
    else:
        user_output = 'closed'

print(user_output)

