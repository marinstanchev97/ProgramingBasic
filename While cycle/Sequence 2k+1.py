def main():
    n = int(input())

    if n < 1:
        print()
        return

    current_number = 1

    while current_number <= n:
        print(current_number)
        current_number = current_number * 2 + 1

if __name__ == "__main__":
    main()

