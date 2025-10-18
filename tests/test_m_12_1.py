import pytest
from textwrap import dedent
from src.module_12 import (
    m_12_1_1,
    m_12_1_2,
    m_12_1_3,
    m_12_1_4,
    m_12_1_5,
    m_12_1_6,
    m_12_1_7,
    m_12_1_8,
    m_12_1_9,
    m_12_1_10,
)
import src.module_12 as module

# для запуска pytest -k "test_12_1_" -q -x --tb=short


# === Тест для задачи 12.1.1 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Sample Input
        (
            ("Двигатель", "Жизнеобеспечение", "Оружие"),
            "Проверка систем:\n- Двигатель: OK\n- Жизнеобеспечение: OK"
            "\n- Оружие: OK",
        ),
        # ✅ Тест №2
        (
            ("Сканер", "Гиперпрыжковый двигатель", "Лазерные пушки", "m_12_1_6ы"),
            "Проверка систем:\n- Сканер: OK\n- Гиперпрыжковый двигатель: OK"
            "\n- Лазерные пушки: OK\n- m_12_1_6ы: OK",
        ),
        # ✅ Тест №3
        (
            ("Радар", "Навигация"),
            "Проверка систем:\n- Радар: OK\n- Навигация: OK",
        ),
    ],
    ids=["sample", "test_2", "test_3"],
)
def test_12_1_1(data, expected):
    assert m_12_1_1(*data) == expected


# === Тест для задачи 12.1.2 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Sample Input
        (
            dict(секция4="Редкие минералы", секция2="Оружие", секция1="Патроны"),
            'Контейнер 1: "Патроны"\nКонтейнер 2: "Оружие"\nКонтейнер 4: "Редкие минералы"',
        ),
        # ✅ Тест №2
        (
            dict(box3="Ресурсы", box1="Части корабля", box2="Запасы"),
            'Контейнер 1: "Части корабля"\nКонтейнер 2: "Запасы"\nКонтейнер 3: "Ресурсы"',
        ),
        # ✅ Тест №3
        (
            dict(
                контейнер5="Металл", контейнер2="Электроника", контейнер1="Медикаменты"
            ),
            'Контейнер 1: "Медикаменты"\nКонтейнер 2: "Электроника"\nКонтейнер 5: "Металл"',
        ),
        # ✅ Тест №4
        (
            dict(контейнер1="Еда", контейнер2="Вода", контейнер3="Инструменты"),
            'Контейнер 1: "Еда"\nКонтейнер 2: "Вода"\nКонтейнер 3: "Инструменты"',
        ),
        # ✅ Тест №5
        (
            dict(контейнер1="Провизия", контейнер2="Оружие", контейнер3="Топливо"),
            'Контейнер 1: "Провизия"\nКонтейнер 2: "Оружие"\nКонтейнер 3: "Топливо"',
        ),
    ],
    ids=["sample", "test_2", "test_3", "test_4", "test_5"],
)
def test_12_1_2(data, expected):
    assert m_12_1_2(**data) == expected


# === Тест для задачи 12.1.3 ===


@pytest.mark.parametrize(
    "args, expected_output",
    [
        # --- Sample Input ---
        # пройти_через_астероиды(5)
        (
            (5,),
            dedent(
                """\
            Шаг 1: Осталось 5 астероидов
            Шаг 2: Осталось 4 астероида
            Шаг 3: Осталось 3 астероида
            Шаг 4: Осталось 2 астероида
            Шаг 5: Остался 1 астероид
            Шаг 6: Поле пройдено!
        """
            ),
        ),
        # --- Test №2 ---
        # пройти_через_астероиды(3)
        (
            (3,),
            dedent(
                """\
            Шаг 1: Осталось 3 астероида
            Шаг 2: Осталось 2 астероида
            Шаг 3: Остался 1 астероид
            Шаг 4: Поле пройдено!
        """
            ),
        ),
        # --- Test №3 ---
        # пройти_через_астероиды(7)
        (
            (7,),
            dedent(
                """\
            Шаг 1: Осталось 7 астероидов
            Шаг 2: Осталось 6 астероидов
            Шаг 3: Осталось 5 астероидов
            Шаг 4: Осталось 4 астероида
            Шаг 5: Осталось 3 астероида
            Шаг 6: Осталось 2 астероида
            Шаг 7: Остался 1 астероид
            Шаг 8: Поле пройдено!
        """
            ),
        ),
        # --- Test №4 ---
        # пройти_через_астероиды(1)
        (
            (1,),
            dedent(
                """\
            Шаг 1: Остался 1 астероид
            Шаг 2: Поле пройдено!
        """
            ),
        ),
    ],
    ids=["five_asteroids", "three_asteroids", "seven_asteroids", "one_asteroid"],
)
def test_12_1_3(capsys, args, expected_output):
    m_12_1_3(*args)
    captured = capsys.readouterr()
    assert captured.out == expected_output


# === Тест для задачи 12.1.4 ===


@pytest.mark.parametrize(
    "a, b, expected",
    [
        # ✅ Sample test
        (24, 36, 12),  # sample
        # ✅ Тест №2 — числа имеют общий делитель
        (18, 27, 9),
        # ✅ Тест №3 — одно число делится на другое
        (10, 5, 5),
        # ✅ Тест №4 — взаимно простые числа
        (7, 13, 1),
        # ✅ Тест №5 — большие числа с НОД > 1
        (462, 1071, 21),
        # ✅ Тест №6 — одинаковые числа
        (20, 20, 20),
        # ✅ Тест №7 — одно из чисел равно нулю
        (0, 25, 25),
        # ✅ Тест №8 — оба числа нули (граничный случай)
        (0, 0, 0),
    ],
    ids=[
        "sample",
        "common_divisor",
        "divisible_pair",
        "coprime_numbers",
        "large_numbers",
        "equal_numbers",
        "zero_and_number",
        "double_zero",
    ],
)
def test_12_1_4(a, b, expected):
    """Проверяет корректность рекурсивной функции найти_нод."""
    assert m_12_1_4(a, b) == expected


# === Тест для задачи 12.1.5 ===


@pytest.mark.parametrize(
    "n, expected",
    [
        # ✅ Sample test
        (7, 294),  # sample
        # ✅ Тест №2 — ноль
        (0, 0),
        # ✅ Тест №3 — отрицательное число
        (-3, -126),
        # ✅ Тест №4 — маленькое положительное число
        (1, 42),
        # ✅ Тест №5 — крупное число
        (1000, 42000),
        # ✅ Тест №6 — большое отрицательное число
        (-250, -10500),
    ],
    ids=[
        "sample",
        "zero",
        "negative_number",
        "small_positive",
        "large_number",
        "large_negative",
    ],
)
def test_12_1_5(n, expected):
    """Проверяет работу lambda-функции зашифровать."""
    assert m_12_1_5(n) == expected


# === Тест для задачи 12.1.6 ===


def test_12_1_6_basic():
    shield = m_12_1_6()
    assert shield() == 10
    assert shield() == 20
    assert shield() == 30


@pytest.mark.parametrize(
    "calls, expected",
    [
        (1, 10),
        (5, 50),
        (10, 100),
    ],
    ids=["one_call", "five_calls", "ten_calls"],
)
def test_12_1_6_parametrize(calls, expected):
    shield = m_12_1_6()
    result = None
    for _ in range(calls):
        result = shield()
    assert result == expected


# === Тест для задачи 12.1.7 ===


def test_12_1_7_basic():

    assert module.мощность == 50
    m_12_1_7()
    assert module.мощность == 75


def test_12_1_7_multiple_calls():

    module.мощность = 50
    m_12_1_7()  # +25
    m_12_1_7()  # +25
    m_12_1_7()  # +25

    assert module.мощность == 125


@pytest.mark.parametrize(
    "initial, calls, expected",
    [
        (50, 1, 75),
        (50, 4, 150),
        (100, 2, 150),
        (0, 3, 75),
    ],
    ids=["one_call", "four_calls", "two_calls_from_100", "three_calls_from_zero"],
)
def test_12_1_7_parametrized(initial, calls, expected):
    module.мощность = initial
    for _ in range(calls):
        m_12_1_7()
    assert module.мощность == expected


# === Тест для задачи 12.1.8 ===


def test_12_1_8_basic():
    ИИ = m_12_1_8()
    assert ИИ() == 120
    assert ИИ() == 140
    assert ИИ() == 160


def test_12_1_8_multiple_instances():
    ИИ1 = m_12_1_8()
    ИИ2 = m_12_1_8()

    assert ИИ1() == 120
    assert ИИ1() == 140
    assert ИИ2() == 120  # новый ИИ должен начинать заново
    assert ИИ1() == 160
    assert ИИ2() == 140


@pytest.mark.parametrize(
    "calls, expected",
    [
        (1, 120),
        (2, 140),
        (5, 200),
    ],
    ids=["one_call", "two_calls", "five_calls"],
)
def test_12_1_8_parametrize(calls, expected):
    ИИ = m_12_1_8()
    result = None
    for _ in range(calls):
        result = ИИ()
    assert result == expected


# === Тест для задачи 12.1.9 ===


def test_12_1_9_base_shield():
    assert m_12_1_9() == 200


def test_12_1_9_custom_function():
    def мега_щит():
        return 300

    мега_щит = module.улучшить_щит(мега_щит)
    assert мега_щит() == 600


@pytest.mark.parametrize(
    "value, expected",
    [
        (1, 2),
        (10, 20),
        (123, 246),
        (0, 0),
        (-5, -10),
    ],
    ids=["one", "ten", "hundred_twenty_three", "zero", "negative"],
)
def test_12_1_9_parametrize(value, expected):
    def test_func():
        return value

    wrapped = module.улучшить_щит(test_func)
    assert wrapped() == expected


# === Тест для задачи 12.1.10 ===


def test_12_1_10_base_attack():
    assert m_12_1_10() == pytest.approx(150.0)


def test_12_1_10_custom_100_percent():
    """Проверяет декоратор с усилением 100%."""

    @module.модификатор_урона(100)
    def атака():
        return 80

    assert атака() == pytest.approx(160.0)


def test_12_1_10_custom_25_percent():

    @module.модификатор_урона(25)
    def атака():
        return 200

    assert атака() == pytest.approx(250.0)


def test_12_1_10_custom_75_percent():

    @module.модификатор_урона(75)
    def атака():
        return 120

    assert атака() == pytest.approx(210.0)


@pytest.mark.parametrize(
    "percent, base, expected",
    [
        (0, 100, 100.0),
        (10, 150, 165.0),
        (200, 50, 150.0),
        (-50, 200, 100.0),
        (33.3, 300, 399.9),
    ],
    ids=[
        "zero_boost",
        "ten_percent",
        "double_damage",
        "half_damage",
        "fractional_percent",
    ],
)
def test_12_1_10_parametrize(percent, base, expected):

    @module.модификатор_урона(percent)
    def атака():
        return base

    assert атака() == pytest.approx(expected, rel=1e-3)
