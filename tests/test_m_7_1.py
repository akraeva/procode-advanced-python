import pytest
from src.module_7 import (
    m_7_1_1,
    m_7_1_2,
    m_7_1_3,
    m_7_1_4,
    m_7_1_5,
    m_7_1_6,
)


# === Тест для задачи 7.1.1 ===


@pytest.mark.parametrize(
    "expected",
    [
        {"name": "Александр", "surname": "Владимиров", "age": 33},
    ],
)
def test_7_1_1(expected):
    assert m_7_1_1() == expected


# === Тест для задачи 7.1.2 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        ("1", 120),
        ("2", 245),
        ("3", 312),
        ("4", 400),
        ("5", 150),
        ("6", 215),
        ("7", 180),
        ("8", 320),
    ],
)
def test_7_1_2(data, expected):
    assert m_7_1_2(data) == expected


# === Тест для задачи 7.1.3 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        ("5", {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}),
        # fmt: off
        ("23", {
            1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100,
            11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256,
            17: 289, 18: 324, 19: 361, 20: 400, 21: 441, 22: 484, 23: 529
        }),
        # fmt: on
        ("0", {}),
        ("1", {1: 1}),
        ("10", {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}),
    ],
)
def test_7_1_3(data, expected):
    assert m_7_1_3(data) == expected


# === Тест для задачи 7.1.4 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            "5\nТортуга: 50\nПорт-Рояль: 80\nПальмовые острова: 120",
            "Тортуга: 10\nПорт-Рояль: 16\nПальмовые острова: 24",
        ),
        (
            "2\nОстров Легенд: 40\nМорской Риф: 60\nОстров Счастья: 80",
            "Остров Легенд: 20\nМорской Риф: 30\nОстров Счастья: 40",
        ),
        (
            "3\nТортуга: 60\nПорт-Рояль: 90\nПальмовые острова: 180",
            "Тортуга: 20\nПорт-Рояль: 30\nПальмовые острова: 60",
        ),
        (
            "4\nКарибы: 200\nЧёрная бухта: 100\nОстров Мистики: 300",
            "Карибы: 50\nЧёрная бухта: 25\nОстров Мистики: 75",
        ),
        (
            "10\nОстров Смерти: 50\nОстров Черепа: 120\nГавань Туманов: 200",
            "Остров Смерти: 5\nОстров Черепа: 12\nГавань Туманов: 20",
        ),
    ],
)
def test_7_1_4(data, expected):
    assert m_7_1_4(data) == expected


# === Тест для задачи 7.1.5 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            "Антон\n5\nМаргарита\n7\nСергей\n3\nДжон\n8\nАлиса\n4",
            "Антон - 5 гр. сахара!\n"
            "Маргарита - 7 гр. сахара!\n"
            "Сергей - 3 гр. сахара!\n"
            "Джон - 8 гр. сахара!\n"
            "Алиса - 4 гр. сахара!",
        ),
        (
            "По\n3\nГоша\n6\nМоника\n13\nТолик\n1\nТося\n3",
            "По - 3 гр. сахара!\n"
            "Гоша - 6 гр. сахара!\n"
            "Моника - 13 гр. сахара!\n"
            "Толик - 1 гр. сахара!\n"
            "Тося - 3 гр. сахара!",
        ),
        (
            "Алексей\n6\nНаташа\n10\nМиша\n2\nАлена\n7\nДжеймс\n4",
            "Алексей - 6 гр. сахара!\n"
            "Наташа - 10 гр. сахара!\n"
            "Миша - 2 гр. сахара!\n"
            "Алена - 7 гр. сахара!\n"
            "Джеймс - 4 гр. сахара!",
        ),
    ],
)
def test_7_1_5(data, expected):
    assert m_7_1_5(data) == expected


# === Тест для задачи 7.1.6 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            """[{"name": "Eva", "phone": "112-342-6718", "email": "eva.smith@mail.com"},
        {"name": "Milo", "phone": "555-982-6741", "email": "milo.james@outlook.com"},
        {"name": "Sophia", "phone": "478-245-8912", "email": ""}]""",
            "Milo",
        ),
        (
            """[{'name': 'Eva', 'phone': '112-342-6718', 'email': 'eva.smith@mail.com'},
        {'name': 'Milo', 'phone': '555-982-6743', 'email': 'milo.james@outlook.com'},
        {'name': 'Sophia', 'phone': '478-245-8911', 'email': ''},
        {'name': 'Theo', 'phone': '555-673-8345', 'email': 'theo.green@protonmail.com'},
        {'name': 'Viktor', 'phone': '417-145-2032', 'email': 'viktor.kaplan@mail.ru'},
        {'name': 'Liam', 'phone': '321-452-7393', 'email': ''},
        {'name': 'Chloe', 'phone': '+7996-789-1234', 'email': 'chloe.miller@icloud.com'},
        {'name': 'Zoe', 'phone': '+7916-542-3124', 'email': 'zoe.williams@gmail.com'},
        {'name': 'David', 'phone': '411-568-9973', 'email': ''},
        {'name': 'Omar', 'phone': '178-903-4768', 'email': 'omar.zahid@outlook.com'},
        {'name': 'Igor', 'phone': '+7956-234-9876', 'email': 'igor.ivanov@mail.com'},
        {'name': 'Kira', 'phone': '7356-478-9281', 'email': ''},
        {'name': 'Leo', 'phone': '+7423-167-2093', 'email': 'leo.pratt@mail.ru'},
        {'name': 'Anna', 'phone': '15-674-3912', 'email': 'anna.morrison@tutanota.com'},
        {'name': 'Max', 'phone': '+7534-287-0654', 'email': ''},
        {'name': 'Charlie', 'phone': '253-346-7024', 'email': 'charlie.jones@gmail.com'}]""",
            "Kira Sophia",
        ),
        (
            """[{'name': 'Eva', 'phone': '112-342-6718', 'email': 'eva.smith@mail.com'},
        {'name': 'Milo', 'phone': '555-982-6745', 'email': 'milo.james@outlook.com'},
        {'name': 'Sophia', 'phone': '478-245-8912', 'email': ''},
        {'name': 'Theo', 'phone': '555-673-8345', 'email': 'theo.green@protonmail.com'},
        {'name': 'Viktor', 'phone': '417-145-2036', 'email': 'viktor.kaplan@mail.ru'},
        {'name': 'Liam', 'phone': '321-452-7396', 'email': ''},
        {'name': 'Chloe', 'phone': '+7996-789-1234', 'email': 'chloe.miller@icloud.com'},
        {'name': 'Zoe', 'phone': '+7916-542-3124', 'email': 'zoe.williams@gmail.com'},
        {'name': 'David', 'phone': '411-568-9970', 'email': ''},
        {'name': 'Omar', 'phone': '178-903-4768', 'email': 'omar.zahid@outlook.com'},
        {'name': 'Igor', 'phone': '+7956-234-9876', 'email': 'igor.ivanov@mail.com'},
        {'name': 'Kira', 'phone': '7356-478-9280', 'email': ''},
        {'name': 'Leo', 'phone': '+7423-167-2090', 'email': 'leo.pratt@mail.ru'},
        {'name': 'Anna', 'phone': '15-674-3911', 'email': 'anna.morrison@tutanota.com'},
        {'name': 'Max', 'phone': '+7534-287-0654', 'email': ''},
        {'name': 'Charlie', 'phone': '253-346-7021', 'email': 'charlie.jones@gmail.com'}]""",
            "Anna Charlie",
        ),
        (
            """[{'name': 'Eva', 'phone': '112-342-6718', 'email': 'eva.smith@mail.com'},
        {'name': 'Milo', 'phone': '555-982-6745', 'email': 'milo.james@outlook.com'},
        {'name': 'Sophia', 'phone': '478-245-8912', 'email': ''},
        {'name': 'Theo', 'phone': '555-673-8345', 'email': 'theo.green@protonmail.com'},
        {'name': 'Viktor', 'phone': '417-145-2036', 'email': 'viktor.kaplan@mail.ru'},
        {'name': 'Liam', 'phone': '321-452-7396', 'email': ''},
        {'name': 'Chloe', 'phone': '+7996-789-1234', 'email': 'chloe.miller@icloud.com'},
        {'name': 'Zoe', 'phone': '+7916-542-3124', 'email': 'zoe.williams@gmail.com'},
        {'name': 'David', 'phone': '411-568-9970', 'email': ''},
        {'name': 'Omar', 'phone': '178-903-4768', 'email': 'omar.zahid@outlook.com'},
        {'name': 'Igor', 'phone': '+7956-234-9876', 'email': 'igor.ivanov@mail.com'},
        {'name': 'Kira', 'phone': '7356-478-9280', 'email': ''},
        {'name': 'Leo', 'phone': '+7423-167-2090', 'email': 'leo.pratt@mail.ru'},
        {'name': 'Anna', 'phone': '15-674-3911', 'email': 'anna.morrison@tutanota.com'},
        {'name': 'Max', 'phone': '+7534-287-0654', 'email': ''},
        {'name': 'Charlie', 'phone': '253-346-7029', 'email': 'charlie.jones@gmail.com'}]""",
            "Anna",
        ),
        (
            """[{'name': 'Eva', 'phone': '112-342-6711', 'email': 'eva.smith@mail.com'}, 
        {'name': 'Milo', 'phone': '555-982-6741', 'email': 'milo.james@outlook.com'}, 
        {'name': 'Sophia', 'phone': '478-245-8912', 'email': ''}, 
        {'name': 'Theo', 'phone': '555-673-8345', 'email': 'theo.green@protonmail.com'}, 
        {'name': 'Viktor', 'phone': '417-145-2031', 'email': 'viktor.kaplan@mail.ru'}, 
        {'name': 'Liam', 'phone': '321-452-7391', 'email': ''}, 
        {'name': 'Chloe', 'phone': '+7996-789-1234', 'email': 'chloe.miller@icloud.com'}, 
        {'name': 'Zoe', 'phone': '+7916-542-3124', 'email': 'zoe.williams@gmail.com'}, 
        {'name': 'David', 'phone': '411-568-9971', 'email': ''}, 
        {'name': 'Omar', 'phone': '178-903-4768', 'email': 'omar.zahid@outlook.com'}, 
        {'name': 'Igor', 'phone': '+7956-234-9876', 'email': 'igor.ivanov@mail.com'}, 
        {'name': 'Kira', 'phone': '7356-478-9201', 'email': ''}, 
        {'name': 'Leo', 'phone': '+7423-167-2091', 'email': 'leo.pratt@mail.ru'}, 
        {'name': 'Anna', 'phone': '15-674-3912', 'email': 'anna.morrison@tutanota.com'}, 
        {'name': 'Max', 'phone': '+7534-287-0654', 'email': ''}, 
        {'name': 'Charlie', 'phone': '253-346-7024', 'email': 'charlie.jones@gmail.com'}]""",
            "David Eva Kira Leo Liam Milo Viktor",
        ),
    ],
)
def test_7_1_6(data, expected):
    assert m_7_1_6(data) == expected
