def get_interest_and_surname_length(student_list):
	interest = set()
	surname_len = 0
	for student_characteristic in student_list.values():
		for key, value in student_characteristic.items():
			if key == "surname":
				surname_len += len(value)
			elif key == 'interests':
				interest.update(set(value))
	return interest, surname_len


students = {
	1: {
		'name': 'Bob',
		'surname': 'Vazovski',
		'age': 23,
		'interests': ['biology, swimming']
	},
	2: {
		'name': 'Rob',
		'surname': 'Stepanov',
		'age': 24,
		'interests': ['math', 'computer games', 'running']
	},
	3: {
		'name': 'Alexander',
		'surname': 'Krug',
		'age': 22,
		'interests': ['languages', 'health food']
	}
}

for student_id in students.keys():
	print(student_id, students[student_id]["name"])

interests, length = get_interest_and_surname_length(students)

print("Длина всех фамилий: {0}\nСписок интересов студентов: {1}".format(length, ", ".join(interests)))
