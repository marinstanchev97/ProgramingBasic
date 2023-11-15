fruit = input()
day_of_week = input()
quantity = float(input())
total = 0
is_input_valid = True
if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' \
  or day_of_week == 'Friday':
    if fruit == 'banana':
        total = quantity * 2.5
    elif fruit == 'apple':
        total = quantity * 1.20
    elif fruit == 'orange':
        total = quantity * 0.85
    elif fruit == 'grapefruit':
        total = quantity * 1.45
    elif fruit == 'kiwi':
        total = quantity * 2.70
    elif fruit == 'pineapple':
        total = quantity * 5.50
    elif fruit == 'grapes':
        total = quantity * 3.85
    else:
        is_input_valid = False

elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
    if fruit == 'banana':
        total = quantity * 2.70
    elif fruit == 'apple':
        total = quantity * 1.25
    elif fruit == 'orange':
        total = quantity * 0.90
    elif fruit == 'grapefruit':
        total = quantity * 1.60
    elif fruit == 'kiwi':
        total = quantity * 3.00
    elif fruit == 'pineapple':
        total = quantity * 5.60
    elif fruit == 'grapes':
        total = quantity * 4.20
    else:
        is_input_valid = False
else:
    is_input_valid = False

if not is_input_valid:
    print('error')
else:
    print(f'{total:.2f}')

