print("Сложение")
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result: float = num1 + num2

except ValueError:(
    print("Ошибка: введено не число!"))

finally:
    print(f"Результат: {result}", end="\n\n")

print("Вычитание")
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result: float = num1 - num2

except ValueError:(
    print("Ошибка: введено не число!"))

finally:
    print(f"Результат: {result}", end="\n\n")

    print("Умножение")
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result: float = num1 * num2

except ValueError:(
    print("Ошибка: введено не число!"))

finally:
    print(f"Результат: {result}", end="\n\n")

    print("Деление")
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result: float = num1 / num2

except ValueError:(
    print("Ошибка: введено не число!"))

except ZeroDivisionError:(
    print("Ошибка: Деление на ноль!"))

finally: print(f"Результат: {result}")