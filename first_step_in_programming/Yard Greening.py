square_meters_for_land_scaping = float(input())

price_for_land_scaping_the_whole_yard = square_meters_for_land_scaping * 7.61
discount_for_landscaping = price_for_land_scaping_the_whole_yard * 0.18
total_sum_for_landscaping = price_for_land_scaping_the_whole_yard - discount_for_landscaping

print(f'The final price is: {total_sum_for_landscaping} lv.')
print(f'The discount is: {discount_for_landscaping} lv.')


