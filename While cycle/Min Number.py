def main():
    min_number = float('inf')

    while True:
        user_input = input()

        if user_input.lower() == "stop":
            break

        try:
            number = int(user_input)
            min_number = min(min_number, number)
        except ValueError:
            print()

    if min_number != float('inf'):
        print(f"{min_number}")
    else:
        print()

if __name__ == "__main__":
    main()
