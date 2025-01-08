#Сложение
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    result: float = num1 + num2

except ValueError:(
    print("Ошибка: введено не число!"))

# except ZeroDivisionError:(
#     print("Ошибка: Деление на ноль!"))

finally:
    print(f"Результат: {result}")

#Вычитание
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    result: float = num1 - num2

except ValueError:(
    print("Ошибка: введено не число!"))

# except ZeroDivisionError:(
#     print("Ошибка: Деление на ноль!"))

finally:
    print(f"Результат: {result}")

#Умножение
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    result: float = num1 * num2

except ValueError:(
    print("Ошибка: введено не число!"))

# except ZeroDivisionError:(
#     print("Ошибка: Деление на ноль!"))

finally:
    print(f"Результат: {result}")

#Деление
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    result: float = num1 / num2

except ValueError:(
    print("Ошибка: введено не число!"))

 # except ZeroDivisionError:(
 #     print("Ошибка: Деление на ноль!"))

finally: print(f"Результат: {result}")