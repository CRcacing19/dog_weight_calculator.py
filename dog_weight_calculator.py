# Название файла: dog_weight_calculator.py

breed = input("Введите породу собаки: ")
weight = int(input("Введите вес собаки в кг: "))

if breed == "Шпиц":
    average_weight = 5
elif breed == "Лабрадор":
    average_weight = 30
elif breed == "Джек Рассел терьер":
    average_weight = 7
elif breed == "Немецкая овчарка":
    average_weight = 35
elif breed == "Чихуахуа":
    average_weight = 2
else:
    print("Извините, не знаю средний вес для этой породы.")
    exit()

if weight < average_weight:
    print("Собака слишком маленькая для своей породы.")
elif weight > average_weight:
    print("Собака слишком тяжелая для своей породы.")
else:
    print("Вес собаки в норме.")
