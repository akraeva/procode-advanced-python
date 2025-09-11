import pytest
from src.module_4 import m_4_1_3, m_4_1_4

# === Тесты для задачи 4.1.3 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        ("3 10 14 21", 14),
        ("1 2 3 4", None),
        ("21 7 14", 21),
        ("3 6 10 20 30 40 101", None),
        ("1 2 3 7", 7),
        ("100 100 42 15", 42),
        ("0", 0),
        ("1 2 7 9 0", 7),
    ],
)
def test_m_4_1_3(data, expected):
    assert m_4_1_3(data) == expected


# === Тесты для задачи 4.1.4 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        ("Hello, cosmic traveler!", "Hello"),
        ("Greetings, universe!", None),
        ("Hello, cosmic traveler!", "Hello"),
        ("Hi, all beings!", "Hi"),
        ("To infinity, and beyond!", "To"),
        ("This message is secret.", "message"),
        ("Greetings, universe! Greetings, universe!", None),
    ],
)
def test_m_4_1_4(data, expected):
    assert m_4_1_4(data) == expected
