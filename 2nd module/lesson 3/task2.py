def merge_sorted_lists(list1, list2):
    list1.extend(list2)
    for element in list1:
        while list1.count(element) > 1:
            list1.remove(element)

    list1.sort()
    return list1


list1 = [1, 3, 5, 7, 9]
# list1 = [1,3] # Это на случай, когда один список короче другого
# list1 = [] # Это на случай, когда один список пустой
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(f"Вывод: {merged}")
