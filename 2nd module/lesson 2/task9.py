N = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

for index in range(len(N)-1, -1, -1):
    if N[index] % 2 == 0:
        print(N[index], end=" ")
