#print("Bears love honey and I'm a Pooh bear")
# 1. Создайте переменные различных типов данных
x = 5
fl = 5.5
my_text = "text"
my_lst = [1,2,3]
my_tpl = (1,2,3)
my_dict = {"name": "Alice", "age": 25}
my_set = {1,2,3}
# 2. Выведите тип данных каждой переменной с помощью функции type() и напечатайте результат
# print(type(x))
# print(type(fl))
# print(type(my_text))
# print(type(my_lst))
# print(type(my_tpl))
# print(type(my_dict))
# print(type(my_set))
num_str = "456"
num = int(num_str)
print(num)

fl_int = int(fl)
num_str = str(fl_int)
print(num_str)

new_tpl = tuple(my_lst)
print(new_tpl)

num_list = [x]
print(num_list)