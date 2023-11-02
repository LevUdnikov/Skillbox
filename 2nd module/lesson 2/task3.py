graphic_card_count = int(input("Количество видеокарт: "))

graphics_card = []
max_card = 0

for graphic_card_number in range(1, graphic_card_count + 1):
    graphic_card = int(input(f"Видеокарта {graphic_card_number}: "))
    graphics_card.append(graphic_card)
    if graphic_card > max_card:
        max_card = graphic_card

for card_id in range(len(graphics_card)-1):
    if graphics_card[card_id] == max_card:
        graphics_card.remove(max_card)

print(f"Новый список видеокарт: {graphics_card}")
