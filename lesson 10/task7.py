# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
#
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

levels = int(input("Введите количество уровней пирамиды: "))
num = 1
for i in range(1, levels+1):
    spaces = " "*(levels-i)
    print(f"{spaces}", end="")
    for j in range(i):
        print(f"{num:2d} ", end="")
        num += 2
    print()
