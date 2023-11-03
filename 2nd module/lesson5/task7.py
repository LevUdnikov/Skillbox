ip = input("Введите IP: ")
ip_numbers = ip.split(".")
if len(ip_numbers) != 4:
    print("Адрес — это четыре числа, разделённые точками.")
else:
    ip = [x for x in ip_numbers if x.isdigit()]
    if len(ip) != 4:
        for i in ip_numbers:
            if i.isalnum() and (not(i.isdigit())):
                print("{} - это не целое число.".format(i))
    else:
        ip_numbers = []
        for numbers in ip:
            if int(numbers) > 255:
                print("{} превышает 255.".format(numbers))

            else:
                ip_numbers.append(numbers)
        if len(ip_numbers) == 4:
            print("IP-адрес корректен.")
