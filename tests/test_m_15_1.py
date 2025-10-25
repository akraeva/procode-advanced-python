import pytest
from src.module_15 import (
    m_15_1_1,
    m_15_1_2,
    m_15_1_3,
    m_15_1_4,
    m_15_1_5,
    m_15_1_6,
    m_15_1_7,
    m_15_1_8,
    m_15_1_9,
    m_15_1_10,
)

# для запуска pytest -k "test_15_1_" -q --tb=short -x


# === Тест для задачи 15.1.1 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Пример ввода (из условия)
        # "Мой стиль — как буря"
        ("Мой стиль — как буря", 5),
        # Тест №2 — Drop the mic and feel the vibe
        ("Drop the mic and feel the vibe", 9),
        # Тест №3 — Я в коде живу, как в бите
        ("Я в коде живу, как в бите", 8),
        # Тест №4 — Flow so smooth, like Python groove
        ("Flow so smooth, like Python groove", 10),
        # Тест №5 — Код как искусство
        ("Код как искусство", 5),
        # Тест №6 — Rhymes in the rain
        ("Rhymes in the rain", 5),
        # Тест №7 — Сила слов — в простоте
        ("Сила слов — в простоте", 6),
        # 🧪 Sample Input — СТИЛЬ БИТ РИТМ
        ("СТИЛЬ БИТ РИТМ", 3),
    ],
    ids=[
        "storm_style",
        "english_vibe",
        "bit_life",
        "python_groove",
        "art_code",
        "rain_rhyme",
        "simplicity_power",
        "sample_input",
    ],
)
def test_15_1_1(data, expected):
    assert m_15_1_1(data) == expected


# === Тест для задачи 15.1.2 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Пример ввода
        # улица,стиль,бит,жизнь
        ("улица,стиль,бит,жизнь", "бит\nжизнь\nстиль\nулица"),
        # Тест №2 — flow,energy,skill,beat
        ("flow,energy,skill,beat", "beat\nenergy\nflow\nskill"),
        # Тест №3 — улица,боль,вера,ритм
        ("улица,боль,вера,ритм", "боль\nвера\nритм\nулица"),
        # Тест №4 — фристайл,панч,код,строка
        ("фристайл,панч,код,строка", "код\nпанч\nстрока\nфристайл"),
        # Тест №5 — Flow,бит,STREET,ритм,STYLE,улица,Code,стиль,Beat,ЗВУК,Mic,Гармония
        (
            "Flow,бит,STREET,ритм,STYLE,улица,Code,стиль,Beat," "ЗВУК,Mic,Гармония",
            "Beat\nCode\nFlow\nMic\nSTREET\nSTYLE\nГармония\nЗВУК\nбит\nритм\nстиль\nулица",
        ),
    ],
    ids=[
        "simple_russian_sort",
        "english_sort",
        "russian_words_mixed",
        "short_russian_set",
        "mixed_case_multilang",
    ],
)
def test_15_1_2(data, expected):
    assert m_15_1_2(data) == expected


# === Тест для задачи 15.1.3 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Пример ввода
        # бит бит стиль стиль стиль бит
        ("бит бит стиль стиль стиль бит", {"бит": 3, "стиль": 3}),
        # Тест №2 — дублирует пример
        ("бит бит стиль стиль стиль бит", {"бит": 3, "стиль": 3}),
        # Тест №3 — улица стиль бит стиль улица улица
        ("улица стиль бит стиль улица улица", {"улица": 3, "стиль": 2, "бит": 1}),
        # Тест №4 — Code beats code beats Beats
        ("Code beats code beats Beats", {"Code": 1, "beats": 2, "code": 1, "Beats": 1}),
        # Тест №5 — flow Flow FLOW beat BEAT
        (
            "flow Flow FLOW beat BEAT",
            {"flow": 1, "Flow": 1, "FLOW": 1, "beat": 1, "BEAT": 1},
        ),
        # Тест №6 — длинный набор слов
        (
            "бит бит стиль Bit стиль бит Flow стиль flow BEAT Beat стиль "
            "rhyme стиль flow бит стиль beat флоу флоу Флоу beat стиль code "
            "стиль стиль стиль микрофон микрофон flow rhyme бит",
            {
                "бит": 5,
                "стиль": 10,
                "Bit": 1,
                "Flow": 1,
                "flow": 3,
                "BEAT": 1,
                "Beat": 1,
                "rhyme": 2,
                "beat": 2,
                "флоу": 2,
                "Флоу": 1,
                "code": 1,
                "микрофон": 2,
            },
        ),
        # Sample Input — я есть стиль я есть бит
        ("я есть стиль я есть бит", {"я": 2, "есть": 2, "стиль": 1, "бит": 1}),
    ],
    ids=[
        "simple_case",
        "duplicate_case",
        "russian_mix",
        "english_case_sensitive",
        "case_variations",
        "long_mixed_text",
        "sample_input",
    ],
)
def test_15_1_3(data, expected):
    assert m_15_1_3(data) == expected


# === Тест для задачи 15.1.4 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Пример ввода
        # Москва,Питер,Казань,Уфа
        (
            "Москва,Питер,Казань,Уфа",
            "('Москва', 'Питер', 'Казань', 'Уфа')\nПоследний город тура: Уфа",
        ),
        # Тест №2 — Токио,Сеул,Пекин,Шанхай,Бангкок
        (
            "Токио,Сеул,Пекин,Шанхай,Бангкок",
            "('Токио', 'Сеул', 'Пекин', 'Шанхай', 'Бангкок')\nПоследний город тура: Бангкок",
        ),
        # Тест №3 — Берлин,Прага,Вена,Будапешт
        (
            "Берлин,Прага,Вена,Будапешт",
            "('Берлин', 'Прага', 'Вена', 'Будапешт')\nПоследний город тура: Будапешт",
        ),
        # Тест №4 — Rio,San Paulo,Buenos Aires,Lima
        (
            "Rio,San Paulo,Buenos Aires,Lima",
            "('Rio', 'San Paulo', 'Buenos Aires', 'Lima')\nПоследний город тура: Lima",
        ),
        # Тест №5 — Москва,Питер,Казань,Уфа (повтор примера)
        (
            "Москва,Питер,Казань,Уфа",
            "('Москва', 'Питер', 'Казань', 'Уфа')\nПоследний город тура: Уфа",
        ),
        # Sample Input — New York,Chicago,Los Angeles,Houston
        (
            "New York,Chicago,Los Angeles,Houston",
            "('New York', 'Chicago', 'Los Angeles', 'Houston')\nПоследний город тура: Houston",
        ),
    ],
    ids=[
        "russian_example",
        "asian_cities",
        "european_cities",
        "south_america",
        "duplicate_case",
        "sample_input",
    ],
)
def test_15_1_4(data, expected):
    assert m_15_1_4(data) == expected


# === Тест для задачи 15.1.5 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Пример ввода
        # бит стиль ритм
        # ритм стиль слова
        ("бит стиль ритм\nритм стиль слова", ["ритм", "стиль"]),
        # Тест №2 — тот же пример
        ("бит стиль ритм\nритм стиль слова", ["ритм", "стиль"]),
        # Тест №3 — бит микрофон стиль рифма / звук сцена свет бит стиль
        ("бит микрофон стиль рифма\nзвук сцена свет бит стиль", ["бит", "стиль"]),
        # Тест №4 — code beat flow / drop rhyme vibe
        ("code beat flow\ndrop rhyme vibe", []),
        # Тест №5 — Beat Flow Vibe / flow beat vibe
        ("Beat Flow Vibe\nflow beat vibe", []),
        # Тест №6 — длинный миксованный пример
        (
            "бит стиль ритм энергия сила улица флоу микрофон код rhyme beat "
            "Flow rhythm code style звук line мощь идея Python логика\n"
            "Rhyme beat voice code стиль бит мощь Focus энергия Vibe флоу "
            "mic logic свет улица sound слово логика бит style rhythm",
            [
                "beat",
                "code",
                "rhythm",
                "style",
                "бит",
                "логика",
                "мощь",
                "стиль",
                "улица",
                "флоу",
                "энергия",
            ],
        ),
        # Sample Input — flow code rhyme skill / beat flow rhyme art
        ("flow code rhyme skill\nbeat flow rhyme art", ["flow", "rhyme"]),
    ],
    ids=[
        "example_case",
        "duplicate_example",
        "russian_basic",
        "no_common_words",
        "case_sensitive_diff",
        "mixed_long_case",
        "sample_input",
    ],
)
def test_15_1_5(data, expected):
    assert m_15_1_5(data) == expected


# === Тест для задачи 15.1.6 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Пример ввода
        # 2
        # Алиса BeatDrop
        # Марк StyleZone
        (
            "2\nАлиса BeatDrop\nМарк StyleZone",
            {"Алиса": "BeatDrop", "Марк": "StyleZone"},
        ),
        # Тест №2 — flowmaster Byte Legacy / bitqueen Heart of Code
        (
            "2\nflowmaster Byte Legacy\nbitqueen Heart of Code",
            {"flowmaster": "Byte Legacy", "bitqueen": "Heart of Code"},
        ),
        # Тест №3 — один участник
        ("1\nМаксим Python Hero", {"Максим": "Python Hero"}),
        # Тест №4 — три участника
        (
            "3\nКира Rhyme Flow\nИлья Bit Line\nВаня Code Style",
            {"Кира": "Rhyme Flow", "Илья": "Bit Line", "Ваня": "Code Style"},
        ),
        # Тест №5 — десять участников
        (
            "10\nАня BeatMaker\nБоб Code Flow\nКатя Rhyme Zone\nМарк Bit Hero\n"
            "Света Стиль улиц\nИгорь FlowMachine\nЛена Улица знаний\n"
            "Оля Bass Drop\nВадим Микро и Фон\nЖеня Пульс кода",
            {
                "Аня": "BeatMaker",
                "Боб": "Code Flow",
                "Катя": "Rhyme Zone",
                "Марк": "Bit Hero",
                "Света": "Стиль улиц",
                "Игорь": "FlowMachine",
                "Лена": "Улица знаний",
                "Оля": "Bass Drop",
                "Вадим": "Микро и Фон",
                "Женя": "Пульс кода",
            },
        ),
        # Sample Input — 4 участника
        (
            "4\nСоня Вечный стиль\nТимур Улицы говорят\nОлег Микрофон\n"
            "Яна Ритм моего кода",
            {
                "Соня": "Вечный стиль",
                "Тимур": "Улицы говорят",
                "Олег": "Микрофон",
                "Яна": "Ритм моего кода",
            },
        ),
    ],
    ids=[
        "example_case",
        "english_case",
        "single_entry",
        "three_entries",
        "ten_entries",
        "sample_input",
    ],
)
def test_15_1_6(data, expected):
    assert m_15_1_6(data) == expected


# === Тест для задачи 15.1.7 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Пример ввода
        (
            ["Бит качает толпу", "Слова как пули в ритме", "Тишина"],
            "Слова как пули в ритме",
        ),
        # Тест №2
        (
            ["Code is art", "Beat drops heavy", "Flow like logic"],
            "Code is art",
        ),
        # Тест №3
        (
            ["Это бит", "Это стиль", "Это мощь в каждом слове"],
            "Это мощь в каждом слове",
        ),
        # Тест №4
        (
            ["Слова", "Звук", "Ритм и движение вместе с сердцем"],
            "Ритм и движение вместе с сердцем",
        ),
        # Тест №5
        (
            ["Мир", "Код как искусство", "Сила строки"],
            "Код как искусство",
        ),
        # Тест №6
        (
            [
                "Бит движется сквозь улицы",
                "Звук пробивает стены битом",
                "Код как поэзия",
            ],
            "Бит движется сквозь улицы",
        ),
        # Тест №7 — длинный пример
        (
            [
                "Бит качает мой мир",
                "Стиль в сердце моем живет",
                "Ритм как пульс улиц",
                "Микрофон – мой лучший друг",
                "Слова летят сквозь шум",
                "Музыка в каждом движении",
                "Энергия строит каждый куплет",
                "Код как поэзия движется мягко",
                "Я создаю строки как бит",
                "Линии связаны логикой глубже",
            ],
            "Стиль в сердце моем живет",
        ),
        # Sample Input
        (
            ["Я рэп читаю", "Микрофон в руке", "Стиль и бит мой"],
            "Стиль и бит мой",
        ),
    ],
    ids=[
        "example_case",
        "english_case",
        "russian_case_1",
        "russian_case_2",
        "russian_case_3",
        "russian_case_4",
        "long_case",
        "sample_input",
    ],
)
def test_15_1_7(data, expected):
    assert m_15_1_7(data) == expected


# === Тест для задачи 15.1.8 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Пример ввода
        (
            "бит стиль стиль бит ритм",
            (3, ["бит", "ритм", "стиль"]),
        ),
        # Тест №2
        (
            "Code logic rhythm code style rhythm",
            (5, ["Code", "code", "logic", "rhythm", "style"]),
        ),
        # Тест №3
        (
            "Код стиль ритм стиль код стиль стиль",
            (4, ["Код", "код", "ритм", "стиль"]),
        ),
        # Тест №4
        (
            "бит стиль код стиль бит ритм микрофон флоу улица бит стиль мощь"
            " код бит ритм стиль звук слова строки музыка бит стиль",
            (
                12,
                [
                    "бит",
                    "звук",
                    "код",
                    "микрофон",
                    "мощь",
                    "музыка",
                    "ритм",
                    "слова",
                    "стиль",
                    "строки",
                    "улица",
                    "флоу",
                ],
            ),
        ),
        # Тест №5
        (
            "Beat flow Code Rhythm beat Flow rhyme rhyme CODE beat mic drop "
            "Logic Beat logic rhyme beat Vibe Mic code rhyme",
            (
                15,
                [
                    "Beat",
                    "CODE",
                    "Code",
                    "Flow",
                    "Logic",
                    "Mic",
                    "Rhythm",
                    "Vibe",
                    "beat",
                    "code",
                    "drop",
                    "flow",
                    "logic",
                    "mic",
                    "rhyme",
                ],
            ),
        ),
        # Sample Input
        (
            "flow Flow beat BEAT rhyme rhyme",
            (5, ["BEAT", "Flow", "beat", "flow", "rhyme"]),
        ),
    ],
    ids=[
        "example_case",
        "english_case",
        "russian_case_1",
        "russian_case_2",
        "english_mixed_case",
        "sample_input",
    ],
)
def test_15_1_8(data, expected):
    assert m_15_1_8(data) == expected


# === Тест для задачи 15.1.9 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Пример ввода
        (
            "4\nByteBro 100\nLilBit 85\nFlowMax 90\nLil Byte 95",
            [("ByteBro", 100), ("Lil Byte", 95), ("FlowMax", 90)],
        ),
        # Тест №2
        (
            "4\nByteBro 100\nLiliBit 85\nFlowMax 90\nLil_Byte 95",
            [("ByteBro", 100), ("Lil_Byte", 95), ("FlowMax", 90)],
        ),
        # Тест №3
        (
            "7\nFuturePast 91\nMeganTheStable 90\nPlayboiTetris 89\n"
            "ChiefKeefChain 83\nLilPickle 94\nYeNotAgain 95\nLilByte 100",
            [("LilByte", 100), ("YeNotAgain", 95), ("LilPickle", 94)],
        ),
        # Тест №4 (тот же вход, повтор)
        (
            "7\nFuturePast 91\nMeganTheStable 90\nPlayboiTetris 89\n"
            "ChiefKeefChain 83\nLilPickle 94\nYeNotAgain 95\nLilByte 100",
            [("LilByte", 100), ("YeNotAgain", 95), ("LilPickle", 94)],
        ),
        # Тест №5
        (
            "6\nSnoopCat 85\nDojaCow 89\nTylerTheCleaner 91\nIceKube 94\n"
            "NickiLasagna 87\nEminemulator 96",
            [("Eminemulator", 96), ("IceKube", 94), ("TylerTheCleaner", 91)],
        ),
        # Тест №6
        (
            "5\n21 Samosa 88\nTravis Teapot 94\nLil Bug 73\nNotorious B.I.T 99"
            "\nCardi Beep 95",
            [("Notorious B.I.T", 99), ("Cardi Beep", 95), ("Travis Teapot", 94)],
        ),
        # Sample Input
        (
            "8\nSnoopCat 85\nEminemulator 96\nIceKube 94\nNotoriousB.I.T 99\n"
            "Jay-Zebra 82\nDrakezilla 97\nLil Byte 105\nYeOldKanye 88",
            [("Lil Byte", 105), ("NotoriousB.I.T", 99), ("Drakezilla", 97)],
        ),
    ],
    ids=[
        "example_case",
        "test2",
        "test3",
        "test4",
        "test5",
        "test6",
        "sample_input",
    ],
)
def test_15_1_9(data, expected):
    assert m_15_1_9(data) == expected


# === Тест для задачи 15.1.10 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Пример работы скрытого кода
        ("бит стиль стиль бит ритм стиль", (6, 3, "стиль")),
        # Тест №2 (тот же ввод)
        ("бит стиль стиль бит ритм стиль", (6, 3, "стиль")),
        # Тест №3
        (
            "Flow как цикл бесконечно крут Если сбился raise но я найду маршрут",
            (12, 12, "Flow"),
        ),
        # Тест №4
        ("Пока ты в паузе я в deploy Bit по венам я real не boy", (14, 12, "в")),
        # Тест №5
        (
            "Моя душа в коде в строках открыта Lil Byte идёт не боится падать",
            (13, 12, "в"),
        ),
        # Тест №6
        (
            "бит бит бит стиль стиль код код код код бит стиль строка строка бит",
            (14, 4, "бит"),
        ),
        # Sample Input
        (
            "Это мой вход мой main мой старт Мои слова как byte-код остры как Dart",
            (14, 11, "мой"),
        ),
    ],
    ids=[
        "example_case",
        "test2",
        "test3",
        "test4",
        "test5",
        "test6",
        "sample_input",
    ],
)
def test_15_1_0(data, expected):
    assert m_15_1_10(data) == expected
