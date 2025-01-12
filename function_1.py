def say_hello():
    print("Hello, Python!")

def repeat_message(message):
    print(*[message] * 3, sep='\n')

say_hello()

print()

repeat_message("Hi!")