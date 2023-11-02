# Реализуйте программу,
# которая получает на вход четырёхзначное число
# и выводит на экран каждую его цифру отдельно
# (в одну строчку либо каждая цифра в новой строчке).
# Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
# Однако можно использовать сколько угодно переменных

number = int(input("Введите число: "))
last_number = number % 10
third_number = (number - last_number) // 10 % 10
second_number = (number - third_number * 10 - last_number) // 100 % 10
first_number = (number - second_number * 100 - third_number * 10 - last_number) // 1000
print(first_number, second_number, third_number, last_number)
