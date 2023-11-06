words = input("Введите строку: ").replace(".", "").split()
max_len = 0
for word in words:
    if len(word) > max_len:
        max_len = len(word)
        longest_word = word
print('Самое длинное слово: "{}"'.format(longest_word))
print("Длина этого слова: {}.".format(max_len))

