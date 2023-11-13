import random


class Unit:
	hp = 100
	name = "Воин"
	
	def info(self):
		print("Оставшееся здоровье: {}".format(self.hp))

	def take_damage(self):
		self.hp -= 20
		self.info()


unit1 = Unit()
unit2 = Unit()
while unit1.hp != 0 and unit2.hp != 0:
	who_take_damage = random.randint(1, 2)
	if who_take_damage == 1:
		print("Атаковал unit1:")
		unit2.take_damage()
	else:
		print("Атаковал unit2:")
		unit1.take_damage()
if unit1.hp > unit2.hp:
	print("Победу одержал unit1")
else:
	print("Победу одержал unit2")