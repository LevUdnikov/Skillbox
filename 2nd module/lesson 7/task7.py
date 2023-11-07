def myzip(a, b):
	return ((a[i], b[i]) for i in range(min(len(a), len(b))))


e = "abcd"
b = (10, 20, 30, 40)
g = myzip(e, b)

print(g)
print(*g, sep='\n')
