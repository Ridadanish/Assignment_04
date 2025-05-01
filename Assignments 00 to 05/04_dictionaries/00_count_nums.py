def get_user_numbers():
    user_num = []

    while True:
        user_input = input('Enter a number')

        if user_input == "":
            break

        num = int(user_input)
        user_num.append(num)
    return user_num
        