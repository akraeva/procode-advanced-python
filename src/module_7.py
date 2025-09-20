# Stepick.org — PROкод: продвинутый курс по Python
# 7. Работа со словарями (dict)

from sys import stdin
import ast


# pylint: disable=W0105

# 7.1 Словари: Основные особенности и их использование

# === Задача 1. Профиль администратора: запись в словарь ===
"""
    Создайте словарь с данными сотрудника и сохраните его в переменную admin:
        ключ 'name' → значение 'Александр' (строка);
        ключ 'surname' → значение 'Владимиров' (строка);
        ключ 'age' → значение 33 (целое число).
    Выведите переменную admin.
    """


def m_7_1_1():
    admin = {"name": "Александр", "surname": "Владимиров", "age": 33}
    return admin


# print(m_7_1_1())


# === Задача 2. Количество страниц в книге ===
"""
    Дан словарь с количеством страниц по номерам книг:
        book_pages = {
            1: 120,
            2: 245,
            3: 312,
            4: 400,
            5: 150,
            6: 215,
            7: 180,
            8: 320,
        }
    Считайте одно целое число --> номер книги и выведите
    количество страниц в этой книге (значение из словаря по ключу).
    """


def m_7_1_2(data: str, book_pages=None):
    if not book_pages:
        book_pages = {
            1: 120,
            2: 245,
            3: 312,
            4: 400,
            5: 150,
            6: 215,
            7: 180,
            8: 320,
        }
    number = int(data)
    return book_pages[number]


# print(m_7_1_2(input(), book_pages))


# === Задача 3. Квадраты чисел в словаре ===
"""
    Считай одно целое число n.
    Сформируй словарь, где ключи --> числа от 1 до n включительно,
    а значения — их квадраты.
    Выведи получившийся словарь.
    """


def m_7_1_3(data: str):
    number = int(data)
    squares = {num: num**2 for num in range(1, number + 1)}
    return squares


# print(m_7_1_3(input()))


# === Задача 4. Карта сокровищ ===
"""
    Считай:
        целое число --> количество членов экипажа;
        затем несколько строк формата Название острова:
            количество золота (по одной строке на остров), до конца ввода.
    Сделай словарь, где:
        ключ --> название острова,
        значение --> количество золота на острове (целое число).
    Для каждого острова вычисли долю на одного пирата: золото // экипаж.
    Выведи по строке для каждого острова в порядке ввода в формате:
        Название острова: <монет на одного>
    """

# from sys import stdin


def m_7_1_4(data: str):
    crew = int(data.split("\n")[0])
    coins_for_crew = {
        name.strip(): int(gold.strip()) // crew
        for island in data.strip().split("\n")[1:]
        for name, gold in [island.split(":")]
    }
    result = (f"{name}: {coins}" for name, coins in coins_for_crew.items())
    return "\n".join(result)


# print(m_7_1_4(stdin.read()))


# === Задача 5. Муравьиная Миссия ===
"""
    Считайте данные о 5 муравьях --> для каждого по две строки:
        имя муравья (строка);
        количество сахара (целое число, в граммах).
    После ввода всех пяти пар выведите по одной строке на каждого
    муравья в порядке ввода в точном формате:
        <Имя> - <число> гр. сахара!
    """

# from sys import stdin


def m_7_1_5(data: str):
    ants = {
        name.strip(): int(sugar.strip())
        for name, sugar in zip(data.strip().split()[::2], data.strip().split()[1::2])
    }
    result = [f"{name} - {sugar} гр. сахара!" for name, sugar in ants.items()]
    return "\n".join(result)


# print(m_7_1_5(stdin.read()))


# === Задача 6. Вход в храм ===
"""
    Считай одну строку --> список словарей с контактами муравьёв.
    Каждый словарь имеет структуру:
        'name': имя муравья (строка),
        'phone': номер телефона (строка, может содержать любые символы),
        'email': email (строка, может отсутствовать или быть пустой).
    Нужно:
        - отфильтровать муравьёв, чей номер заканчивается на цифру 1
          (при проверке игнорируй все нецифровые символы -->
          анализируй только цифры);
        - вывести их имена в алфавитном порядке, разделив одним пробелом
          (сортировка без учёта регистра, но выводить имена как есть).
        - Если подходящих имён нет --> выведи пустую строку.
    """

# from sys import stdin
# import ast


def m_7_1_6(data: str):
    ants = ast.literal_eval(data.strip())
    names = [ant["name"] for ant in ants if ant["phone"][-1] == "1"]
    result = sorted(names, key=lambda x: x.lower())
    return " ".join(result)


# print(m_7_1_6(stdin.read()))


# 7.2 Основы работы со словарями


# === Задача 1. Курс валют по запросу клиента ===
"""
    Дан словарь курсов:
        currency_exchange_rates = {
            "US Dollar (USD)": 90.123456,
            "Indian Rupee (INR)": 1.0845,
            "Australian Dollar (AUD)": 1582.512635,
            "Euro (EUR)": 98.765432,
        }
    Считайте одну строку --> название валюты
    (например, US Dollar (USD) или Indian Rupee (INR)).
    Выведите:
        - курс этой валюты (значение из словаря), если ключ найден;
        - строку Такой валюты нет, если ключ отсутствует.
    """

currency_exchange_rates = {
    "Argentine Peso (ARS)": 118372.215342,
    "Australian Dollar (AUD)": 1582.512635,
    "Bahraini Dinar (BHD)": 423.832745,
    "Botswana Pula (BWP)": 13179.672894,
    "Brazilian Real (BRL)": 5960.483625,
    "British Pound (GBP)": 835.245978,
    "Bruneian Dollar (BND)": 1522.126897,
    "Bulgarian Lev (BGN)": 1956.182346,
    "Canadian Dollar (CAD)": 1432.340798,
    "Chilean Peso (CLP)": 898553.372948,
    "Chinese Yuan Renminbi (CNY)": 7174.693871,
    "Colombian Peso (COP)": 4447999.273481,
    "Croatian Kuna (HRK)": 7530.652004,
    "Czech Koruna (CZK)": 24317.432120,
    "Danish Krone (DKK)": 7445.118312,
    "Emirati Dirham (AED)": 4140.527034,
    "Hong Kong Dollar (HKD)": 8789.672314,
    "Hungarian Forint (HUF)": 355967.319801,
    "Icelandic Krona (ISK)": 143605.740298,
    "Indian Rupee (INR)": 84248.241932,
    "Indonesian Rupiah (IDR)": 16187562.798213,
    "Iranian Rial (IRR)": 47534592.138725,
    "Israeli Shekel (ILS)": 3571.194506,
    "Japanese Yen (JPY)": 129152.736468,
    "Kazakhstani Tenge (KZT)": 489305.740973,
    "Kuwaiti Dinar (KWD)": 341.174296,
    "Libyan Dinar (LYD)": 5198.387920,
    "Malaysian Ringgit (MYR)": 4721.008324,
    "Mauritian Rupee (MUR)": 49219.721499,
    "Mexican Peso (MXN)": 23145.269032,
    "Nepalese Rupee (NPR)": 134858.540174,
    "New Zealand Dollar (NZD)": 1704.289657,
    "Norwegian Krone (NOK)": 9957.238134,
    "Omani Rial (OMR)": 433.477982,
    "Pakistani Rupee (PKR)": 198912.730142,
    "Philippine Peso (PHP)": 57586.209944,
    "Polish Zloty (PLN)": 4581.183949,
    "Qatari Riyal (QAR)": 4105.756309,
    "Romanian New Leu (RON)": 4949.538550,
    "Russian Ruble (RUB)": 86201.978414,
    "Saudi Arabian Riyal (SAR)": 4228.342118,
    "Singapore Dollar (SGD)": 1521.157853,
    "South African Rand (ZAR)": 17170.890324,
    "South Korean Won (KRW)": 1355527.193091,
    "Sri Lankan Rupee (LKR)": 228258.042514,
    "Swedish Krona (SEK)": 10441.135361,
    "Swiss Franc (CHF)": 1038.372528,
    "Taiwan New Dollar (TWD)": 31335.522134,
    "Thai Baht (THB)": 37439.467252,
    "Trinidadian Dollar (TTD)": 7638.784156,
    "Turkish Lira (TRY)": 15079.658926,
    "US Dollar (USD)": 1127.624590,
    "Venezuelan Bolivar (VES)": 511084173.217216,
}


def m_7_2_1(data: str, exchange=currency_exchange_rates):
    result = exchange.get(data, "Такой валюты нет")
    return result


# print(m_7_2_1(input()))


# === Задача 2. Тайный архив Ордена Охотников ===
"""
    Дан словарь:
        hunters_power = {
            "Джин": 85,
            "Дон": 90,
            "Сим": 88,
            "Андрей": 70,
            "Богги": 95,
            "Кастиель": 95,
            "Ребекка": 80,
            "Люцифер": 100,
            "Микаэль": 98,
            "Габриэль": 92
        }
    Считай одну строку --> имя охотника.
    Если имя есть среди ключей словаря --> выведи:
        Уровень силы <имя>: <число>
    Иначе выведи:
        Такой охотник не найден в архиве.
    """


def m_7_2_2(name: str, hunters_power=None):
    if not hunters_power:
        hunters_power = {
            "Джин": 85,
            "Дон": 90,
            "Сим": 88,
            "Андрей": 70,
            "Богги": 95,
            "Кастиель": 95,
            "Ребекка": 80,
            "Люцифер": 100,
            "Микаэль": 98,
            "Габриэль": 92,
        }
    if name in hunters_power:
        return f"Уровень силы {name}: {hunters_power[name]}"
    return "Такой охотник не найден в архиве."


# print(m_7_2_2(input(), hunters_power))


# === Задача 3.  Хранитель ключей Древнего Города ===
"""
    Дан ввод одной строкой в виде списка пар
    код: "название", разделённых запятыми.
    Нужно:
        разобрать строку и составить словарь magic_keys,
        где ключи -> целые числа,
        а значения --> строки (названия ключей);
    вывести:
        Сумма всех ключей: <sum>
        Минимальный ключ: <min>
        Максимальный ключ: <max>
    Для вычислений используй sum(), min(), max() по ключам словаря.
    """


def m_7_2_3(keys: str):
    magic_keys = {
        int(num.strip()): value.strip("\"' ")
        for key in keys.split(",")
        for num, value in [key.strip().split(":")]
    }
    return (
        f"Сумма всех ключей: {sum(magic_keys)}\n"
        f"Минимальный ключ: {min(magic_keys)}\n"
        f"Максимальный ключ: {max(magic_keys)}"
    )


# print(m_7_2_3(input()))


# === Задача 4. Книга заклинаний Верховного Мага ===
"""
    Считай две строки --> по одной на каждую версию книги.
    Каждая строка имеет вид:
        Название: число, Другое название: число, ...
    Например: Огненный шар: 50, Ледяная стрела: 40, Щит молнии: 70
    Сделай следующее:
        Преобразуй каждую строку в словарь:
            ключ --> название заклинания (строка),
            значение --> уровень силы (целое число).
            Пробелы вокруг названий и чисел нужно убрать.
    Сравни полученные словари.
    Выведи:
        - Книги идентичны --> если словари равны;
        - Книги отличаются --> если различаются.
    """

# from sys import stdin


def m_7_2_4(data: str):
    def parser(line: str):
        books = {
            name.strip(): int(num.strip())
            for book in line.split(",")
            for name, num in [book.split(":")]
        }
        return books

    dict1, dict2 = (parser(line) for line in data.strip().split("\n"))
    return "Книги идентичны" if dict1 == dict2 else "Книги отличаются"


# print(m_7_2_4(stdin.read()))
