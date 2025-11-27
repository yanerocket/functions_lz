#задаем функцию
def perevod(time):
    hours, minutes, secundos = time_input.split(":")
    hours = int(hours)
    minutes = int(minutes)
    secundos = int(secundos)
    return secundos + minutes * 60 + hours * 3600
#вводим время
time_input = input("Введите время в формате ЧЧ:ММ:СС: ")
#выводим функцию
print("Время в секундах:", perevod(time_input))