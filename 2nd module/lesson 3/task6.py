count = 0

n = int(input("Количество роликов: "))
roller_sizes = []
for i in range(n):
    size = int(input("Размер пары {}: ".format(i+1)))
    roller_sizes.append(size)

k = int(input("Количество людей: "))
foot_sizes = []
for i in range(k):
    size = int(input("Размер ноги человека {}: ".format(i+1)))
    foot_sizes.append(size)

for i in foot_sizes:
    if i in roller_sizes:
        count += 1
        roller_sizes.remove(i)

print("Наибольшее количество людей, которые могут взять ролики:", count)
