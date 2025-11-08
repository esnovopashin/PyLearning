def pswrd_input():
    pswrd = input("Введите начальный пароль: ").lower().strip()
        
    return pswrd


def user_input(pswrd):
    user_pswrd = input("Введите пароль: ").lower().strip()
    
    while len(user_pswrd) != len(pswrd):
        if len(user_pswrd) < len(pswrd):
            user_pswrd = input(f"Ошибка! Количество букв меньше {len(pswrd)}. Введите пароль: ").lower()
        elif len(user_pswrd) > len(pswrd):
            user_pswrd = input(f"Ошибка! Количество букв больше {len(pswrd)}. Введите пароль: ").lower()
        
    return user_pswrd


def check_pswrd():
    while True:
        try:
            user_pswrd = user_input(pswrd)
            if pswrd == user_pswrd:
                print("Молодец, у тебя получилось!")
                break
            else:
                print("Сожалею, пароль не подошел... Попробуй снова!")     
    
        except ValueError:
            print("Что-то пошло не так")

pswrd = pswrd_input()
print("=" * 50)
print("Введите пароль. Допускаются только прописные латинские буквы и цифры \nЕсли пароль не подобран, можно попробовать снова \nУдачи!")
print(f"Количество букв {len(pswrd)}")
print("=" * 50)

if __name__ == "__main__":
    check_pswrd()