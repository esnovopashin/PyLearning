str_1 = ' строка с пробелами в начале и в конце '

print(str_1.strip(), '\n')

str_2 = 'замените одно слово на другое'
new_str = str_2.replace("другое", "иное")

print(new_str, '\n')

str_3 = "Python is great"
words = str_3.split()

print(words, '\n')

letters = ['Объединил', 'слова', 'в', 'одну', 'строку']
word = " ".join(letters)

print("Получаем слово:", word)