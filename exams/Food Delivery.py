number_of_chiken_menu = int(input())
number_of_fish_menu = int(input())
number_of_vegge_menu = int(input())

chiken_menu = 10.35
fish_menu = 12.40
vegge_menu = 8.15
delivery_fee = 2.50

order_price = number_of_chiken_menu * chiken_menu + number_of_fish_menu * fish_menu\
              + number_of_vegge_menu * vegge_menu
desert = order_price * 0.2
delivery = 2.5
total_price = order_price + desert + delivery_fee

print(total_price)
