
odd_num = [num for num in range(1, 10, 2)]
numbers = [num for num in range(0,101)]


def verify_user_input():
    count = 0
    while True:
        try:
            user_input = int(
                input("Введите число : ").strip()
            )

            if user_input < 0:
                break
            count += 1
        
        except ValueError:
            print("Ошибка! Введите число")
    
    print("-" * 25)        
    print(f"Введено чисел: ", count)
    
    return count

print("=" * 25, "Задание 1 ", "=" * 25)
even_num = [num for num in numbers if num % 2 == 0]
print(f"четные числа: ", even_num)
print(f"Сумма четных чисел: ", sum(even_num))

print("=" * 25, "Задание 2 ", "=" * 25)
sq_odd_numbers = [num ** 2 for num in odd_num]
print(f"Квадраты нечетных чисел: ", sq_odd_numbers)

if __name__ == "__main__":
    print("=" * 25, "Задание 3 ", "=" * 25)
    print(f"Подсчитаем количество введенных чисел\nВвод принимается, пока не будет введено отрицательное число")
    counter_user_input = verify_user_input()