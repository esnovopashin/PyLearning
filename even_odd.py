even_num = []
odd_num = []
sq_odd_numbers = []
numbers = [num for num in range(0,101)]
#print(f"Длина массива: ", len(numbers))

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

for num in numbers:
    if num % 2 == 0:
        even_num.append(num)

print(f"четные числа: ", even_num)
print(f"Сумма четных чисел: ", sum(even_num))

print("=" * 25, "Задание 2 ", "=" * 25)

for num in numbers:
    if num % 2 != 0:
        odd_num.append(num)
print(f"Нечетные числа: ", odd_num)

sq_odd_numbers = [(lambda num: num*num)(num) for num in odd_num]
print(f"Квадраты нечетных чисел: ", sq_odd_numbers)

if __name__ == "__main__":
    print("=" * 25, "Задание 3 ", "=" * 25)
    counter_user_input = verify_user_input()