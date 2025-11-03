#1
def max_number(a, b):
    return a if a > b else b #добавил тернарник вместо if/else


#2
def empty_function():
    pass


#3
def even_numbers(n):
    for i in range(0, n+1, 2):
        yield i


#4 автотест для функции max_number(a, b)
def test_max_number():

    assert max_number(1, 3) == 3, "Error: 3 > 1"
    assert max_number(-3, -1) == -1, "Error: -1 > -3"
    assert max_number(10, 5) == 10, "Error: 10 > 5"
    
    print("Passed")


test_max_number()

# вывод в цикле
for num in even_numbers(10):
    print(num)