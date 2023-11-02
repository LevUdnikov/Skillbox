containers_count = int(input("Количество контейнеров: "))

containers = []
count = 0
find = False
while count < containers_count:
    container_weight = int(input("Введите вес контейнера: "))
    if 0 <= container_weight <= 200:
        containers.append(container_weight)
        count += 1

containers.sort(reverse=True)
new_container = int(input("Введите вес нового контейнера: "))

for number in range(len(containers)):
    if containers[number] < new_container:
        print(f"Номер, который получит новый контейнер: {number + 1}")
        find = True
        break

# Это исключение для случая, если новый контейнер массой как самый маленький контейнер
if not find:
    print(f"Номер, который получит новый контейнер: {containers_count + 1}")
