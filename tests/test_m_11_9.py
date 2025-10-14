import pytest
from src.module_11 import m_11_9_1, m_11_9_2, m_11_9_3


# для запуска pytest -k "test_11_9_" -q -x --tb=short


# === Тест для задачи 11.9.1 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Example1
        ("10 -3 7 -2 5", 22),
        # Test2
        ("5 -5 6 -6 7 -7", 5),
        # Test3
        ("0", 5),
        # Test4
        ("-5", 0),
        # Test5
        ("100 -20 -33 -6", 46),
        # Test6
        ("1 -15 -40", -49),
        # Sample
        ("-10 5 11 12 13 -6", 30),
    ],
    ids=[
        "Example1",
        "Test2",
        "Test3",
        "Test4",
        "Test5",
        "Test6",
        "Sample",
    ],
)
def test_11_9_1(data, expected):
    assert m_11_9_1(data) == expected


# === Тест для задачи 11.9.2 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Example1
        ("История - это важно!", "istoriya+-+eto+vazhno+"),
        # Test2
        (
            "Москва, Санкт-Петербург и Казань - красивые города!",
            "moskva+sankt-peterburg+i+kazan+-+krasivye+goroda+",
        ),
        # Test3
        (
            "Инвестиции - это важный шаг к финансовой независимости.",
            "investicii+-+eto+vazhnyy+shag+k+finansovoy+nezavisimosti+",
        ),
        # Sample
        ("Привет, мир! Как дела?", "privet+mir+kak+dela+"),
    ],
    ids=[
        "Example1",
        "Test2",
        "Test3",
        "Sample",
    ],
)
def test_11_9_2(data, expected):
    assert m_11_9_2(data) == expected


# === Тест для задачи 11.9.3 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Example1
        ("admin", "✅ Данные успешно удалены (пользователь: admin)"),
        # Example2
        ("manager", "✅ Данные успешно удалены (пользователь: manager)"),
        # Example3
        ("guest", "Ошибка: доступ запрещен"),
        # Test2
        ("admin", "✅ Данные успешно удалены (пользователь: admin)"),
        # Test3
        ("Коля", "Ошибка: доступ запрещен"),
        # Test4
        ("manager", "✅ Данные успешно удалены (пользователь: manager)"),
        # Sample
        ("Вася", "Ошибка: доступ запрещен"),
    ],
    ids=[
        "Example1",
        "Example2",
        "Example3",
        "Test2",
        "Test3",
        "Test4",
        "Sample",
    ],
)
def test_11_9_3(data, expected):
    assert m_11_9_3(data) == expected
