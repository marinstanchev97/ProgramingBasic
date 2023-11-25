number_of_groups = int(input())
musala_climbers = 0
montblanc_climbers = 0
kilimanjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0
for current_group in range(number_of_groups):
    current_group_climbers = int(input())
    if current_group_climbers <= 5:
        musala_climbers += current_group_climbers
    elif current_group_climbers <= 12:
        montblanc_climbers += current_group_climbers
    elif current_group_climbers <= 25:
        kilimanjaro_climbers += current_group_climbers
    elif current_group_climbers <= 40:
        k2_climbers += current_group_climbers
    elif current_group_climbers >= 41:  # else
        everest_climbers += current_group_climbers
total_climbers = musala_climbers \
                 + montblanc_climbers \
                 + kilimanjaro_climbers \
                 + k2_climbers \
                 + everest_climbers
percentage_musala_climbers = musala_climbers / total_climbers * 100
percentage_montblanc_climbers = montblanc_climbers / total_climbers * 100
percentage_kilimanjaro_climbers = kilimanjaro_climbers / total_climbers * 100
percentage_k2_climbers = k2_climbers / total_climbers * 100
percentage_everest_climbers = everest_climbers / total_climbers * 100
print(f"{percentage_musala_climbers:.2f}%")
print(f"{percentage_montblanc_climbers:.2f}%")
print(f"{percentage_kilimanjaro_climbers:.2f}%")
print(f"{percentage_k2_climbers:.2f}%")
print(f"{percentage_everest_climbers:.2f}%")