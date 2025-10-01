import pytest
from src.module_9 import (
    m_9_5_1,
    m_9_5_2,
    m_9_5_3,
)


# === Test для задачи 9.5.1 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Example
        (
            "2\nНаташа Александр\n3\nНаташа Александр Вера",
            "A is subset of B? True\n"
            "B is superset of A? True\n"
            "A and B are disjoint? False",
        ),
        # Test №2
        (
            "2\nЕлена Павел\n6\nИрина Павел Артем Татьяна Андрей Ольга",
            "A is subset of B? False\n"
            "B is superset of A? False\n"
            "A and B are disjoint? False",
        ),
        # Test №3
        (
            "1\nАлексей\n3\nАлексей Борис Виктор",
            "A is subset of B? True\n"
            "B is superset of A? True\n"
            "A and B are disjoint? False",
        ),
        # Test №4
        (
            "5\nНиколай Артем Светлана Антон Галина\n5\nАртем Светлана Антон Галина Николай",
            "A is subset of B? True\n"
            "B is superset of A? True\n"
            "A and B are disjoint? False",
        ),
        # Test №5
        (
            "5\nПолина Василиса Тимофей Захар Маргарита\n3\nТимофей Захар Маргарита",
            "A is subset of B? False\n"
            "B is superset of A? False\n"
            "A and B are disjoint? False",
        ),
        # Test №6
        (
            "0\n\n0\n",
            "A is subset of B? True\n"
            "B is superset of A? True\n"
            "A and B are disjoint? True",
        ),
        # Sample
        (
            "4\nАнна Борис Василий Глеб\n3\nДмитрий Екатерина Федор",
            "A is subset of B? False\n"
            "B is superset of A? False\n"
            "A and B are disjoint? True",
        ),
    ],
    ids=[
        "Example",
        "Test2",
        "Test3",
        "Test4",
        "Test5",
        "Test6",
        "Sample",
    ],
)
def test_9_5_1(data, expected):
    assert m_9_5_1(data) == expected


# === Test для задачи 9.5.2 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Example 1
        (
            "Дон, Сим, Боб\nДон, Сим, Боб, Алиса",
            "Первая группа - подмножество второй.",
        ),
        # Example 2
        (
            "Джек, Джилл\nМария, Алекс",
            "Группы не пересекаются.",
        ),
        # Test №2
        (
            "Анна, Борис\nВиктор, Дарья",
            "Группы не пересекаются.",
        ),
        # Test №3
        (
            "a, b\na, b, c, d",
            "Первая группа - подмножество второй.",
        ),
        # Test №4
        (
            "a, b, c, d\na, b",
            "Вторая группа - подмножество первой.",
        ),
        # Test №5
        (
            "a, b\nc, d",
            "Группы не пересекаются.",
        ),
        # Test №6
        (
            "a, b, c\nb, c, d",
            "Группы пересекаются, но ни одна не является подмножеством другой.",
        ),
        # Sample
        (
            "Анна, Борис, Виктор, Дарья\nАнна, Борис",
            "Вторая группа - подмножество первой.",
        ),
    ],
    ids=[
        "Example1",
        "Example2",
        "Test2",
        "Test3",
        "Test4",
        "Test5",
        "Test6",
        "Sample",
    ],
)
def test_9_5_2(data, expected):
    assert m_9_5_2(data) == expected


# === Test для задачи 9.5.3 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Example 1
        (
            "☠ ⚔ 🕯\n☠ 🔮 ⚔ 📜 🕯",
            "Первый свиток скрыт в тексте второго.",
        ),
        # Example 2
        (
            "✡ ⚜ ☀\n♆ 🜂 🜄",
            "Свитки принадлежат разным эпохам.",
        ),
        # Example 3
        (
            "☀ ☾ ✹\n☀ ✡ ☾ ✦ ✹",
            "Первый свиток скрыт в тексте второго.",
        ),
        # Example 4
        (
            "☥ ☼ ☾\n☥ ☀ ☾ ✡",
            "Свитки имеют общие символы, но их порядок различен.",
        ),
        # Test №1
        (
            "⚡ 🔥 💧\n🌿 ⚡ 🔥 🌙 💧",
            "Первый свиток скрыт в тексте второго.",
        ),
        # Test №2
        (
            "☀ ☁ 🌙\n🌙 ☀ ☁",
            "Свитки имеют общие символы, но их порядок различен.",
        ),
        # Test №3
        (
            "⚜ 🦇 🩸\n🦇 🩸 ⚜",
            "Свитки имеют общие символы, но их порядок различен.",
        ),
        # Test №4
        (
            "🔮 🌌 ✨\n🕯 🏹 🎭",
            "Свитки принадлежат разным эпохам.",
        ),
        # Test №5
        (
            "🗡 🏹 🔥\n🗡 🏹 🔥 ⚔ 🛡",
            "Первый свиток скрыт в тексте второго.",
        ),
        # Sample
        (
            "⚡ 🔥 💧\n🌿 ⚡ 🔥 🌙 💧",
            "Первый свиток скрыт в тексте второго.",
        ),
    ],
    ids=[
        "Example1",
        "Example2",
        "Example3",
        "Example4",
        "Test1",
        "Test2",
        "Test3",
        "Test4",
        "Test5",
        "Sample",
    ],
)
def test_9_5_3(data, expected):
    assert m_9_5_3(data) == expected
