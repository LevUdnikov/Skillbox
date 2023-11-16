import requests
from bs4 import BeautifulSoup


def get_subheadings(url):
	# Отправляем GET-запрос к указанному URL и получаем HTML-код страницы
	response = requests.get(url)

	# Используем BeautifulSoup для парсинга HTML
	soup = BeautifulSoup(response.content, 'html.parser')

	# Находим все подзаголовки, заключенные в теги <h3>
	subheadings = [heading.text.strip() for heading in soup.find_all('h3')]

	return subheadings


# URL веб-страницы, с которой мы хотим извлечь подзаголовки
url = 'http://www.columbia.edu/~fdc/sample.html'

# Получаем список подзаголовков
subheadings = get_subheadings(url)

# Выводим результат
print(subheadings)