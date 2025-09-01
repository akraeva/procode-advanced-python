# Stepick.org — PROкод: продвинутый курс по Python
# 2. Освежаем базовые знания

from sys import stdin

# 2.1 Объявление переменных, ввод (input()) и вывод (print())


def m_2_1_1(data):
    start1, end1, start2, end2 = map(int, data.split("\n"))
    if end1 <= start2:
        return "Нет"
    else:
        return f"Да\n{start2//60:02}:{start2 % 60:02} - {end2//60:02}:{end2 % 60:02}"


# data = stdin.read()
# print(m_2_1_1(data))


def m_2_1_2(apples, bananas):
    str_1 = f"Общее количество фруктов: {apples+bananas}"
    str_2 = f"Каждому другу достанется по {(apples+bananas)//2} фруктов."
    return "\n".join((str_1, str_2))


# print(m_2_1_2(int(input()), int(input())))


def m_2_1_3(name, age, number):
    return f"Секретный код: {(age+number)*len(name)}"


# print(m_2_1_3(input(), int(input()), int(input())))


def m_2_1_4(name, number):
    number_sum = sum(int(x) for x in number)
    name_sum = sum(len(word) for word in name.split())
    return f"Код замка: {number_sum}-{name_sum}"


# print(m_2_1_4(input(), input()))


def m_2_1_5(*args):
    """
    Считайте четыре значения (каждое с новой строки):
    - текущий год --> целое число;
    - количество лет для подготовки --> целое число;
    - число технологического развития --> целое число;
    - название проекта --> строка.

    Вычислите «индекс инноваций» по формуле:
    индекс = (сумма цифр числа из пункта 3) + (количество символов в названии без пробелов)
    Вычислите год прорыва:
    год_прорыва = текущий_год + (количество_лет * индекс)

    Выведите результат в формате: Год прорыва: <число>
    """
    current_year = int(args[0])
    number_of_years = int(args[1])
    tech_number = int(args[2])
    project_name = args[3]
    innovation_index = sum(int(digit) for digit in str(tech_number)) + len(
        project_name.replace(" ", "")
    )
    breakthrough = current_year + number_of_years * innovation_index
    return f"Год прорыва: {breakthrough}"


# data = stdin.read().split("\n")
# print(m_2_1_5(*data))
