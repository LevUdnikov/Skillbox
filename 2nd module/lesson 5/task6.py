string = input("Введите строку: ")
encoded_string = []
count = 1
for i in range(len(string)):
    if i == len(string)-1:
        encoded_string.append(string[i] + str(count))
    elif string[i] == string[i+1]:
        count += 1
    else:
        encoded_string.append(string[i] + str(count))
        count = 1

encoded_string = ''.join(encoded_string)
print("Закодированная строка:", encoded_string)