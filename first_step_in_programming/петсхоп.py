def calculate_result(cats_food_count_input, dogs_food_count_input):
    return f"{cats_food_count_input * 4.0 + dogs_food_count_input * 2.5} lv."


dogs_food_count = int(input())
cats_food_count = int(input())

print(calculate_result(cats_food_count, dogs_food_count))

