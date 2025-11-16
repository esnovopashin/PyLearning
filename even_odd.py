numbers = list(range(101))
#print(numbers)
even_num = []
odd_num = []

for x in numbers:
    if x % 2 == 0:
        even_num.append(x)
print(f"четные числа: {even_num}")

for y in numbers:
    if y % 2 != 0:
        odd_num.append(y)
print(f"нечетные числа: {odd_num}")