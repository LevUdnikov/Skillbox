while True:
    password = input("Придумайте пароль: ")
    length = len(password)
    capitalized_letter = len([char for char in password if char.isupper()])
    digit_count = len([char for char in password if char.isdigit()])
    if length >= 8 and capitalized_letter > 0 and digit_count >= 3:
        print("Это надёжный пароль.")
        break
    else:
        print("Пароль ненадёжный. Попробуйте ещё раз.")