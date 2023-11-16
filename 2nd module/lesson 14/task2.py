import time
import functools


def delay_execution(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		time.sleep(3)  # Ждем 3 секунды
		return func(*args, **kwargs)

	return wrapper


@delay_execution
def some_function():
	print('Выполнение функции с задержкой...')


some_function()
