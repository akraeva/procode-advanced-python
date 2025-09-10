# Stepick.org — PROкод: продвинутый курс по Python
# 4. Работа с функциями. Начало

from string import punctuation


# pylint: disable=W0105

# 4.1 Что такое функции. Их объявление и вызов

# === Задача 1-1. Привет от функции ===
"""
    Напиши только определение функции say_hello(),
    которая при вызове выводит ровно эту строку:
    Привет! Я функция. Я здесь, чтобы работать за тебя. Плати печеньками!
    Вызов функции писать не нужно.
    """


def m_4_1_1():
    def say_hello():
        print("Привет! Я функция. Я здесь, чтобы работать за тебя. Плати печеньками!")


# === Задача 1-2. breaking_bad: I AM THE ONE WHO KNOCKS ===
"""
    Напиши только определение функции breaking_bad(),
    которая при вызове выводит ровно:
    I AM THE ONE WHO KNOCKS
    Вызов функции писать не нужно.
    """


def m_4_1_2():
    def breaking_bad():
        print("I AM THE ONE WHO KNOCKS")


# === Задача 2-1. Поиск магического числа ===
"""
    Считайте одну строку с целыми числами, разделёнными пробелами.
    Преобразуйте её в список чисел и найдите первое число,
    которое делится на 7 без остатка.
    Выведите: это число --> если оно найдено;
    None --> если в последовательности нет подходящих чисел.
    """


def m_4_1_3(data: str):
    nums = map(int, data.split())
    for num in nums:
        if num % 7 == 0:
            return num
    return None


# print(m_4_1_3(input()))


# === Задача 2-2. Послание из космоса: Тайна магического слова ===
"""
    Реализуйте функцию find_magic_word(message), которая принимает одну
    строку с посланием и:
        - разбивает её на слова;
        - для каждого слова удаляет знаки препинания только с начала и конца
          (набор знаков берите из модуля String;
        - определяет, является ли длина очищенного слова простым числом;
        - как только встретится первое слово с простой длиной -->
          выводит это слово с помощью print;
        - если подходящих слов нет --> выводит None.

    Требования:
        - функция работает только с переданной строкой (без input() внутри);
        - вызывать функцию не нужно, нужно только её определить.
    """


def m_4_1_4(data: str):
    # from string import punctuation
    def find_magic_word(message: str):
        words = [word.strip(punctuation) for word in message.split()]
        max_len = len(max(words, key=len))
        primes = tuple(
            num
            for num in range(2, max_len + 1)
            if 1 < num < 4 or not any(num % n == 0 for n in range(2, int(num**0.5) + 1))
        )
        for word in words:
            if len(word) in primes:
                print(word)
                return word
        print(None)
        return None

    return find_magic_word(data)
