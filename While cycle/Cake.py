width = int(input())
length = int(input())

total_cake_pieces = width * length
cake_taken = 0

while True:
    command = input()
    if command == "STOP":
        break
    cake_taken += int(command)

    if cake_taken > total_cake_pieces:
        pieces_needed = cake_taken - total_cake_pieces
        print(f"No more cake left! You need {pieces_needed} pieces more.")
        break

if cake_taken <= total_cake_pieces:
    pieces_left = total_cake_pieces - cake_taken
    print(f"{pieces_left} pieces are left.")
