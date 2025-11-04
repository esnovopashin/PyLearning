# Алексей Рыбицкий:
# 1) должна быть функция которая сообщает может человек голосовать или нет
# 2) создай более четкую структуру, например функции в которых будет проверка корректно введенного
# - возраста, age
# - гражданства, citizenship
# - дисквалификации, disqualification
# - функция запуска can_vote
def verify_age():
    while True:
        try:
            age = int(
                input("Введите ваш возраст (полное количество лет): ").strip()
            )

            if age > 0:
                return age
            print("Возраст не может быть отрицательным")

        except ValueError:
            print("Ошибка! Введите целое число")


def verify_citizenship():
    while True:
        try:
            citizenship = int(
                input("У вас есть гражданство? Введите 1 - да, 0 - нет: ").strip()
            )

            if citizenship in (0, 1):
                return citizenship
            print("Введите 1 (да) или 0 (нет)")

        except ValueError:
            print("Введите только цифру 1 или 0")


def verify_disqualification():

    questions_lst = [
        "У вас есть гражданство другой страны или вид на жительство в другой стране? Введите 1 - да, 0 - нет: ",
        "Вы признаны судом недееспособным? Введите 1 - да, 0 - нет: ",
        "Вы находитесь в местах лишения свободы по приговору суда или имеете непогашенную судимость? Введите 1 - да, 0 - нет: "
    ]

    for n in questions_lst:
        while True:
            try:
                answer = int(
                    input(n + "Введите 1 - да, 0 - нет: ").strip()
                )

                if answer in (0, 1):
                    if answer == 1:
                        return True
                    break

                print("Введите 1 (да) или 0 (нет)")

            except ValueError:
                print("Введите только цифру 1 или 0")
    return False


def can_vote():
    age = verify_age()

    if age < 18:
        print("Не может голосовать")
        return

    if verify_citizenship() == 0:
        print("Не может голосовать")
        return

    if verify_disqualification():
        print("Не может голосовать")
        return

    print("Может голосовать")


if __name__ == "__main__":
    can_vote()
