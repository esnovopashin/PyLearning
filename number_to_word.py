def num_to_word(num):
    if num == 1:
        print("One")
    elif num == 2:
        print("Two")
    elif num == 3:
        print("Three")
    elif num == 4:
        print("Four")
    elif num == 5:
        print("Five")
    else:
        print("Число должно быть от 1 до 5")
        num = number_input()
        num_to_word(num)

def number_input():
    while True:
        try:
            num = int(input("Введите число от 1 до 5: ").strip())
            if 1 <= num <= 5:
                return num
            else:
                print("Ошибка! Введите число в диапазоне от 1 до 5")
        except ValueError:
            print("Ошибка! Введите только цифры")

num = number_input()
num_to_word(num)