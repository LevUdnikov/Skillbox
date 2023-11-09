def print_to_num(n):
	if n > 0:
		print_to_num(n-1)
		print(n)


num = int(input("Введите num: "))
print_to_num(num)
