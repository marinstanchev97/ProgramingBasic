city = input()
sales = float(input())
is_input_valid = True
commission = 0

if city == 'Sofia':
    if 0 <= sales <= 500:
        commission = sales * 0.05
    elif 500 < sales <= 1000:
        commission = sales * 0.07
    elif 1000 < sales <= 10000:
        commission = sales * 0.08
    elif sales > 10000:
        commission = sales * 0.12
    else:
        is_input_valid = False

elif city == 'Varna':
    if 0 <= sales <= 500:
        commission = sales * 0.045
    elif 500 < sales <= 1000:
        commission = sales * 0.075
    elif 1000 < sales <= 10000:
        commission = sales * 0.1
    elif sales > 10000:
        commission = sales * 0.13
    else:
        is_input_valid = False

elif city == 'Plovdiv':
    if 0 <= sales <= 500:
        commission = sales * 0.055
    elif 500 < sales <= 1000:
        commission = sales * 0.08
    elif 1000 < sales <= 10000:
        commission = sales * 0.12
    elif sales > 10000:
        commission = sales * 0.145
    else:
        is_input_valid = False
else:
    is_input_valid = False

    if is_input_valid:
        print(f'{commission:.2f}')
    else:
        print('error')