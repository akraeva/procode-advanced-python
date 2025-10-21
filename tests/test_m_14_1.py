import pytest
from src.module_14 import (
    m_14_1_2,
    m_14_1_3,
    m_14_1_4,
    m_14_1_5,
)

# для запуска pytest -k "test_14_1_" -q -x --tb=short


# === Тест для задачи 14.1.2 ===


@pytest.mark.parametrize(
    "file_content, expected",
    [
        # Базовый пример из условия
        (
            "В начале было слово.\nИ слово было у Бога.\nИ слово было Бог.\n",
            "В начале было слово.\nИ слово было у Бога.\nИ слово было Бог.\n"
            "В начале было слово.",
        ),
        # Одна строка в файле
        ("Одинокая строка.\n", "Одинокая строка.\nОдинокая строка."),
        # Файл без перевода строки в конце
        (
            "Строка без перевода в конце",
            "Строка без перевода в конце\nСтрока без перевода в конце",
        ),
        # Строки с пробелами (важно: не убираем пробелы)
        (
            "  Первая строка\n   Вторая строка  \n",
            "  Первая строка\n   Вторая строка  \n  Первая строка",
        ),
        # Файл с пустыми строками
        ("   \n    \n", "   \n    \n   "),
    ],
)
def test_14_1_2(tmp_path, file_content, expected):
    file_path = tmp_path / "scroll.txt"
    file_path.write_text(file_content, encoding="utf-8")
    assert m_14_1_2(str(file_path)) == expected


# === Тест для задачи 14.1.3 ===


@pytest.mark.parametrize(
    "content, expected",
    [
        # Базовый пример из условия
        (
            "В начале было слово.\n" "И слово было у Бога.\n" "И слово было Бог.\n",
            "В начале было слово.\n" "И слово было у Бога.\n" "И слово было Бог.\n" "3",
        ),
        # Одинарная строка
        ("Одинокая строка.\n", "Одинокая строка.\n1"),
        # Строки с лишними пробелами и пустыми символами
        (
            "    Первая строка    \n" "       Вторая строка\n" "Третья строка    ",
            "Первая строка\n" "Вторая строка\n" "Третья строка\n" "3",
        ),
        # Файл с пустыми строками (они должны учитываться)
        (
            "Первая строка\n" "    \n" "Вторая строка\n",
            "Первая строка\n" "\n" "Вторая строка\n" "3",
        ),
    ],
)
def test_14_1_3(tmp_path, content, expected):
    file_path = tmp_path / "scroll.txt"
    file_path.write_text(content, encoding="utf-8")
    result = m_14_1_3(str(file_path))
    assert result == expected


# === Тест для задачи 14.1.4 ===


@pytest.mark.parametrize(
    "content, expected",
    [
        # Пример из задания
        ("10\n-2\n17\n5\n", 30),
        # Все положительные
        ("1\n2\n3\n4\n", 10),
        # Все отрицательные
        ("-5\n-5\n-5\n-5\n", -20),
        # Смешанные значения
        ("100\n-50\n25\n-25\n", 50),
        # Нули
        ("0\n0\n0\n0\n", 0),
    ],
    ids=["example", "positive", "negative", "mixed", "zeros"],
)
def test_14_1_4(tmp_path, monkeypatch, content, expected):
    file_path = tmp_path / "ancient_key.txt"
    file_path.write_text(content, encoding="utf-8")
    monkeypatch.chdir(tmp_path)
    assert m_14_1_4() == expected


# === Тест для задачи 14.1.5 ===


@pytest.mark.parametrize(
    "content, expected",
    [
        # === Example from the task ===
        (
            "Точка доступа №1: координата X = 42\n"
            "Ошибка на уровне -15. Повторите через 30 секунд!\n"
            "В секторе B4 нашли 102 артефакта и -7 ловушек\n"
            "Финальный контроль: 0\n",
            "1 42 -15 30 4 102 -7 0",
        ),
        # === Only positive ===
        (
            "A1 B2 C3",
            "1 2 3",
        ),
        (
            "Ошибка -100 на уровне 20 и -3 повторения",
            "-100 20 -3",
        ),
        (
            "-5 в начале, потом текст, потом 99 в конце",
            "-5 99",
        ),
    ],
    ids=["task_example", "simple_positive", "mixed_signs", "edge_positions"],
)
def test_14_1_5(tmp_path, monkeypatch, content, expected):
    file_path = tmp_path / "fragments.txt"
    file_path.write_text(content, encoding="utf-8")
    monkeypatch.chdir(tmp_path)

    assert m_14_1_5() == expected
