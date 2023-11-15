budget = float(input())
number_of_video_cards = int(input())
number_of_processors = int(input())
number_of_ram_memories = int(input())
all_video_cards_price = number_of_video_cards * 250   # price per one GPU
one_processor_price = all_video_cards_price * 0.35
all_processors_price = number_of_processors * one_processor_price
one_ram_memory_price = all_video_cards_price * 0.10
all_ram_memories_price = number_of_ram_memories * one_ram_memory_price
needed_money = all_video_cards_price \
               + all_ram_memories_price \
               + all_processors_price
if number_of_video_cards > number_of_processors:
    needed_money *= 0.85
difference = abs(budget - needed_money)
if budget >= needed_money:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")







