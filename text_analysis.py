def cyrillic_input(): # проверка на кириллицу
    while True:
        text = input("Введите текст на русском языке : ")
        # где введен не тот символ
        for char in text.lower():
            if char not in ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя.,?!:;()\\/|-_=+#@$%^&*<>{[]}1234567890':
                print(f"не тот символ: '{char}' (код: {ord(char)})")
        # конец проверки
        if all(char in ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя.,?!:;()\\/|-_=+#@$%^&*<>{[]}1234567890' for char in text.lower()):
            return text
        else:
            print("Ошибка! Используйте только кириллицу")


def clean_text(text): # очистка исходного текста от символов
    clear_text = text
    symbols = [".", ",", ":", ";", "(", ")", "'", "\"", "-", "_", "+", "?", "!"]

    for char in symbols:
        clear_text = clear_text.replace(char, "")
    
    return clear_text


def find_longest_words(split_text): # ищем длинные слова
    max_length = 0
    longest_words = []
    
    for word in split_text:
        word_length = len(word)
        
        if word_length > max_length:
            max_length = word_length
            longest_words = [word]
        elif word_length == max_length:
            longest_words.append(word)
            
    return longest_words


def count_vowel(text):  # Считаем гласные
    vowel_letters = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    result = {}
    
    for vowel in vowel_letters:
        result[vowel] = 0
    
    for char in text.lower():
        if char in vowel_letters:
            result[char] += 1

    return result

def count_words_from(split_text):  # Считаем слова
    count_words = {}
    
    for word in split_text:
        if word in count_words:
            count_words[word] += 1
        else:
            count_words[word] = 1
    return count_words

def out_count_words(split_text): # вывод счетчика слов
    word_stat = count_words_from(split_text)
    print("\nИспользовано слов:")
    
    for word, count in word_stat.items():
        print(f"'{word}': {count}")


def out_longest_word(longest_words): # вывод длинного слова
    if longest_words:
        word = longest_words[0]
        print(f"Самое длинное слово: '{word}', его длина = {len(word)}")
    else:
        print("Слов не найдено")


def out_vowel_analyses(text): # вывод гласных
    vowel_stats = count_vowel(text)
    print("\nИспользовано гласных:")
    
    for vowel, count in vowel_stats.items():
        if count > 0:
            print(f"'{vowel}': {count}")


if __name__ == "__main__":
    text = cyrillic_input()
    cleaning_text = clean_text(text)
    split_text = cleaning_text.split()
    print("====== Анализ текста ======")
    print(f"Слов: {len(split_text)}")
    longest_words = find_longest_words(split_text)
    out_longest_word(longest_words)
    out_count_words(split_text)
    print("=" * 50)
    out_vowel_analyses(text)