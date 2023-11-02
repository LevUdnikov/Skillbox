n = int(input("Количество человек: "))
k = int(input("Какое число в считалке? "))

people = list(range(1, n+1))
i = 0

while len(people) > 1:
    i = (i + k - 1) % len(people)
    print("Выбывает человек под номером", people[i])
    people.pop(i)

print("Остался человек под номером", people[0])