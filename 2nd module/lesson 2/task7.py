string = input("Введите слово: ")
reversed_string = ""

for char in string:
    reversed_string = char + reversed_string

if string == reversed_string:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")