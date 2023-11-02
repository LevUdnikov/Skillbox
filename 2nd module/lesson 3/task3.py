shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]
price = 0
count = 0

detail_name = input("Название детали: ")
detail_count = int(input("Количество деталей: "))

for names in shop:
    if names[0] == detail_name and count < detail_count:
        count += 1
        price += names[1]
print(f"Общая стоимость: {price}")
