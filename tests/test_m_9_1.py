import pytest
from src.module_9 import (
    m_9_1_1,
    m_9_1_2,
    m_9_1_3,
    m_9_1_4,
)


# === Тест для задачи 9.1.1 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            "5.89 12.34 7.2 9.1 3.14 1.618 8.75 5.89",
            "Сумма минимального и максимального числа: 13.96",
        ),
        (
            "1.5 2.5 3.5 4.5 2.5 1.5",
            "Сумма минимального и максимального числа: 6.0",
        ),
        (
            "7.8 3.3 9.5 12.1 4.6 3.3",
            "Сумма минимального и максимального числа: 15.4",
        ),
        (
            "20.1 12.3 8.5 5.7 6.4 8.5 20.1",
            "Сумма минимального и максимального числа: 25.8",
        ),
        (
            "10.5 3.2 8.1 15.6 4.4 8.1",
            "Сумма минимального и максимального числа: 18.8",
        ),
    ],
    ids=[
        "Test_1 (with duplicates, min=1.618, max=12.34)",
        "Test_2 (min=1.5, max=4.5)",
        "Test_3 (min=3.3, max=12.1)",
        "Test_4 (min=5.7, max=20.1, repeated max)",
        "Sample (min=3.2, max=15.6)",
    ],
)
def test_9_1_1(data, expected):
    assert m_9_1_1(data) == expected


# === Тест для задачи 9.1.2 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            "лиса зайчонок белка лиса орёл зайчонок\nлиса",
            "Количество уникальных обитателей в Лесном Реестре: 4"
            ""
            "\nОбитатель 'лиса' зарегистрирован.",
        ),
        (
            "лиса зайчонок белка лиса орёл зайчонок\nбобр",
            "Количество уникальных обитателей в Лесном Реестре: 4"
            ""
            "\nОбитатель 'бобр' не зарегистрирован.",
        ),
        (
            "сова заяц белка белка заяц\nзаяц",
            "Количество уникальных обитателей в Лесном Реестре: 3\n"
            "Обитатель 'заяц' зарегистрирован.",
        ),
        (
            "белка ёжик медведь ёжик орёл\nорёл",
            "Количество уникальных обитателей в Лесном Реестре: 4"
            "\nОбитатель 'орёл' зарегистрирован.",
        ),
        (
            "лиса сова сова медведь\nсова",
            "Количество уникальных обитателей в Лесном Реестре: 3"
            "\nОбитатель 'сова' зарегистрирован.",
        ),
        (
            "зайчонок ёжик ёжик зайчонок\nбобр",
            "Количество уникальных обитателей в Лесном Реестре: 2"
            "\nОбитатель 'бобр' не зарегистрирован.",
        ),
        (
            "ёжик сова сова лиса медведь ёжик\nмедведь",
            "Количество уникальных обитателей в Лесном Реестре: 4"
            "\nОбитатель 'медведь' зарегистрирован.",
        ),
    ],
    ids=[
        "Example_1 (fox present)",
        "Example_2 (beaver absent)",
        "Test_2 (hare present, duplicates removed)",
        "Test_3 (eagle present)",
        "Test_4 (owl present)",
        "Test_5 (beaver absent, only hedgehog and hare unique)",
        "Sample (bear present)",
    ],
)
def test_9_1_2(data, expected):
    assert m_9_1_2(data) == expected


# === Тест для задачи 9.1.3 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        ("348597", "Да"),
        ("123123", "Нет"),
        ("1231234", "Нет"),
        ("0987654321", "Да"),
        ("9440870934763796", "Нет"),
        ("123456", "Да"),
    ],
    ids=[
        "Example_1 (valid)",
        "Example_2 (invalid)",
        "Test_2 (invalid, extra digit)",
        "Test_3 (valid, descending digits)",
        "Test_4 (invalid long number)",
        "Sample (valid straight sequence)",
    ],
)
def test_9_1_3(data, expected):
    assert m_9_1_3(data) == expected


# === Тест для задачи 9.1.4 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        ("1234\n2341", "Да"),
        ("1\n2", "Нет"),
        ("234\n123", "Нет"),
        ("001122\n110022", "Да"),
        ("3456\n7890", "Нет"),
        ("327428\n824723", "Да"),
    ],
    ids=[
        "Example_1 (rotation possible)",
        "Example_2 (different single digits)",
        "Test_2 (different length, no rotation)",
        "Test_3 (leading zeros, valid rotation)",
        "Test_4 (completely different numbers)",
        "Sample (rotation match)",
    ],
)
def test_9_1_4(data, expected):
    assert m_9_1_4(data) == expected
