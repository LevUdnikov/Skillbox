class Student:

	def __init__(self, name, surname, group_number, estimation):
		self.name = name
		self.surname = surname
		self.group_number = group_number
		self.estimation = estimation

	def info(self):
		print("Имя и фамилия студента: {0} {1} Номер группы: {2} Оценки студента: {3}".format(self.name, self.surname,
																								self.group_number,
																								self.estimation))

	def get_average(self):
		estimate_count = 0
		score = 0
		for estimation in self.estimation:
			score += estimation
			estimate_count += 1

		return score / estimate_count


misha = Student("Миша", "Фомин", "РИ-100000", [3, 5, 4, 6, 7])
lena = Student("Лена", "Асхабова", "РИ-100010", [5, 5, 5, 5, 5])
lesha = Student("Леша", "Шомин", "РИ-200000", [2, 2, 3, 5, 5])
egor = Student("Егор", "Ромин", "РИ-300000", [5, 3, 4, 6, 7])
oleg = Student("Олег", "Громин", "РИ-400000", [4, 4, 4, 6, 7])
zhenya = Student("Женя", "Пронин", "РИ-500000", [3, 5, 4, 6, 7])
senya = Student("Сеня", "Шалдашов", "РИ-600000", [2, 2, 4, 6, 7])
stepa = Student("Степа", "Устинов", "РИ-700000", [2, 3, 4, 6, 7])
ilya = Student("Илья", "Абдрахманов", "РИ-800000", [2, 4, 4, 6, 7])
serega = Student("Сережа", "Гервойтинов", "РИ-900000", [2, 5, 4, 6, 7])

students = [misha, lena, lesha, egor, oleg, zhenya, serega, senya, stepa, ilya]
for i in range(len(students) - 1):
	for j in range(i + 1, len(students)):
		if students[i].get_average() < students[j].get_average():
			temp = students[i]
			students[i] = students[j]
			students[j] = temp

print("После сортировки: ")
for i in students:
	i.info()
	print(("Средний балл: {0}".format(i.get_average())))
