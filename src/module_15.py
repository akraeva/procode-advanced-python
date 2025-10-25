# Stepick.org — PROкод: продвинутый курс по Python
# 15. Практические задания

import re
from sys import stdin


# pylint: disable=W0105


# 15.1 Lil Byte -- путь к вершине!


# === Задача 1. Первый риф Lil Byte-а ===
"""
    Твой код должен:
        - Прочитать строку от пользователя.
        - Посчитать количество гласных букв
          (a, e, i, o, u, а, е, ё, и, о, у, ы, э, ю, я).
        - Вывести это количество.
    """

# import re


def m_15_1_1(data: str):
    chrs = r"[aeiouаеёиоуыэюя]"
    result = len(re.findall(chrs, data.lower()))
    return result


# print(m_15_1_1(input()))


# === Задача 2. Рэп-список тем ===
"""
    Твой код должен:
        - Прочитать строку с темами, разделёнными запятыми.
        - Разбить строку в список.
        - Отсортировать список по алфавиту.
        - Вывести темы построчно.
    """


def m_15_1_2(data: str):
    result = sorted(map(str.strip, data.split(",")))
    return "\n".join(result)


# print(m_15_1_2(input()))


# === Задача 3. Текстовая магия ===
"""
    Твой код должен:
        - Прочитать строку текста.
        - Разбить текст на слова.
        - Посчитать, сколько раз каждое слово встречается.
        - Вывести словарь.
    """


def m_15_1_3(data: str):
    words = data.split()
    result = dict.fromkeys(words, 0)
    for word in result:
        result[word] = words.count(word)
    return result


# print(m_15_1_3(input()))

# === Задача 4. Турне по городам ===
"""
    Твой код должен:
        - Прочитать строку городов через запятую.
        - Преобразовать её в кортеж.
        - Вывести:
            - Весь кортеж городов.
            - Последний город в кортеже.
    """


def m_15_1_4(data: str):
    result = tuple(map(str.strip, data.split(",")))
    return f"{str(result)}\nПоследний город тура: {result[-1]}"


# print(m_15_1_4(input()))


# === Задача 5. Рэп-баттл с FlowMax ===
"""
    Твой код должен:
        - Прочитать два текста -- от Lil Byte и FlowMax.
        - Разбить тексты на слова.
        - Преобразовать в множества.
        - Найти их пересечение.
        - Вывести отсортированный список общих слов.
    """

# from sys import stdin


def m_15_1_5(data: str):
    lil_byte, flowmax = (set(line.split()) for line in data.strip().split("\n"))
    result = sorted(lil_byte & flowmax)
    return result


# print(m_15_1_5(stdin.read()))


# === Задача 6. Любимые треки фанатов ===
"""
    Твой код должен:
        - Получить число фанатов.
        - Затем построчно ввести имя и любимый трек.
        - Сохранить пары в словарь.
        - Вывести словарь.
    """

# from sys import stdin


def m_15_1_6(data: str):
    result = {
        key: value
        for line in data.strip().split("\n")[1:]
        for key, value in [line.split(" ", 1)]
    }
    return result


# print(m_15_1_6(stdin.read()))

# === Задача 7. Самая жирная строчка ===
"""
    Твой код должен:
        - Объявить функцию find_max_line().
        - Внутри пройтись по строкам и найти ту, где больше всего слов.
          Если таких несколько, вернуть первую.
        - Вернуть эту строку.
        - Функцию вызывать не нужно.
    """


def find_max_line(data: list):
    lines = [(line, len(line.split())) for line in data]
    result = max(lines, key=lambda line: line[-1])
    return result[0]


m_15_1_7 = find_max_line


# === Задача 8. Уникальный стиль ===
"""
    Твой код должен:
        - Объявить функцию analyze_text(text).
        - Разбить строку на слова.
        - Посчитать количество уникальных слов через множество.
        - Вернуть:
            - количество уникальных слов
            - отсортированное множество в виде отсортированного списка.
        - Функцию вызывать не нужно.
    """


def analyze_text(text: str):
    words = set(text.split())
    return (len(words), sorted(words))


m_15_1_8 = analyze_text


# === Задача 9. Рэп-чарт TOP3 ===
"""
    Твой код должен:
        - Прочитать количество рэперов.
        - Ввести имя и баллы каждого.
        - Сохранить пары в виде кортежей.
        - Отсортировать список по убыванию баллов.
        - Вывести топ-3.
    """


# from sys import stdin


def m_15_1_9(data: str):
    top = [
        (name, int(score))
        for line in data.strip().split("\n")[1:]
        for name, score in [line.rsplit(" ", 1)]
    ]
    result = sorted(top, key=lambda line: line[-1], reverse=True)
    return result[:3]


# print(m_15_1_9(stdin.read()))

# === Задача 10. Финальный баттл мирового уровня ===
"""
    Объявить функцию analyze_battle(text).
        - Разбить строку на слова.
        - Посчитать общее количество слов.
        - Посчитать количество уникальных слов.
        - Найти самое частое слово. Если их несколько вывести первое!
        - Вернуть кортеж: (всего_слов, уникальных_слов, самое_частое_слово).
        - Функцию вызывать не нужно.
    """


def analyze_battle(text: str):
    words = text.split()
    unique = set(words)
    frequency = {}
    for word in words:
        if word not in frequency:
            frequency[word] = words.count(word)
    most_popular = max(frequency, key=lambda word: frequency[word])
    return (len(words), len(unique), most_popular)


m_15_1_10 = analyze_battle
