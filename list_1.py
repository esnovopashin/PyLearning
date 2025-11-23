#Напишите программу, которая создает список из 5 строк и меняет первый и последний элементы в нём
def create_list():
    
    while len(my_list) < 5:
        item = input("Введите строку: ").strip()
        my_list.append(item)

def change_list(my_list):
    item5 = my_list.pop(4)
    item0 = my_list.pop(0)
    my_list.insert(0,item5)
    my_list.insert(4,item0)

        
if __name__ == "__main__":
    my_list = []
    create_list()
    print(f"Исходный список: ", my_list)
    change_list(my_list)
    print(f"Измененный список: ", my_list)