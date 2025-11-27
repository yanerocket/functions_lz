#задаем функцию
def proveryaem(a):
    if a % 2 == 0:
         print('четное:' , a)
    else:
        print('нечетное:', a)

b = (input('введите число: ').split('.')) #вводим число

proveryaem(int(b[0])) #вызываем функцию 