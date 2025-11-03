num = int(input("Введите число от 1 до 5: "))
def num_to_word(num):
    if num == 1:
        print("One")
    elif num == 2:
        print("Two")
    elif num == 3:
        print("Three")
    elif num == 4:
        print("Four")
    elif num ==5:
        print("Five")
    else:
        num = int(input("Введите число от 1 до 5: "))
        num_to_word(num)

num_to_word(num)