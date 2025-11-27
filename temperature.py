#пишем функцию
def perevod(a):
    return (a*9/5)+32
b = float(input('Ввод темппературы:'))
resultat = perevod(b) #вызываем функцию
print('Температура в градусах по Фаренгейту:', resultat) #вывод результата