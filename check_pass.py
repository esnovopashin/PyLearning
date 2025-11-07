pswrd = "juni0r"
user_pswrd = " "

print("=" * 50)
print("Введите пароль. Допускаются только прописные латинские буквы и цифры \nЕсли пароль не подобран, можно попробовать снова \nУдачи!")
print(f"Количество букв {len(pswrd)}")
print("=" * 50)

def user_input():
    user_pswrd = str(
        input("Введите пароль: ").lower()
        )
    if len(pswrd) < len(user_pswrd):
        user_pswrd = str(
            input(f"Ошибка! Количество букв больше {len(pswrd)} Введите пароль: ").lower()
        )
    elif len(pswrd) > len(user_pswrd):
        user_pswrd = str(
            input(f"Ошибка! Количество букв меньше {len(pswrd)}. Введите пароль: ").lower()
            )
    return user_pswrd

def check_pswrd():
    while True:
        try:
            user_pswrd = user_input()
            if pswrd == user_pswrd:
                print("Молодец, у тебя получилось!")
                break
            else:
                print("Сожалею, пароль не подошел... Попробуй снова!")     
    
        except ValueError:
            print("Что-то пошло не так")
   

if __name__ == "__main__":
    check_pswrd()