def main():
    max_number = float('-inf')

    while True:
        user_input = input()

        if user_input.lower() == "stop":
            break

        try:
            number = int(user_input)
            max_number = max(max_number, number)
        except ValueError:
            print()

    if max_number != float('-inf'):
        print(f"{max_number}")
    else:
        print()

if __name__ == "__main__":
    main()
