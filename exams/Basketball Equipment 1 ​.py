annual_tax = int(input())
sneakers_price = annual_tax * 0.60  # sneakers_price = annual_tax  - annual * 40 / 100
equipment_price = sneakers_price * 0.80  # equipment_price = sneakers_price  - sneakers_price * 20 / 100
ball_price = equipment_price / 4
accessories_price = ball_price / 5
total_sum = annual_tax \
            + sneakers_price \
            + equipment_price \
            + ball_price \
            + accessories_price
print(total_sum)