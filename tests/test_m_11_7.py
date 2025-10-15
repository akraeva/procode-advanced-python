import pytest
from src import module_11
from src.module_11 import m_11_7_1, m_11_7_2, m_11_7_3


# для запуска pytest -k "test_11_7_" -q -x --tb=short


# === Тест для задачи 11.7.1 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        ("Иван\nАлександр\n", "Александр\nАлександр\n"),
        ("Толик\nДурик\n", "Дурик\nДурик\n"),
        ("ф и\nы ь\n", "ы ь\nы ь\n"),
    ],
    ids=["Ivan", "Tolik", "fy_i"],
)
def test_11_7_1(monkeypatch, capsys, data, expected):
    inputs = iter(data.strip().split("\n"))
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    m_11_7_1()
    captured = capsys.readouterr()
    assert captured.out == expected


# === Тест для задачи 11.7.2 ===


def test_11_7_2():
    result = m_11_7_2()
    assert module_11.security_level == 5
    assert result == 10


# === Тест для задачи 11.7.3 ===


def test_11_7_3():
    result = module_11.m_11_7_3()
    assert module_11.total_energy == 80
    assert result == (80, 30)
