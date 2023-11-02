guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]
action = ""

while action != "Пора спать":
    print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
    action = input("Гость пришёл или ушёл? ")

    if action == "пришёл":
        guest_name = input("Имя гостя: ")
        if len(guests) <= 5:
            guests.append(guest_name)
        else:
            print("Прости, Гоша, но мест нет.")
    elif action == "ушёл":
        guest_name = input("Имя гостя: ")
        guests.remove(guest_name)
        print(f"Пока, {guest_name}!")
print("Вечеринка закончилась, все легли спать.")