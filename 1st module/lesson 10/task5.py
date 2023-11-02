# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.
N = int(input("Введите кол-во чисел: "))
max_number = 0
max_summ = 0
for counter in range(N):
    sum = 0
    digit = 0
    number = int(input("Введите число: "))
    temp = number

    while temp > 0:
        digit = temp % 10
        sum += digit
        temp //= 10

    if sum > max_summ:
        max_summ = sum
        max_number = number
print(f"Наибольше по сумме цифр число это {max_number} с суммой {max_summ}")
