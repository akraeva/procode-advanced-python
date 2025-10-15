import pytest
from src.module_11 import (
    m_11_5_1,
    m_11_5_2,
    m_11_5_3,
    m_11_5_4,
    m_11_5_5,
    m_11_5_6,
)


# для запуска pytest -k "test_11_5_" -q -x --tb=short


# === Тест для задачи 11.5.1 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Example input
        ("Cat, Cow, Cheetah, Lion, Camel, Elephant", ["Camel", "Cheetah"]),
        # Test 2
        ("Elephant, Tiger, Cat, Cheetah, Cow", ["Cheetah"]),
        # Test 3
        ("Cat, Lion, Camel, Cobra, Cow, Cheetah", ["Camel", "Cobra", "Cheetah"]),
        # Test 4
        (
            "Crocodile, Dog, Cat, Cheetah, Cow, Chicken",
            ["Cheetah", "Chicken", "Crocodile"],
        ),
        # Test 5
        ("for, mor, bor", []),
        # Sample Input
        (
            "Cat, Cheetah, Crow, Camel, Dog, Crocodile",
            ["Crow", "Camel", "Cheetah", "Crocodile"],
        ),
    ],
    ids=["Example", "Test2", "Test3", "Test4", "Test5", "Sample"],
)
def test_11_5_1(data, expected):
    assert m_11_5_1(data) == expected


# === Тест для задачи 11.5.2 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        ("1 2 3 4 5 6 7 8 9 10 11 12", [6, 12, 18, 24]),
        ("15 25 35 45 55", [30, 90]),
        ("11 22 55", []),
        ("60 20 30", [60, 120]),
        ("10 9 8 7 6 5 4 3 2 1", [6, 12, 18]),
        ("10 20 30 40 50 60", [60, 120]),
    ],
    ids=["Example", "Test2", "Test3", "Test4", "Test5", "Sample"],
)
def test_11_5_2(data, expected):
    assert m_11_5_2(data) == expected


# === Тест для задачи 11.5.3 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Example input
        ("3\n1 80\n2 120\n3 50", [(2, 144.0)]),
        # Test 2
        ("3\n1 85\n2 80\n3 75", [(1, 102.0)]),
        # Test 3
        (
            "6\n1 85\n2 80\n3 70\n7 113\n5 111\n10 1234",
            [(1, 102.0), (5, 133.2), (7, 135.6), (10, 1480.8)],
        ),
        # Sample Input
        (
            "5\n4 65\n8 200\n1 90\n3 88\n7 87",
            [(1, 108.0), (3, 105.6), (7, 104.4), (8, 240.0)],
        ),
    ],
    ids=["Example", "Test2", "Test3", "Sample"],
)
def test_11_5_3(data, expected):
    assert m_11_5_3(data) == expected


# === Тест для задачи 11.5.4 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        ("3\n100\n150\n200", [90.0, 135.0, 180.0]),
        ("3\n111\n222\n333", [99.9, 199.8, 299.7]),
        ("6\n444\n555\n666\n777\n888\n999", [399.6, 499.5, 599.4, 699.3, 799.2, 899.1]),
        ("4\n10\n11\n12\n13", [9.0, 9.9, 10.8, 11.7]),
        ("5\n1\n2\n3\n4\n5", [0.9, 1.8, 2.7, 3.6, 4.5]),
        ("3\n1000\n1050\n1999", [900.0, 945.0, 1799.1]),
    ],
    ids=["Example", "Test2", "Test3", "Test4", "Test5", "Sample"],
)
def test_11_5_4(data, expected):
    assert m_11_5_4(data) == expected


# === Тест для задачи 11.5.5 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Test №2
        (
            "4\nОскар и Розовая дама 2003\nМастер и Маргарита 1967\n"
            "Страна чудес без тормозов и Конец света 2006\nШум и ярость 1929",
            "Книги, выпущенные после 2000 года:\n['Оскар и Розовая дама', "
            "'Страна чудес без тормозов и Конец света']",
        ),
        # Test №3
        (
            "3\nЗулейха открывает глаза 2015\nУнесенные ветром 1936\n"
            "Кот в сапогах 2003",
            "Книги, выпущенные после 2000 года:\n['Зулейха открывает глаза', "
            "'Кот в сапогах']",
        ),
        # Test №4
        ("1\n123 2000", "Книги, выпущенные после 2000 года:\n[]"),
        # Test №5
        ("1\nфыв 2001", "Книги, выпущенные после 2000 года:\n['фыв']"),
        # Sample Input
        (
            "5\nПеснь льда и огня 1996\n1984 1949\nВино из одуванчиков 2000\n"
            "Гарри Поттер и Орден Феникса 2003\nМиф о том, что ты уже всё знаешь 2010",
            "Книги, выпущенные после 2000 года:\n['Гарри Поттер и Орден Феникса', "
            "'Миф о том, что ты уже всё знаешь']",
        ),
    ],
    ids=[
        "mixed_books",
        "two_modern_books",
        "none_new_books",
        "one_new_book",
        "sample_input",
    ],
)
def test_11_5_5(data, expected):
    assert m_11_5_5(data) == expected


# === Тест для задачи 11.5.6 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Test №2
        ("0", "Артефакты после обработки:\n[]"),
        # Test №3
        (
            "3\nАмулет, 1995, 11111\nМеч, 2015, 55550\nЩит, 1999, 333312",
            "Артефакты после обработки:\n[('Меч', 2015, 69437.5)]",
        ),
        # Test №4
        ("1\nЩит, 1999, 333312", "Артефакты после обработки:\n[]"),
        # Test №5
        (
            "1\nЩит, 2001, 333312",
            "Артефакты после обработки:\n[('Щит', 2001, 416640.0)]",
        ),
        # Test №6
        (
            "5\nАмулет, 1995, 1111\nМеч, 2015, 5555\nЩит, 1999, 3333\n"
            "Кубок, 2020, 8888\nКольцо, 2010, 1523",
            "Артефакты после обработки:\n[('Кольцо', 2010, 1903.75), "
            "('Меч', 2015, 6943.75), ('Кубок', 2020, 11110.0)]",
        ),
        # Sample Input
        (
            "4\nАмулет, 1995, 1000\nМеч, 2015, 5000\nЩит, 1999, 3000\nКубок, 2020, 8000",
            "Артефакты после обработки:\n[('Меч', 2015, 6250.0), ('Кубок', 2020, 10000.0)]",
        ),
    ],
    ids=[
        "no_artifacts",
        "one_valid_artifact",
        "old_artifact",
        "one_recent_artifact",
        "multiple_artifacts",
        "sample_input",
    ],
)
def test_11_5_6(data, expected):
    assert m_11_5_6(data) == expected
