string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")

if len(string1) != len(string2):
    print("Строки разной длины, невозможно получить первую строку из второй с помощью циклического сдвига.")
else:
    for i in range(len(string1)):
        if string1 == string2:
            print("Первая строка получается из второй со сдвигом", i)
            break
        string2 = string2[1:] + string2[0]
    else:
        print("Первую строку нельзя получить из второй с помощью циклического сдвига.")
