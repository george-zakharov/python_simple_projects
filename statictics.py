import re
import string
import numpy

# Готовим словарь для заполнения
letters = list(string.ascii_lowercase)
letters = dict.fromkeys(letters)

# Читаем файл, пишем в переменную
with open('files/long_text.txt', 'r') as file:
    raw_text = file.read().lower()

# Считаем количество вхождений букв алфавита в тексте
for letter, value in letters.items():
    letters[letter] = raw_text.count(letter)

# Разбиваем исходный текст на предложения
raw_text_lines = re.split(r"\.(?:[\[\d\]]+)?\s+", raw_text)

words_in_lines_count = []  # Количество слов в предложении
letters_in_words_count = []  # Количество букв в словах
all_words_count = 0  # Количество слов в тексте

for line in raw_text_lines:
    words = re.split(r"\s+", line)
    words_in_line = len(words)
    words_in_lines_count.append(words_in_line)
    all_words_count += words_in_line

    for word in words:
        letters_in_words_count.append(len(word))

# Считаем частоту букв в тексте
for letter, value in letters.items():
    letters[letter] = value / all_words_count

results = {}
# Считаем среднюю длину предолжения
results['Средняя длина предложения'] = numpy.mean(words_in_lines_count)
results['Средняя длина слова'] = numpy.mean(letters_in_words_count)
results['Частота букв'] = letters

# Пишем результаты в файл
with open('files/results.txt', 'w') as file:
    for title, value in results.items():
        if type(value) is dict:
            file.write(str(title + ':' + '\n'))
            for letter, letter_value in value.items():
                file.write(str(letter + ' - ' + str(letter_value) + '\n'))
        else:
            file.write(str(title + ': ' + str(value) + '\n'))
