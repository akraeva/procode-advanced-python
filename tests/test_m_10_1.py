import pytest
from src.module_10 import (
    m_10_1_1,
    m_10_1_2,
    m_10_1_3,
    m_10_1_4,
    m_10_1_5,
)


# === Тест для задачи 10.1.1 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Example
        (
            "Огонь Вода Ветер Огонь Молния Земля Ветер",
            "{Ветер, Вода, Земля, Молния, Огонь}",
        ),
        # Test 2
        ("Молния Тьма Свет Молния Свет Тьма", "{Молния, Свет, Тьма}"),
        # Test 3
        (
            "Воздух Огонь Вода Огонь Лёд Вода Воздух Лава",
            "{Вода, Воздух, Лава, Лёд, Огонь}",
        ),
        # Test 4
        ("Огонь Огонь Огонь Огонь", "{Огонь}"),
        # Test 5
        (
            "Огонь Вода Ветер Огонь Молния Земля Ветер",
            "{Ветер, Вода, Земля, Молния, Огонь}",
        ),
        # Sample
        ("Огонь Вода Лёд Земля Вода Огонь Песок", "{Вода, Земля, Лёд, Огонь, Песок}"),
    ],
    ids=["Example", "Test2", "Test3", "Test4", "Test5", "Sample"],
)
def test_10_1_1(data, expected):
    assert m_10_1_1(data) == expected


# === Тест для задачи 10.1.2 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Example 1
        ("Кира Л Лайт Миками Такеда\nМиками\nРем", "{Кира, Л, Лайт, Рем, Такеда}"),
        # Example 2
        (
            "Рюук Джеллас Соичиро Эл Лайт\nСоичиро\nМиса",
            "{Джеллас, Лайт, Миса, Рюук, Эл}",
        ),
        # Example 3
        ("Мело Ниар Лайт Кира\nЛайт\nРюузаки", "{Кира, Мело, Ниар, Рюузаки}"),
        # Example 4
        ("Такеда Аидзо Мидзуки Мелло\nАидзо\nЛ", "{Л, Мелло, Мидзуки, Такеда}"),
        # Example 5
        ("Кира Эл Лайт Миса\nМиса\nДжастин", "{Джастин, Кира, Лайт, Эл}"),
        # Test 6
        ("Акаши Сакура Лелуш Вито\nСакура\nИтачи", "{Акаши, Вито, Итачи, Лелуш}"),
        # Test 7
        ("Л Кира Нагато Лайт Мелло\nНагато\nМиса", "{Кира, Л, Лайт, Мелло, Миса}"),
        # Test 8
        ("Гаара Итачи Дейдара Обито\nОбито\nРюк", "{Гаара, Дейдара, Итачи, Рюк}"),
        # Sample
        ("Кира Л Лайт Миками Такеда\nМиками\nРем", "{Кира, Л, Лайт, Рем, Такеда}"),
    ],
    ids=[
        "Example1",
        "Example2",
        "Example3",
        "Example4",
        "Example5",
        "Test6",
        "Test7",
        "Test8",
        "Sample",
    ],
)
def test_10_1_2(data, expected):
    assert m_10_1_2(data) == expected


# === Тест для задачи 10.1.3 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Example 1
        (
            "Гон Курапика Киллуа Бисквит\nКурапика Хисока Иллуми",
            "Общие: {Курапика}\nЧистые охотники: {Бисквит, Гон, Киллуа}",
        ),
        # Example 2
        (
            "Леорио Гон Курапика\nГон Курапика",
            "Общие: {Гон, Курапика}\nЧистые охотники: {Леорио}",
        ),
        # Test 2
        (
            "Гон Курапика Киллуа Бисквит\nХисока Чролло",
            "Общие: {}\nЧистые охотники: {Бисквит, Гон, Киллуа, Курапика}",
        ),
        # Test 3
        (
            "Меруем Питоу Понго\nПитоу",
            "Общие: {Питоу}\nЧистые охотники: {Меруем, Понго}",
        ),
        # Test 4
        (
            "Леорио Гон Курапика\nГон Курапика",
            "Общие: {Гон, Курапика}\nЧистые охотники: {Леорио}",
        ),
        # Test 5
        (
            "Гон Курапика Киллуа Бисквит\nКурапика Хисока Иллюми",
            "Общие: {Курапика}\nЧистые охотники: {Бисквит, Гон, Киллуа}",
        ),
        # Sample
        (
            "Иллуми Хисока Увогин\nИллуми Хисока Увогин",
            "Общие: {Иллуми, Увогин, Хисока}\nЧистые охотники: {}",
        ),
    ],
    ids=["Example1", "Example2", "Test2", "Test3", "Test4", "Test5", "Sample"],
)
def test_10_1_3(data, expected):
    assert m_10_1_3(data) == expected


# === Тест для задачи 10.1.4 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Example 1
        (
            "Гоку Вегета Джирен Фриза\nГоку Джирен",
            "Все мастера входят в первое множество: True",
        ),
        # Example 2
        (
            "Гоку Вегета Джирен\nГоку Фриза",
            "Все мастера входят в первое множество: False",
        ),
        # Test 2
        (
            "Гоку Вегета Джирен\nГоку Фриза",
            "Все мастера входят в первое множество: False",
        ),
        # Test 3
        (
            "Гоку Вегета Джирен Топпо\nГоку Вегета Джирен",
            "Все мастера входят в первое множество: True",
        ),
        # Test 4
        (
            "Гохан Пикколо Транкс\nГоку Джирен",
            "Все мастера входят в первое множество: False",
        ),
        # Test 5
        (
            "Броли Чи-Чи Криллин Вегета\nКриллин Броли",
            "Все мастера входят в первое множество: True",
        ),
        # Sample
        (
            "Гоку Вегета Джирен Фриза\nГоку Джирен",
            "Все мастера входят в первое множество: True",
        ),
    ],
    ids=["Example1", "Example2", "Test2", "Test3", "Test4", "Test5", "Sample"],
)
def test_10_1_4(data, expected):
    assert m_10_1_4(data) == expected


# === Тест для задачи 10.1.5 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Example 1
        (
            "Naruto, One Piece, Death Note, Attack on Titan, Fullmetal Alchemist",
            [
                "Attack on Titan",
                "Death Note",
                "Fullmetal Alchemist",
                "Naruto",
                "One Piece",
            ],
        ),
        # Example 2
        (
            "Demon Slayer, Hunter x Hunter, Bleach, Code Geass, Steins;Gate",
            ["Bleach", "Code Geass", "Demon Slayer", "Hunter x Hunter", "Steins;Gate"],
        ),
        # Test 2
        (
            "Naruto, One Piece, Death Note, Attack on Titan, Fullmetal Alchemist",
            [
                "Attack on Titan",
                "Death Note",
                "Fullmetal Alchemist",
                "Naruto",
                "One Piece",
            ],
        ),
        # Test 3
        (
            "Demon Slayer, Hunter x Hunter, Bleach, Code Geass, Steins;Gate",
            ["Bleach", "Code Geass", "Demon Slayer", "Hunter x Hunter", "Steins;Gate"],
        ),
        # Test 4
        (
            "JoJo's Bizarre Adventure, Fairy Tail, Cowboy Bebop, Vinland Saga, Re:Zero",
            [
                "Cowboy Bebop",
                "Fairy Tail",
                "JoJo's Bizarre Adventure",
                "Re:Zero",
                "Vinland Saga",
            ],
        ),
        # Sample
        (
            "Sword Art Online, Tokyo Ghoul, Black Clover, My Hero Academia, Dragon Ball",
            [
                "Black Clover",
                "Dragon Ball",
                "My Hero Academia",
                "Sword Art Online",
                "Tokyo Ghoul",
            ],
        ),
    ],
    ids=["Example1", "Example2", "Test2", "Test3", "Test4", "Sample"],
)
def test_10_1_5(data, expected):
    assert m_10_1_5(data) == expected
