import pytest
from src.module_9 import (
    m_9_2_1,
    m_9_2_2,
    m_9_2_3,
    m_9_2_4,
    m_9_2_5,
)


# === Тест для задачи 9.2.1 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            "Андрей\nЕкатерина\nИрина\nДмитрий\nЕкатерина\nАндрей",
            4,
        ),
        (
            "Александр\nНаташа\nНикита\nКатя\nРодион\nПолина\nТимур\nМаша",
            8,
        ),
        (
            "Иван\nИван\nИван",
            1,
        ),
        (
            "Оля\nВася\nПетя\nОля\nПетя",
            3,
        ),
    ],
    ids=[
        "Sample_1 (with duplicates)",
        "Sample_2 (all unique)",
        "Only one name repeated",
        "Mixed duplicates",
    ],
)
def test_9_2_1(data, expected):
    assert m_9_2_1(data) == expected


# === Тест для задачи 9.2.2 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            "еда; вода; лекарства; оружие; инструменты",
            "Общее количество уникальных ресурсов: 5\n"
            "Самый ценный ресурс: инструменты\n"
            "Самый редкий ресурс: еда\n"
            "Суммарная ценность ресурсов: 33\n"
            "Ресурсы в отсортированном порядке: еда, вода, оружие, лекарства, инструменты",
        ),
        (
            "топливо; вода; медикаменты; инструменты; топливо",
            "Общее количество уникальных ресурсов: 4\n"
            "Самый ценный ресурс: инструменты\n"
            "Самый редкий ресурс: вода\n"
            "Суммарная ценность ресурсов: 33\n"
            "Ресурсы в отсортированном порядке: вода, топливо, инструменты, медикаменты",
        ),
        (
            "еда; дрова; соль; кислород; питьевая_вода; еда; дрова; бетон",
            "Общее количество уникальных ресурсов: 6\n"
            "Самый ценный ресурс: питьевая_вода\n"
            "Самый редкий ресурс: еда\n"
            "Суммарная ценность ресурсов: 38\n"
            "Ресурсы в отсортированном порядке: еда, соль, бетон, дрова, кислород, питьевая_вода",
        ),
        (
            "металл; вода; пищевые_продукты; инструменты; первоначальная_помощь",
            "Общее количество уникальных ресурсов: 5\n"
            "Самый ценный ресурс: первоначальная_помощь\n"
            "Самый редкий ресурс: вода\n"
            "Суммарная ценность ресурсов: 58\n"
            "Ресурсы в отсортированном порядке: вода, металл, инструменты, пищевые_продукты, первоначальная_помощь",
        ),
    ],
    ids=[
        "Sample_1 (basic resources)",
        "Sample_2 (duplicate resource)",
        "Sample_3 (many resources with repeats)",
        "Sample_4 (longer names, higher value)",
    ],
)
def test_9_2_2(data, expected):
    assert m_9_2_2(data) == expected


# === Тест для задачи 9.2.3 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            "Mission 7 to X4-4Z complete in 20 days.",
            "0 2 4 7",
        ),
        (
            "Exploration complete!",
            "Цифр нет",
        ),
        (
            "No numbers here!",
            "Цифр нет",
        ),
        (
            "The 5th mission took 3 days and 4 hours.",
            "3 4 5",
        ),
        (
            "Rocket launch in 2023, expected at 8:00 AM.",
            "0 2 3 8",
        ),
    ],
    ids=[
        "Sample_1 (digits mixed with text)",
        "Sample_2 (no digits, text only)",
        "Test_№2 (explicit no numbers)",
        "Test_№3 (digits scattered in text)",
        "Sample_3 (year and time digits)",
    ],
)
def test_9_2_3(data, expected):
    assert m_9_2_3(data) == expected


# === Тест для задачи 9.2.4 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            "Afuro: интервью прошло отлично!\n"
            "Dark Horse: я немного переживала.\n"
            "Василий Фоминых: спасибо за возможность.\n"
            "Михаил Орловский: было интересно.\n"
            "Василий Фоминых: хочу присоединиться к команде.\n",
            4,
        ),
        (
            "Sophie Clark: какие-то вопросы по теме.\n"
            "John Doe: интересно узнать больше.\n"
            "Sophie Clark: надеюсь, все получится.\n"
            "John Doe: рад был участвовать.\n",
            2,
        ),
        (
            "David Miller: спасибо за подробное объяснение!\n"
            "Sophie Clark: все было очень понятно!\n"
            "David Miller: хотелось бы больше примеров.\n"
            "Tom Smith: отличная информация!\n",
            3,
        ),
        (
            "Sarah Davis: интервью было полезным.\n"
            "Michael Green: надеюсь на продолжение.\n"
            "Sarah Davis: хочу узнать больше!\n"
            "Michael Green: спасибо за возможность.\n",
            2,
        ),
        (
            "Alex Brown: интервью прошло отлично!\n"
            "Lily Green: много полезной информации.\n"
            "Alex Brown: интересно, как это устроено.\n"
            "TomW hite: хотелось бы узнать больше.\n"
            "Lily Green: надеюсь, что это поможет.\n"
            "Тонни: именно так.\n",
            4,
        ),
    ],
    ids=[
        "Sample_1 (4 unique participants)",
        "Sample_2 (2 unique participants)",
        "Test_3 (3 unique participants)",
        "Test_4 (2 unique participants, repeated)",
        "Sample_3 (4 unique participants, mix of names)",
    ],
)
def test_9_2_4(data, expected):
    assert m_9_2_4(data) == expected


# === Тест для задачи 9.2.5 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        ("ACGTOACGT", "YES"),
        ("AGGOTH", "NO"),
        ("ACGTYUI", "YES"),
        ("IUNMJHESDFO", "NO"),
        ("AJCYGTBN", "YES"),
        ("ACGT", "YES"),
        ("ACG", "NO"),
        ("AAAA", "NO"),
        ("ACGG", "NO"),
        ("OIUYACGT", "YES"),
        ("GTCAYUI", "YES"),
    ],
    ids=[
        "Sample_1 contains ACGT twice",
        "Sample_2 no sequence",
        "Test_3 contains ACGT at start",
        "Test_4 no ACGT",
        "Test_5 scattered but valid",
        "Test_6 exactly ACGT",
        "Test_7 missing T",
        "Test_8 only A's",
        "Test_9 last letter mismatch",
        "Test_10 sequence at end",
        "Test_11 sequence with noise",
    ],
)
def test_9_2_5(data, expected):
    assert m_9_2_5(data) == expected
