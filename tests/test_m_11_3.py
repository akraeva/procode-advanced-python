import pytest
from src.module_11 import (
    m_11_3_1,
    m_11_3_2,
    m_11_3_3,
)


# для запуска pytest -k "test_11_3_" -q -x --tb=short


# === Тест для задачи 11.3.1 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # === Example 1 ===
        (
            [
                "Привет!",
                ["Как дела?", ["Хорошо, а у тебя?", ["Тоже отлично!"]]],
                "Что нового?",
            ],
            5,
        ),
        # === Example 2 ===
        (
            [
                "Начинаем собрание",
                ["Кто присутствует?", ["Я", "Я тоже"]],
                "Переходим к вопросам",
                ["Когда дедлайн?", ["Через неделю", ["А можно отложить?", ["Нет!"]]]],
            ],
            9,
        ),
    ],
    ids=["simple_nested", "deep_nested"],
)
def test_11_3_1(data, expected):
    assert m_11_3_1(data) == expected


# === Тест для задачи 11.3.2 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # === Example 1 ===
        ([12, -13, 17, -8, 5], 13),
        # === Example 2 ===
        ([100, -50, -30, 20, 10], 50),
        # === Example 3 ===
        ([-15, -10, -5, -20], -50),
        # === Example 4 ===
        ([42, -17, 13, -25, 7, 3], 23),
        # === Example 5 ===
        ([0, 0, 0, 0, 0], 0),
        # === Sample ===
        ([5, -2, 10, -7, 8], 14),
    ],
    ids=["basic", "mixed", "all_negative", "mixed2", "all_zero", "sample"],
)
def test_11_3_2(data, expected):
    assert m_11_3_2(data) == expected


# === Тест для задачи 11.3.3 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Example 1 — сложная вложенность с числами, булевыми и строками
        (
            [
                42,
                [3.14, [True, False], "GPT-4"],
                ["Python", [10, 20], ["AI", [100, 200, [300]]]],
                "Data Science",
            ],
            [
                42,
                3.14,
                True,
                False,
                "GPT-4",
                "Python",
                10,
                20,
                "AI",
                100,
                200,
                300,
                "Data Science",
            ],
        ),
        # Example 2 — вложенные пустые списки
        (
            [[], ["A", ["B", []]], [[["C"]]], 0],
            ["A", "B", "C", 0],
        ),
        # Test 3 — полностью пустой список
        (
            [],
            [],
        ),
        # Test 4 — список без вложений
        (
            [1, 2, 3],
            [1, 2, 3],
        ),
        # Test 5 — разные типы элементов и глубина вложенности
        (
            [[[[1]]], [[2, [3, [4]]]], "end"],
            [1, 2, 3, 4, "end"],
        ),
    ],
    ids=["complex", "nested_empty", "empty", "flat", "deep_mixed"],
)
def test_11_3_3(data, expected):
    assert m_11_3_3(data) == expected
