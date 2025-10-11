import pytest
from src.module_11 import (
    m_11_6_1,
    m_11_6_2,
    m_11_6_3,
)


# для запуска pytest -k "test_11_6_" -q -x --tb=short


# === Тест для задачи 11.6.1 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Example group
        (100, 110.0),
        (200, 220.0),
        (333, 366.3),
        (0, 0.0),
        (555, 610.5),
        (1000000, 1100000.0),
        (111, 122.1),
    ],
    ids=[
        "hundred",
        "two_hundred",
        "three_three_three",
        "zero",
        "five_five_five",
        "million",
        "sample",
    ],
)
def test_11_6_1(data, expected):
    assert m_11_6_1(data) == expected


# === Тест для задачи 11.6.2 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Example group
        ("Александр Владимиров", "<h2>Александр Владимиров</h2>"),
        ("sdgsgsggsg", "<h2>sdgsgsggsg</h2>"),
        ("1kfhjJF'gjGJ'Jjg", "<h2>1kfhjJF'gjGJ'Jjg</h2>"),
        ("парвольыслаь рпоя опоп ", "<h2>парвольыслаь рпоя опоп </h2>"),
    ],
    ids=["russian_name", "random_letters", "mixed_symbols", "russian_spaces"],
)
def test_11_6_2(data, expected):
    assert m_11_6_2(data) == expected


# === Тест для задачи 11.6.3 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Example group
        ("list\n1 2 3 4 5", [1, 2, 3, 4, 5]),  # list type
        ("tuple\n10 20 30", (10, 20, 30)),  # tuple type
        ("tuple\n1 2 3 4 5", (1, 2, 3, 4, 5)),  # tuple 5 elements
        ("list\n13 -6 -7 -8 22 101", [13, -6, -7, -8, 22, 101]),  # list with negatives
        (
            "tuple\n-5 -6 1 0 11 101 -8 98",
            (-5, -6, 1, 0, 11, 101, -8, 98),
        ),  # long tuple
    ],
    ids=["list_simple", "tuple_simple", "tuple_five", "list_negatives", "tuple_long"],
)
def test_11_6_3(data, expected):
    assert m_11_6_3(data) == expected
