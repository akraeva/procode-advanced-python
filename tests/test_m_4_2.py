import pytest
from src.module_4 import (
    terminator,
    check_parity,
    can_form_triangle,
    m_4_2_4,
    get_strongest_avenger,
)


# === Тест для задачи 4.2.1 ===


def test_m_4_1_1():
    assert terminator() == "I’LL BE BACK"


# === Тест для задачи 4.2.2 ===


@pytest.mark.parametrize(
    "number, expected",
    [
        (2, "четное"),
        (10, "четное"),
        (3, "нечетное"),
        (15, "нечетное"),
        (0, None),  # если ноль — считаем невалидным
        (-4, None),  # отрицательные тоже None
        (-7, None),
    ],
)
def test_m_4_1_2(number, expected):
    assert check_parity(number) == expected


# === Тест для задачи 4.2.3 ===


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (5, 7, 10, True),
        (1, 2, 3, False),
        (3, 3, 3, True),
        (10, 6, 5, True),
        (7, 10, 5, True),
        (2, 2, 3, True),
        (2, 2, 4, False),
        (100, 50, 50, False),
        (100, 60, 50, True),
    ],
)
def test_m_4_1_3(a, b, c, expected):
    assert can_form_triangle(a, b, c) == expected


# === Тест для задачи 4.2.4 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            "8 17 -4 31 -12 25 0",
            "-372\n[8, 17, -4, 31, -12, 25, 0]",
        ),
        (
            "12 -5 22 10 0 8",
            "-110\n[12, -5, 22, 10, 0, 8]",
        ),
        (
            "45 67 32 -5 12 78",
            "-390\n[45, 67, 32, -5, 12, 78]",
        ),
        (
            "-1 -9 -4 3 7 15",
            "-135\n[-1, -9, -4, 3, 7, 15]",
        ),
        (
            "2 13 -3 8 5 -1",
            "-39\n[2, 13, -3, 8, 5, -1]",
        ),
        (
            "0 34 12 -8 5 1",
            "-272\n[0, 34, 12, -8, 5, 1]",
        ),
    ],
)
def test_m_4_2_4(data, expected):
    assert m_4_2_4(data) == expected


# === Тест для задачи 4.2.5 ===


@pytest.mark.parametrize(
    "names, powers, expected",
    [
        (["Iron Man", "Thor", "Hulk"], [85, 95, 90], "Thor"),
        (["Captain America", "Black Widow"], [80, 75], "Captain America"),
        (["Hawkeye"], [65], "Hawkeye"),
        (["Spider-Man", "Doctor Strange", "Ant-Man"], [70, 90, 70], "Doctor Strange"),
        (["Black Panther", "Vision", "Scarlet Witch"], [88, 92, 89], "Vision"),
        # проверим случай равных значений — берётся первый
        (["Captain America", "Black Widow"], [50, 50], "Captain America"),
    ],
)
def test_m_4_2_5(names, powers, expected):
    assert get_strongest_avenger(names, powers) == expected
