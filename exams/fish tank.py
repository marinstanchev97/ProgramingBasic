length = int(input())
width = int(input())
height = int(input())
percent_non_free_volume = float(input())
fish_tank_volume_in_centimeters = length * width * height
fish_tank_volume_in_liters = fish_tank_volume_in_centimeters * 0.001 # / 1000 -> /10/10/10
percentage = percent_non_free_volume * 0.01 # / 100
needed_liters = fish_tank_volume_in_liters * (1 - percentage)
print(needed_liters)