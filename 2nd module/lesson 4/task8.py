cyrillic = [chr(i) for i in range(ord('а'), ord('я') + 1)]
encrypted_text = ""

users_text = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))

for letter in users_text:
    if letter in cyrillic:
        new_letter = cyrillic[(cyrillic.index(letter) + shift) % len(cyrillic)]
        encrypted_text += new_letter
    else:
        encrypted_text += letter

print("Зашифрованное сообщение:", encrypted_text)

