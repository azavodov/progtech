"""
Прочитать из файла (имя - параметр командной строки) все слова (разделитель пробел)

Создать "Похожий" словарь который отображает каждое слово из файла
на список всех слов, которые следуют за ним (все варианты).

Список слов может быть в любом порядке и включать повторения.
например "and" ['best", "then", "after", "then", ...] 

Считаем, что пустая строка предшествует всем словам в файле.

С помощью "Похожего" словаря сгенерировать новый текст похожий на оригинал.
Т.е. напечатать слово - посмотреть какое может быть следующим и выбрать случайное.

В качестве теста можно использовать вывод программы как вход.парам. для следующей копии
(для первой вход.парам. - файл)

Файл:
He is not what he should be
He is not what he need to be
But at least he is not what he used to be
(c) Team Coach
"""

import random
import sys


def generate_same_text(same_dict: dict, words_count: int) -> str:
    generated_words = list()
    for i in range(words_count):
        prev_word = generated_words[i - 1] \
            if len(generated_words) else random.choice(list(same_dict.keys()))
        word = random.choice(same_dict[prev_word]) \
            if len(same_dict[prev_word]) else random.choice(list(same_dict.keys()))
        generated_words.append(word)
    return " ".join(generated_words)


def parse_same_dict(file: str) -> dict:
    same_dict = dict()
    with open(file, "r") as f:
        for line in f.read().split("\n"):
            words = line.split(" ")
            for i, word in enumerate(words):
                if word not in same_dict:
                    same_dict[word] = list()
                if i + 1 < len(words):
                    same_dict[word].append(words[i + 1])
    return same_dict


if __name__ == '__main__':
    filename = sys.argv[1]
    word_count = sys.argv[2] if len(sys.argv) > 1 else 35
    same_dict = parse_same_dict(filename)
    print(generate_same_text(same_dict, int(word_count)))
