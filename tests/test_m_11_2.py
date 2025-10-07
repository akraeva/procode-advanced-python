import pytest
from src.module_11 import (
    m_11_2_1,
    m_11_2_2,
)


# для запуска pytest -k "test_11_2_" -q -x --tb=short


# === Тест для задачи 11.2.1 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # test_1
        ("8 42 -17 0 99 23 -5 14 76 32", "8 42 -17 0 99"),
        # test_2
        ("120 13 -45 88 4 9 11 6 -8 77", "120 13 -45 88 4"),
        # test_3
        ("-1 -2 -3 -4 -5 -6 -7 -8 -9 0", "-1 -2 -3 -4 -5"),
        # test_4
        ("12 15 -50 1 3 4 0 98 77 66", "12 15 -50 1 3"),
    ],
    ids=["example_1", "example_2", "negative_numbers", "sample_input"],
)
def test_11_2_1(data, expected, capsys):
    m_11_2_1(data)
    captured = capsys.readouterr().out.strip()
    assert captured == expected


# === Тест для задачи 11.2.2 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # test_1
        ("Артефакт Камень Древний\nМеч Щит Камень", "Артефакт Камень Древний Меч Щит"),
        # test_2
        (
            "Манускрипт Дневник Руна\nРуна Чаша Амулет",
            "Манускрипт Дневник Руна Чаша Амулет",
        ),
        # test_3
        (
            "Манускрипт Дневник Руны\nРуна Чаша Амулет",
            "Манускрипт Дневник Руны Руна Чаша Амулет",
        ),
        # test_4
        (
            "Светлый Черный Белый\nКрасный Зеленый Черный",
            "Светлый Черный Белый Красный Зеленый",
        ),
    ],
    ids=["example_1", "example_2", "variant_ruны", "colors_case"],
)
def test_11_2_2(data, expected, capsys):
    m_11_2_2(data)
    captured = capsys.readouterr().out.strip()
    assert captured == expected
