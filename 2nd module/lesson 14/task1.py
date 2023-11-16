def how_are_you(func):
	def wrapper():
		answer = input('Как дела? ')
		print('А у меня не очень!')
		func()

	return wrapper


@how_are_you
def test():
	print('Функция 0')


@how_are_you
def test1():
	print('Функция 1')


@how_are_you
def test2():
	print('Функция 2')


test()
test1()
test2()

