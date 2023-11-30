def main():
    username = input()
    password = input()

    login_password = input()

    while login_password != password:
        login_password = input()

    print(f"Welcome {username}!")

if __name__ == "__main__":
    main()



