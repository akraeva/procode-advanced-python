import pytest
from src.module_11 import m_11_8_1, m_11_8_2, m_11_8_3


# для запуска pytest -k "test_11_8_" -q -x --tb=short


# === Тест для задачи 11.8.1 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # test_1
        ("5 13", "📏 Площадь помещения: 65 м²"),
        # test_2
        ("55 55", "📏 Площадь помещения: 3025 м²"),
        # test_3
        ("0 11", "📏 Площадь помещения: 0 м²"),
        # sample
        ("11 22", "📏 Площадь помещения: 242 м²"),
    ],
    ids=["example_1", "big_square", "zero_width", "sample_case"],
)
def test_11_8_1(monkeypatch, capsys, data, expected):
    w, h = map(int, data.split())
    result = m_11_8_1(w, h)
    captured = capsys.readouterr().out.strip()
    assert captured == expected
    assert result == w * h


# === Тест для задачи 11.8.2 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # example_1
        (
            "apple banana orange grape\nяблоко банан апельсин виноград",
            {
                "apple": "яблоко",
                "banana": "банан",
                "orange": "апельсин",
                "grape": "виноград",
            },
        ),
        # test_2
        (
            "apple banana orange grape\nяблоко банан апельсин виноград",
            {
                "apple": "яблоко",
                "banana": "банан",
                "orange": "апельсин",
                "grape": "виноград",
            },
        ),
        # test_3
        (
            "cat dog elephant rabbit\nкот собака слон кролик",
            {"cat": "кот", "dog": "собака", "elephant": "слон", "rabbit": "кролик"},
        ),
        # sample_case
        (
            "doctor engineer teacher artist\nдоктор инженер учитель художник",
            {
                "doctor": "доктор",
                "engineer": "инженер",
                "teacher": "учитель",
                "artist": "художник",
            },
        ),
    ],
    ids=["example_1", "repeat_case", "animals", "professions"],
)
def test_11_8_2(data, expected):
    str1, str2 = data.split("\n")
    result = m_11_8_2(str1, str2)
    assert result == expected


# === Тест для задачи 11.8.3 ===


@pytest.mark.parametrize(
    "data, expected_output",
    [
        # example_1
        ("25", 5.0),
        # test_2
        ("22", 4.69),
        # test_3
        ("0", "Ошибка: число должно быть больше нуля!"),
        # test_4
        ("100", 10.0),
        # test_5
        ("11", 3.32),
        # test_6
        ("-100", "Ошибка: число должно быть больше нуля!"),
        # sample_case
        ("12", 3.46),
    ],
    ids=["example_1", "test_2", "test_3", "test_4", "test_5", "test_6", "sample_case"],
)
def test_11_8_3(data, expected_output):
    n = float(data)
    result = m_11_8_3(n)
    assert result == expected_output, f"Ожидалось {expected_output}, получено {result}"
