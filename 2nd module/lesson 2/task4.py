films = ["Крепкий орешек", "Назад в будущее", "Таксист", "Леон", "Богемская рапсодия", "Город грехов", "Мементо",
         "Отступники", "Деревня"]
favorite_films = []

films_count = int(input("Сколько фильмов хотите добавить? "))

for film_number in range(films_count):
    film_add = input("Введите название фильма: ")
    if film_add in films:
        favorite_films.append(film_add)
    else:
        print(f"Ошибка: фильма {film_add} у нас нет :(")

print("Ваш список любимых фильмов: ", end="")
print(", ".join((str(item) for item in favorite_films)))
