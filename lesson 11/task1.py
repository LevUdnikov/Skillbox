# При покупках за рубежом
# с помощью карты банки делают конвертацию через промежуточную валюту.

# Например,
# если купить что-то в евро,
# то сначала эта сумма конвертируется в доллары, а уже потом - в рубли.
#
# Напишите программу,
# которая получает на вход стоимость покупки в евро,
# затем выводит ответ в рублях.
#
# Мы живём в альтернативной реальности,
# где 1 евро = 1.25 доллара, а 1 доллар = 60.87 рублей.
coast = float(1)
rub = 0

while int(coast) != 0:
    coast = float(input('Введите стоимость товара (0 - выход): '))
    rub = round((coast * 1.25) * 60.87, 2)
    if coast > 0:
        print('Стоимость товара в рублях составила:', rub)
