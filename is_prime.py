#задаем функцию
def primer(n):
    if n <= 1:
        print(f"{n} — не является простым числом")
    elif n == 2:
        print(f"{n} — простое число")
    elif n % 2 == 0:
        print(f"{n} — не является простым числом")
    else:
        is_prime = True
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                is_prime = False
                break
        
        if is_prime:
            print(f"{n} — простое число")
        else:
            print(f"{n} — не является простым числом")
#выводим 
n = int(input("Введите число для проверки на простоту: "))
primer(n)
