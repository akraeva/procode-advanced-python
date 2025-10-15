import pytest
from src.module_11 import (
    m_11_4_1,
)


# для запуска pytest -k "test_11_4_" -q -x --tb=short


# === Тест для задачи 11.4.1 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Example 1
        ("84\n120", "Наибольший общий делитель чисел равен: 12"),
        # Example 2 (повтор предыдущего для проверки)
        ("84\n120", "Наибольший общий делитель чисел равен: 12"),
        # Example 3
        ("48\n180", "Наибольший общий делитель чисел равен: 12"),
        # Example 4
        ("100\n25", "Наибольший общий делитель чисел равен: 25"),
        # Example 5
        ("25\n100", "Наибольший общий делитель чисел равен: 25"),
        # Example 6
        ("111\n3458", "Наибольший общий делитель чисел равен: 1"),
        # Sample Input
        ("56\n98", "Наибольший общий делитель чисел равен: 14"),
    ],
    ids=[
        "Example1",
        "Example2",
        "Example3",
        "Example4",
        "Example5",
        "Example6",
        "Sample",
    ],
)
def test_11_4_1(data, expected):
    assert m_11_4_1(data) == expected
