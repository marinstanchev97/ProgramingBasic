number_stacks_of_pens = int(input())
number_stacks_of_markers = int(input())
litters_of_detergent = int(input())
discount_percent = int(input())

price_per_pen = 5.80
price_per_marker = 7.20
price_of_detergent = 1.20

needed_sum = number_stacks_of_pens * price_per_pen + \
            number_stacks_of_markers * price_per_marker + \
            litters_of_detergent * price_of_detergent
needed_sum = needed_sum - needed_sum * discount_percent / 100
print(needed_sum)

