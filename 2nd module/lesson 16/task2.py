def callback(route):
	def decorator(func):
		route_handlers[route] = func
		return func

	return decorator


route_handlers = {}


@callback('//')
def example():
	print('Пример функции, которая возвращает ответ сервера')
	return 'OK'


# Основной код
requested_route = '//'
route_handler = route_handlers.get(requested_route)
if route_handler:
	response = route_handler()
	print('Ответ:', response)
else:
	print('Такого пути нет')
requested_route = '/invalid_route'

#
route_handler = route_handlers.get(requested_route)
if route_handler:
	response = route_handler()
	print('Ответ:', response)
else:
	print('Такого пути нет')
