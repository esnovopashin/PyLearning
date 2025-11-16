#1. Напишите программу, которая вычисляет сумму всех четных чисел от 1 до 100.
#2. Создайте список, содержащий квадраты всех нечетных чисел от 1 до 10, используя **генератор списка**.
#3. Напишите программу, которая просит пользователя ввести число и продолжает запрашивать числа, пока пользователь не введет отрицательное число. Затем программа должна вывести количество введенных чисел

numbers = []
even_num = []
odd_num = []
sq_odd_numbers = []
num = 0
numbers = [num for num in range(0,101)]
print(f"Длина массива: ", len(numbers))

#1
for num in numbers:
    if num % 2 == 0:
        even_num.append(num)
print(f"четные числа: ", even_num)

#sum_even_num = sum(even_num)
print(f"Сумма четных чисел: ", sum(even_num))

#2
for num in numbers:
    if num % 2 != 0:
        odd_num.append(num)
print(f"Нечетные числа: {odd_num}")

sq_odd_numbers = [(lambda num: num*num)(num) for num in odd_num]
print(sq_odd_numbers)


#3
