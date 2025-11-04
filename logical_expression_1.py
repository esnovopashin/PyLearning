# вариант с проверкой каждого ответа
def verify_input(question):
    while True:
        try:
            value = int(input(question))
            if value == 0 or value == 1:
                return value
            else:
                print("Введите 1 (да) или 0 (нет)")
        except ValueError:
            print("Ошибка! Введите 1 или 0")

def can_vote():
    
    # Проверка ввода возраста
    while True:
        try:
            age = int(input("Введите ваш возраст (полное количество лет): ").strip())
            if age >= 0:
                break
            else:
                print("Возраст не может быть меньше 18")
        except ValueError:
            print("Ошибка! Введите целое число для возраста")
    
    # Проверка на возраст меньше 18
    if age < 18:
        print("Не может голосовать")
        return
    
    # Проверка на гражданство
    is_citizenship = verify_input(("У вас есть гражданство? Введите 1 - да, 0 - нет: ").strip())
    
    if is_citizenship == 0:
        print("Не может голосовать")
        return
    
    # Проверка на гражданство другой страны
    is_disqualified1 = verify_input(("У вас есть гражданство другой страны или вид на жительство в другой стране? Введите 1 - да, 0 - нет: ").strip())

    if is_disqualified1 == 1:
        print("Не может голосовать")
        return
    
    # Проверка на недееспособность
    is_disqualified2 = verify_input(("Вы признаны судом недееспособным? Введите 1 - да, 0 - нет: ").strip())

    if is_disqualified2 == 1:
        print("Не может голосовать")
        return

    # Проверка на судимость
    is_disqualified3 = verify_input(("Вы находитесь в местах лишения свободы по приговору суда или имеете непогашенную судимость? Введите 1 - да, 0 - нет: ").strip())

    if is_disqualified3 == 1:
        print("Не может голосовать")
        return

    # все ОК, пашем
    print("Может голосовать")

can_vote()
