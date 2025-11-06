def verify_num():
    while True:
        try:
            start_num = int(
                input("Введите целое положительное число, с которого стартует счетчик. ").strip()
            )

            if start_num > 0:
                return start_num
            elif start_num == 0:
                print("Ошибка!")
            else:
                print("Число не может быть отрицательным")
                
        except ValueError:
            print("Ошибка!")

def countdown(start_num):
    while start_num >= 0:
        print("Счетчик= ", start_num)
        start_num -= 1
        
if __name__ == "__main__":
    start_number = verify_num()
    countdown(start_number)