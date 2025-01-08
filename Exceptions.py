try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))

    result: float = num1 / num2

except ValueError:(
    print("Ошибка: введено не число!"))

except ZeroDivisionError:(
    print("Ошибка: Деление на ноль!"))

finally:
    print(f"Результат: {result}")
    print("Программа завершена")
    exit()