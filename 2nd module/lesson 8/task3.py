import copy


def replace_product_name(template, product_name):
	if isinstance(template, str):
		return template.replace('телефон', product_name).replace('iPhone', product_name)
	elif isinstance(template, dict):
		new_template = {}
		for key, value in template.items():
			new_template[key] = replace_product_name(value, product_name)
		return new_template
	else:
		return template


# Исходный сайт
site = {
	'html': {
		'head': {
			'title': 'Куплю/продам телефон недорого'
		},
		'body': {
			'h2': 'У нас самая низкая цена на iPhone',
			'div': 'Купить',
			'p': 'Продать'
		}
	}
}

# Запрашиваем у пользователя количество сайтов
num_sites = int(input("Сколько сайтов: "))

# Список для хранения сайтов
sites_list = [copy.deepcopy(site) for _ in range(num_sites)]

# Запрашиваем названия продуктов для каждого сайта, заменяем и выводим все активные сайты
for i in range(num_sites):
	product_name = input("Введите название продукта для нового сайта: ")
	for j in range(i + 1):
		print(f"Сайт для {product_name}: ")
		print(replace_product_name(sites_list[j], product_name))
