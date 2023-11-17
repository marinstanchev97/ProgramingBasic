month = input()
number_overnight = int(input())
studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if 7 < number_overnight <= 14:
        studio *= 0.95
    elif number_overnight > 14:
        studio *= 0.70
        apartment *= 0.90
elif month == "June" or month == "September":
        studio = 75.20
        apartment = 68.70
        if number_overnight > 14:
            studio *= 0.80
            apartment *= 0.90
elif month == "July" or month == "August":
            studio = 76
            apartment = 77
            if number_overnight > 14:
                apartment *= 0.90
price_studio = number_overnight * studio
price_apartment = number_overnight * apartment
print(f'Apartment: {price_apartment:.2f} lv.')
print(f'Studio: {price_studio:.2f} lv.')




