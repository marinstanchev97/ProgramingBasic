# Четене на входните данни от потребителя
budget = float(input())
season = input()

destination = ""
vacation_type = ""
spent_money = 0

# Определяне на дестинацията и изхарчените средства според бюджета и сезона
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        vacation_type = "Camp"
        spent_money = budget * 0.30
    elif season == "winter":
        vacation_type = "Hotel"
        spent_money = budget * 0.70
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        vacation_type = "Camp"
        spent_money = budget * 0.40
    elif season == "winter":
        vacation_type = "Hotel"
        spent_money = budget * 0.80
elif budget > 1000:
    destination = "Europe"
    vacation_type = "Hotel"
    spent_money = budget * 0.90

# Отпечатване на резултата
print(f"Somewhere in {destination}")
print(f"{vacation_type} - {spent_money:.2f}")
