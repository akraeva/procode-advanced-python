# Stepick.org — PROкод: продвинутый курс по Python
# 10. Практические задания

from sys import stdin


# pylint: disable=W0105


# 10.1 Легенда о потерянных артефактах аниме-миров


# === Задача 1. Камни чакры  ===
"""
    - Принять список чакр (разделённые пробелами).
    - Преобразовать в множество (чтобы убрать повторы).
    - Отсортировать множество и представить его в виде строки с {}.
    - Вывести отформатированный результат.
    Ограничение: не используйте list, dict, range
    """


def m_10_1_1(data: str):
    chakras = sorted(set(data.split()))
    return f"{{{', '.join(chakras)}}}"


# print(m_10_1_1(input()))


# === Задача 2. Знаки с Грешниками  ===
"""
    - Принять список имён грешников (разделённые пробелами).
    - Создать множество из этих имён.
    - Принять имя, которое нужно удалить.
    - Принять имя, которое нужно добавить.
    - Вывести обновлённый список грешников в отсортированном виде в формате {}.
    """

# from sys import stdin


def m_10_1_2(data: str):
    lines = data.strip().split("\n")
    sinners = set(lines[0].split())
    to_remove, to_add = lines[1:]
    sinners.remove(to_remove)
    sinners.add(to_add)
    return f"{{{', '.join(sorted(sinners))}}}"


# print(m_10_1_2(stdin.read()))


# === Задача 3. Кланы Хантера  ===
"""
    Получить два множества:
        - охотники (разделены пробелами).
        - преступники (разделены пробелами).
            - Найти общих людей (пересечение множеств).
            - Найти уникальных охотников (разность множеств).
            - Вывести оба результата в предсказуемом порядке.
    Ограничение: не используйте list, dict, range...
    """

# from sys import stdin


def m_10_1_3(data: str):
    hunters, criminals = (set(line.split()) for line in data.strip().split("\n"))
    common = hunters & criminals
    purebred = hunters - criminals
    return (
        f"Общие: {{{', '.join(sorted(common))}}}\n"
        f"Чистые охотники: {{{', '.join(sorted(purebred))}}}"
    )


# print(m_10_1_3(stdin.read()))


# === Задача 4. Легендарные техники  ===
"""
    - Получить два множества:
        - те, кто владеет техникой "Ультра-инстинкт"
        - те, кто достиг "Истинного Ультра-инстинкта"
    - Проверить, является ли второе множество подмножеством первого.
    - Вывести результат в формате:
    Все мастера входят в первое множество: True/False
    Ограничение: не используйте list, dict, range
    """

# from sys import stdin


def m_10_1_4(data: str):
    possess, achieved = (set(line.split()) for line in data.strip().split("\n"))
    return f"Все мастера входят в первое множество: {achieved.issubset(possess)}"


# print(m_10_1_4(stdin.read()))


# === Задача 5. Священный артефакт аниме-вселенной ===
"""
    - Получить список легендарных аниме.
    - Преобразовать его в замороженное множество (frozenset).
    - Вывести отсортированный список этих аниме. Для вывода списка
      использовать переменную anime_frozen_set
    Важно: переменная anime_frozen_set должна оставаться
        замороженным множеством
    Ограничение: не используйте dict, range
    """


def m_10_1_5(data: str):
    anime = frozenset(name.strip() for name in data.split(","))
    return sorted(anime)


# print(m_10_1_5(input()))
