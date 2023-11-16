import re

input_string = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

# Номера частных автомобилей
private_cars = re.findall(r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b', input_string)
print("Список номеров частных автомобилей:", private_cars)

# Номера такси
taxis = re.findall(r'\b[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}\b', input_string)
print("Список номеров такси:", taxis)