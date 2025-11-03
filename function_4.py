#1
def max_number(a, b):
    if a > b:
        return a
    elif b >= a:
        return b

    
#2
def empty_function():
    pass


#3
def even_numbers(n):
    for i in range(0, n+1, 2):
        print(i)
        yield i
        

#4 автотест для функции max_number(a, b)
def test_max_number():

    assert max_number(1, 3) == 3, "Error: 3 > 1"
    assert max_number(-3, -1) == -1, "Error: -1 > -3"
    assert max_number(10, 5) == 10, "Error: 10 > 5"
    
    print("Passed")
    
test_max_number()