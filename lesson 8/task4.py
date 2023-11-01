# Напишите программу, которая считывает с клавиатуры три числа a, b и c, считает и выводит на консоль среднее
# арифметическое всех чисел из отрезка [a; b], кратных числу c.

a, b, c = map(int, input("Введите три числа через пробел: ").split(' '))
count = 0
sum_number = 0
for number in range(a, b + 1):
    if number % c == 0:
        sum_number += number
        count += 1
print(f"Среднее арифметическое чисел: {sum_number / count}")
