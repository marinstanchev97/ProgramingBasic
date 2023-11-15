record_seconds = float(input())
distance_meters = float(input())
time_per_meter_seconds = float(input())

# Изчисления
water_resistance = (distance_meters // 15) * 12.5  # Съпротивлението на водата
total_time = distance_meters * time_per_meter_seconds + water_resistance  # Общото време в секунди

# Проверка дали е подобрен Световния рекорд
if total_time < record_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    time_difference = total_time - record_seconds
    print(f"No, he failed! He was {time_difference:.2f} seconds slower.")


