def get_obj_info(obj):
    obj_length = len(obj)
    obj_type = type(obj)

    print(f"Объект: {obj}")
    print(f"Длина: {obj_length}")
    print(f"Тип: {obj_type}")

obj = "Hallo, world!"
get_obj_info(obj)

print()

obj = [1, 2, 3, 4, 5]
get_obj_info(obj)