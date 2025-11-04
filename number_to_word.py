def num_to_word(num):
    if num == 1:
        word = "One"
        return word
    elif num == 2:
        word = "Two"
        return word
    elif num == 3:
        word = "Three"
        return word
    elif num == 4:
        word = "Four"
        return word
    elif num == 5:
        word = "Five"
        return word
    else:
        print("Число должно быть от 1 до 5")


def number_input():
    while True:
        try:
            num = int(input("Введите число от 1 до 5: ").strip())
            if num in range(1, 6):
                return num
            else:
                print("Ошибка! Введите число в диапазоне от 1 до 5")
        except ValueError:
            print("Ошибка! Введите только целые числа")


def translate():
    num = number_input()
    print("Соответствующее слово: ", num_to_word(num))


if __name__ == "__main__":
    translate()
