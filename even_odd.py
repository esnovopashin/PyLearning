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


# Задача 1
print("=" * 25, "Задание 1 ", "=" * 25)
numbers = [num for num in range(0,101)]
summ_even_num = 0

for num in numbers:
    if num % 2 == 0:
        summ_even_num += num

print(f"Сумма четных чисел: ", summ_even_num)

# Задача 2
print("=" * 25, "Задание 2 ", "=" * 25)

odd_num = [num for num in range(1, 11, 2)]
print(f"Квадраты нечетных чисел: ", [num ** 2 for num in odd_num])

if __name__ == "__main__":
    print("=" * 25, "Задание 3 ", "=" * 25)
    print(f"Подсчитаем количество введенных чисел\nВвод принимается, пока не будет введено отрицательное число")
    counter_user_input = verify_user_input()