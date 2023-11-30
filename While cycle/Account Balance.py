def main():
    total_amount = 0

    while True:
        try:
            command = input("Въведете сума за вноска или 'NoMoreMoney' за край: ")

            if command == "NoMoreMoney":
                break

            amount = float(command)

            if amount < 0:
                raise ValueError("Invalid operation!")

            total_amount += amount
            print(f"Increase: {amount:.2f}")

        except ValueError as e:
            print(e)
            break

    print(f"Total: {total_amount:.2f}")

if __name__ == "__main__":
    main()







