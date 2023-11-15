number_of_pages_in_the_book = int(input())
readed_pages_per_hour = int(input())
number_of_days = int(input())

needed_hours_for_whole_book = number_of_pages_in_the_book / readed_pages_per_hour
hours_per_day = needed_hours_for_whole_book / number_of_days
print(int(hours_per_day))
