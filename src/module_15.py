# Stepick.org — PROкод: продвинутый курс по Python
# 15. Практические задания

import re
from sys import stdin
from math import ceil
from collections import Counter


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


# 15.2 PyHero -- игра на выживание


# === Задача 1. Пробуждение в Системе ===
"""
    Пользователь вводит строку команд, разделённых пробелами.
    Требуется:
        - Преобразовать строку в список команд.
        - Вывести сам список.
        - Вывести количество всех команд.
        - Вывести количество уникальных команд.
        - Вывести команду, которая встречается чаще всего.
          Если таких несколько, вывести первую.
    """


def m_15_2_1(data: str):
    commands = data.split()
    frequency = {}
    for command in commands:
        if command not in frequency:
            frequency[command] = commands.count(command)
    result = [
        str(commands),
        f"Всего команд: {len(commands)}",
        f"Уникальных команд: {len(set(commands))}",
        f"Чаще всего используется: {max(frequency, key=lambda c: frequency[c])}",
    ]
    return "\n".join(result)


# print(m_15_2_1(input()))

# === Задача 2. Первое оружие ===
"""
    Пользователь вводит строку, в которой перечислены предметы инвентаря через
    запятую (например: "Лазерный нож,Нанощит,Граната").
    Требуется:
        - Преобразовать строку в список предметов.
        - Вывести весь список.
        - Вывести количество предметов.
        - Найти и вывести предмет с самой короткой длиной.
          Если таких несколько, вывести первый.
        - Найти и вывести предмет с самой длинной длиной.
          Если таких несколько, вывести первый.
    """


def m_15_2_2(data: str):
    items = list(map(str.strip, data.split(",")))
    result = [
        str(items),
        f"Всего предметов: {len(items)}",
        f"Самый короткий предмет: {min(items, key=len)}",
        f"Самый длинный предмет: {max(items, key=len)}",
    ]
    return "\n".join(result)


# print(m_15_2_2(input()))


# === Задача 3. Система координат ===
"""
    Пользователь сначала вводит количество зон (строк).
    Затем для каждой зоны вводится строка из трёх целых чисел,
        разделённых пробелами (координаты).
    Нужно:
        - Сформировать вложенный список coordinates.
        - Вывести всю карту.
        - Вывести координату из второй зоны, первая позиция.
          Если такой нет, вывести: Недостаточно зон для доступа к [1][0]
        - Найти зону с наибольшей суммой координат, и вывести эту зону.
        - Найти максимальную точку на всей карте и вывести её.
    """

# from sys import stdin


def m_15_2_3(data: str):
    coordinates = [
        list(map(int, line.split())) for line in data.strip().split("\n")[1:]
    ]
    try:
        start = coordinates[1][0]
    except IndexError:
        start = None
    max_zone = max(coordinates, key=sum)
    max_point = max(map(max, coordinates))
    result = [
        str(coordinates),
        (
            f"Координата [1][0]: {start}"
            if start is not None
            else "Недостаточно зон для доступа к [1][0]"
        ),
        f"Зона с максимальной суммой: {max_zone}",
        f"Максимальная координата: {max_point}",
    ]
    return "\n".join(result)


# print(m_15_2_3(stdin.read()))


# === Задача 4. Столкновение с отрядом врагов ===
"""
    Пользователь вводит количество врагов.
    Затем для каждого врага он вводит три строки:
        Имя врага (строка)
        Урон врага (целое число)
        Броня врага (целое число)
    Тебе нужно:
        - Создать список словарей с информацией о каждом враге.
        - Найти врага с максимальной угрозой (угроза = урон + броня).
        - Вычислить, хватит ли тебе урона (60), чтобы пробить броню этого
            врага. Урон по врагу не может быть меньше 0, если броня
            превышает урон, итоговый урон = 0.
        - Вывести информацию:
            - Имя самого сильного врага.
            - Уровень угрозы этого врага.
            - Итоговый урон после вычета его брони.
            - Сообщение, победишь ты или нет.
    """

# from sys import stdin


def m_15_2_4(data: str, my_power=60):
    input_data = data.strip().split("\n")
    enemies = []
    for i in range(1, len(input_data), 3):
        name, damage, armor = input_data[i : i + 3]
        enemies.append({"name": name, "damage": int(damage), "armor": int(armor)})
    enemy = max(enemies, key=lambda e: e["damage"] + e["armor"])

    threat_level = enemy["damage"] + enemy["armor"]
    result_damage = my_power - enemy["armor"]

    result = [
        f"Самый опасный враг: {enemy['name']}",
        f"Уровень угрозы: {threat_level}",
        f"Итоговый урон по врагу: {result_damage if result_damage > 0 else 0}",
        f"Исход боя: {'Победа' if result_damage > 0 else 'Поражение'}",
    ]
    return "\n".join(result)


# print(m_15_2_4(stdin.read()))


# === Задача 5. Зелье восстановления ===
"""
    Пользователь вводит названия зелий в виде строки через запятую.
    Нужно:
        - Сформировать список зелий.
        - Определить и вывести отсортированный список уникальных зелий.
        - Вывести общее количество зелий.
        - Вывести количество уникальных зелий.
        - Вычислить и вывести самое часто встречающееся зелье
          и количество его повторов.
        - Если несколько зелий одинаково распространены, вывести то,
        что стоит первым в отсортированном списке.
    """


# from sys import stdin
# from collections import Counter


def m_15_2_5(data: str):
    potions = list(map(str.strip, data.split(",")))
    unique = set(potions)
    potion, count = Counter(sorted(potions)).most_common(1)[0]
    result = [
        f"Уникальные зелья: {sorted(unique)}",
        f"Всего зелий: {len(potions)}",
        f"Количество уникальных зелий: {len(unique)}",
        f"Самое частое зелье: {potion} ({count} раз(а))",
    ]
    return "\n".join(result)


# print(m_15_2_5(stdin.read()))


# === Задача 6. Квестовые сообщения ===
"""
    Пользователь вводит сообщение (строку). Нужно:
        - Привести текст к нижнему регистру и разбить на слова.
        - Найти и вывести три самых частых слова с числом повторов.
        - Если слов меньше трёх, вывести столько, сколько есть.
        - Слова сортировать по убыванию частоты, при равенстве -- по алфавиту.
    """

# from collections import Counter


def m_15_2_6(data: str):
    words = data.lower().strip().split()
    counter = Counter(words)
    result = sorted(counter.items(), key=lambda w: (-w[1], w[0]))[:3]
    return "\n".join(f"{word} {count}" for word, count in result)


# print(m_15_2_6(input()))


# === Задача 7. Готовность к прокачке героя ===
"""
    Напиши функцию analyze_exp(exp_list), которая принимает список целых чисел
    (очки опыта за каждый бой) и возвращает словарь со следующими ключами:
        'max': максимальный опыт за бой.
        'min': минимальный опыт за бой.
        'sum': суммарный опыт.
        'avg': средний опыт (округлить до целого).
        'battles': общее число проведённых боёв.
        'level_up': возможность перейти на новый уровень
            (True, если суммарный опыт больше 500, иначе False).
    """


def analyze_exp(exp_list):
    exp_sum = sum(exp_list)
    count = len(exp_list)
    result = {
        "max": max(exp_list),
        "min": min(exp_list),
        "sum": exp_sum,
        "avg": round(exp_sum / count),
        "battles": count,
        "level_up": exp_sum > 500,
    }
    return result


m_15_2_7 = analyze_exp


# === Задача 8. Карта порталов ===
"""
    Напиши функцию analyze_portals(portal_list), которая принимает на вход
        список целых чисел -- энергии каждого портала.
    Функция должна вернуть кортеж из двух элементов:
        - Отсортированный по возрастанию список порталов.
        - Множество порталов, энергия которых выше среднего
          значения всех порталов.
    Вызывать функцию не нужно!
    """


def analyze_portals(portal_list):
    average = sum(portal_list) / len(portal_list)
    above_average = set(portal for portal in portal_list if portal > average)
    return (sorted(portal_list), above_average)


m_15_2_8 = analyze_portals


# === Задача 9. Алтарь навыков ===
"""
    Напиши функцию analyze_skills(skills_dict),
        которая принимает словарь (навык: уровень).
    Функция возвращает словарь с ключами:
        'sorted_skills': список кортежей (навык, уровень),
            отсортированный по убыванию уровня (при равных — по алфавиту).
        'above_average': отсортированный по алфавиту список названий навыков,
            уровень которых выше среднего.
        'average_level': средний уровень навыков (округлённый до целого).
    """


def analyze_skills(skills_dict: dict):
    skills = sorted(skills_dict.items(), key=lambda s: (-s[1], s[0]))
    average_level = round(sum(skills_dict.values()) / len(skills_dict))
    above_average = sorted(
        skill for skill, level in skills_dict.items() if level > average_level
    )
    result = {
        "sorted_skills": skills,
        "above_average": above_average,
        "average_level": average_level,
    }
    return result


m_15_2_9 = analyze_skills


# === Задача 10. Финальный бой с Боссом ===
"""
    Напиши функцию fight_boss(attacks, boss_defense), которая принимает:
        attacks -- список словарей, каждый из которых описывает атаку:
            {"name": str, "power": int, "type": str}
        boss_defense — словарь, содержащий параметры босса:
            "armor": int — защита (снижает урон),
            "weakness": str — тип атаки, на который Босс уязвим (твой бонус),
            "shield": int — щит (дополнительно уменьшает урон).
    Функция должна:
        - Выбрать атаку, которая наносит наибольший урон с учётом бонусов:
            - Если attack["type"] == boss["weakness"],
              к attack["power"] прибавляется +50% (округляется вверх).
        - Отнять урон Босса armor + shield и вернуть:
            - Название лучшей атаки.
            - Урон после всех защит (не меньше нуля).
            - Сообщение "Победа!", если урон > 100, иначе — "Босс выжил...".
    """

# from math import ceil


def fight_boss(attacks: list, boss: dict):
    for attack in attacks:
        if attack["type"] == boss["weakness"]:
            attack["power"] = ceil(attack["power"] * 1.5)
    max_attack = max(attacks, key=lambda a: a["power"])
    damage = max_attack["power"] - (boss["armor"] + boss["shield"])
    resuil = (
        max_attack["name"],
        damage if damage > 0 else 0,
        "Победа!" if damage > 100 else "Босс выжил...",
    )
    return resuil


m_15_2_10 = fight_boss
