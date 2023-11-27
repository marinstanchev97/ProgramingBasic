def main():
    target_sum = int(input())
    current_sum = 0

    while current_sum < target_sum:
        number = int(input())
        current_sum += number

    print(f"{current_sum}")

if __name__ == "__main__":
    main()

