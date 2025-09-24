import pytest
from src.module_7 import (
    m_7_5_1,
    m_7_5_2,
    m_7_5_3,
)


# для запуска pytest -k "test_7_5_1" -q -x --tb=short


# === Тест для задачи 7.5.1 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            "Goku\n30\nDragon Ball Z",
            "Информация о всех персонажах:\n\n"
            "Имя: Naruto\nВозраст: 17\nЛюбимое аниме: Naruto Shippuden\n\n"
            "Имя: Luffy\nВозраст: 19\nЛюбимое аниме: One Piece\n\n"
            "Имя: Goku\nВозраст: 30\nЛюбимое аниме: Dragon Ball Z",
        ),
        (
            "Mikasa\n21\nAttack on Titan  ",
            "Информация о всех персонажах:\n\n"
            "Имя: Naruto\nВозраст: 17\nЛюбимое аниме: Naruto Shippuden\n\n"
            "Имя: Luffy\nВозраст: 19\nЛюбимое аниме: One Piece\n\n"
            "Имя: Mikasa\nВозраст: 21\nЛюбимое аниме: Attack on Titan",
        ),
        (
            "Tanjiro\n16\nDemon Slayer  ",
            "Информация о всех персонажах:\n\n"
            "Имя: Naruto\nВозраст: 17\nЛюбимое аниме: Naruto Shippuden\n\n"
            "Имя: Luffy\nВозраст: 19\nЛюбимое аниме: One Piece\n\n"
            "Имя: Tanjiro\nВозраст: 16\nЛюбимое аниме: Demon Slayer",
        ),
    ],
    ids=["Sample", "Test_2", "Test_3"],
)
def test_7_5_1(data, expected):
    assert m_7_5_1(data) == expected


# === Тест для задачи 7.5.2 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            "Название: One Piece, Количество серий: 1000, Жанр: Adventure, Просмотрено: True\n"
            "Название: Naruto, Количество серий: 500, Жанр: Action, Просмотрено: False\n"
            "Название: Attack on Titan, Количество серий: 75, Жанр: Action, Просмотрено: True\n"
            "Название: Your Name, Количество серий: 1, Жанр: Romance, Просмотрено: True\n"
            "Название: Demon Slayer, Количество серий: 26, Жанр: Action, Просмотрено: False",
            "Просмотренные аниме:\n"
            "One Piece\n"
            "Attack on Titan\n"
            "Your Name\n\n"
            "Аниме, которые хотите посмотреть:\n"
            "Naruto\n"
            "Demon Slayer\n\n"
            "Аниме в жанре Action:\n"
            "Naruto\n"
            "Attack on Titan\n"
            "Demon Slayer",
        ),
        (
            "Название: My Hero Academia, Количество серий: 88, Жанр: Action, Просмотрено: True\n"
            "Название: Demon Slayer, Количество серий: 26, Жанр: Action, Просмотрено: False\n"
            "Название: Naruto, Количество серий: 500, Жанр: Adventure, Просмотрено: False\n"
            "Название: Fullmetal Alchemist, Количество серий: 64, Жанр: Adventure, Просмотрено: True\n"
            "Название: Death Note, Количество серий: 37, Жанр: Thriller, Просмотрено: True",
            "Просмотренные аниме:\n"
            "My Hero Academia\n"
            "Fullmetal Alchemist\n"
            "Death Note\n\n"
            "Аниме, которые хотите посмотреть:\n"
            "Demon Slayer\n"
            "Naruto\n\n"
            "Аниме в жанре Action:\n"
            "My Hero Academia\n"
            "Demon Slayer",
        ),
        (
            "Название: Attack on Titan, Количество серий: 75, Жанр: Action, Просмотрено: True\n"
            "Название: One Piece, Количество серий: 1000, Жанр: Adventure, Просмотрено: False\n"
            "Название: Bleach, Количество серий: 366, Жанр: Action, Просмотрено: True\n"
            "Название: Cowboy Bebop, Количество серий: 26, Жанр: Sci-Fi, Просмотрено: True\n"
            "Название: Spirited Away, Количество серий: 1, Жанр: Fantasy, Просмотрено: False",
            "Просмотренные аниме:\n"
            "Attack on Titan\n"
            "Bleach\n"
            "Cowboy Bebop\n\n"
            "Аниме, которые хотите посмотреть:\n"
            "One Piece\n"
            "Spirited Away\n\n"
            "Аниме в жанре Action:\n"
            "Attack on Titan\n"
            "Bleach",
        ),
        (
            "Название: Steins;Gate, Количество серий: 24, Жанр: Sci-Fi, Просмотрено: True\n"
            "Название: Your Name, Количество серий: 1, Жанр: Romance, Просмотрено: True\n"
            "Название: Sword Art Online, Количество серий: 25, Жанр: Action, Просмотрено: False\n"
            "Название: The Promised Neverland, Количество серий: 12, Жанр: Thriller, Просмотрено: True\n"
            "Название: Dragon Ball Z, Количество серий: 291, Жанр: Action, Просмотрено: False",
            "Просмотренные аниме:\n"
            "Steins;Gate\n"
            "Your Name\n"
            "The Promised Neverland\n\n"
            "Аниме, которые хотите посмотреть:\n"
            "Sword Art Online\n"
            "Dragon Ball Z\n\n"
            "Аниме в жанре Action:\n"
            "Sword Art Online\n"
            "Dragon Ball Z",
        ),
    ],
    ids=["Sample", "Test_2", "Test_3", "Test_4"],
)
def test_7_5_2(data, expected):
    assert m_7_5_2(data) == expected


# === Тест для задачи 7.5.3 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            "Vova\n2",
            "Такого участника нет в клубе\n"
            "Результаты фильтрации по цифре '2':\n"
            "Olga: 222-333-4444",
        ),
        (
            "Sofia\n5",
            "Телефон: 666-777-8888\n"
            "Адрес: 1230 Maple Ave\n"
            "Результаты фильтрации по цифре '5':\n"
            "Alex: 555-789-4567\n"
            "Dmitry: 555-666-7777",
        ),
        (
            "Nina\n8",
            "Телефон: 333-444-5555\n"
            "Адрес: 6789 Cedar Dr\n"
            "Нет контактов, начинающихся с цифры '8'",
        ),
        (
            "Olga\n7",
            "Телефон: 222-333-4444\n"
            "Адрес: 7890 Birch Blvd\n"
            "Результаты фильтрации по цифре '7':\n"
            "Anton: 777-888-9999",
        ),
    ],
    ids=["Sample", "Test_2", "Test_3", "Test_4"],
)
def test_7_5_3(data, expected):
    assert m_7_5_3(data) == expected
