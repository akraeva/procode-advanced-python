import pytest
from src.module_8 import (
    m_8_1_1,
    m_8_1_2,
    m_8_1_3,
    m_8_1_4,
    m_8_1_5,
    m_8_1_6,
    m_8_1_7,
    m_8_1_8,
    m_8_1_9,
    m_8_1_10,
)


# === Тест для задачи 8.1.1 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            '{"001": "взлом", "002": "успешен", "003": "следующий", "004": "объект"}\n001 002 003 004',
            "взлом успешен следующий объект",
        ),
        (
            '{"001": "взлом", "002": "успешен", "003": "следующий", "004": "объект"}\n001 002 003 004',
            "взлом успешен следующий объект",
        ),
        (
            '{"X": "сервер", "Y": "работает", "Z": "стабильно"}\nX Y Z',
            "сервер работает стабильно",
        ),
        (
            '{"key1": "найден", "key2": "новый", "key3": "след"}\nkey2 key3 key1',
            "новый след найден",
        ),
        (
            '{"alpha": "это", "beta": "код", "gamma": "секретный"}\nalpha gamma beta',
            "это секретный код",
        ),
        (
            '{"A1": "доступ", "B2": "разрешен", "C3": "к", "D4": "системе"}\nA1 B2 C3 D4',
            "доступ разрешен к системе",
        ),
    ],
    ids=[
        "Sample_1",
        "Test_2",
        "Test_3",
        "Test_4",
        "Test_5",
        "Sample",
    ],
)
def test_8_1_1(data, expected):
    assert m_8_1_1(data) == expected


# === Тест для задачи 8.1.2 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            '{"192.168.1.1": false, "10.0.0.23": true, "172.16.5.4": false}',
            "Истинный адрес: 10.0.0.23",
        ),
        (
            '{"192.168.1.1": false, "10.0.0.23": true, "172.16.5.4": false}',
            "Истинный адрес: 10.0.0.23",
        ),
        (
            '{"192.168.100.1": false, "192.168.100.2": false, "192.168.100.3": true, "192.168.100.4": false}',
            "Истинный адрес: 192.168.100.3",
        ),
        (
            '{"192.168.1.10": false, "10.0.0.15": false, "172.16.5.5": true}',
            "Истинный адрес: 172.16.5.5",
        ),
        (
            '{"198.51.100.2": false, "203.0.113.5": true, "192.168.0.1": false}',
            "Истинный адрес: 203.0.113.5",
        ),
    ],
    ids=[
        "Sample_1",
        "Test_2",
        "Test_3",
        "Test_4",
        "Sample",
    ],
)
def test_8_1_2(data, expected):
    assert m_8_1_2(data) == expected


# === Тест для задачи 8.1.3 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            '{"12345": [["DarkMaster", "DarkNet"], ["CyberFox", "HackerForum"]], "67890": [["GhostX", "DeepWeb"]]} \n12345',
            "Призрак найден на 2 платформ(ах):\n- DarkNet: DarkMaster\n- HackerForum: CyberFox",
        ),
        (
            '{"333": [["Neo", "MatrixForum"]]} \n999',
            "ID не найден.",
        ),
        (
            '{"777": [["ShadowHunter", "GitHub"], ["GhostRider", "Twitter"], ["DarkPhantom", "Discord"], ["HackerX", "YouTube"]]} \n777',
            "Призрак найден на 4 платформ(ах):\n- GitHub: ShadowHunter\n- Twitter: GhostRider\n- Discord: DarkPhantom\n- YouTube: HackerX",
        ),
        (
            '{"101": [["Shadow", "ExploitDB"], ["Phantom", "BlackHatWorld"], ["Stealth", "Reddit"]]} \n101',
            "Призрак найден на 3 платформ(ах):\n- ExploitDB: Shadow\n- BlackHatWorld: Phantom\n- Reddit: Stealth",
        ),
        (
            '{"555": [["DarkSeeker", "Telegram"]]} \n555',
            "Призрак найден на 1 платформ(ах):\n- Telegram: DarkSeeker",
        ),
    ],
    ids=[
        "Sample_1 1",
        "Sample_1 2",
        "Test_4",
        "Test_5",
        "Sample",
    ],
)
def test_8_1_3(data, expected):
    assert m_8_1_3(data) == expected


# === Тест для задачи 8.1.4 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            '{"report.txt": ".txt", "virus.exe": ".exe", "script.py": ".py", "hacker.dll": ".dll"}',
            "Поддельные файлы: virus.exe, hacker.dll",
        ),
        (
            '{"notes.doc": ".doc", "passwords.txt.exe": ".exe", "malware.dll.": ".dll", "image.png": ".png"}',
            "Поддельные файлы: passwords.txt.exe, malware.dll.",
        ),
        (
            '{"data.csv": ".csv", "readme.md": ".md", "trojan.bat": ".bat", "stealth.scr.": ".scr"}',
            "Поддельные файлы: trojan.bat, stealth.scr.",
        ),
        (
            '{"document.pdf": ".pdf", "song.mp3": ".mp3", "video.mp4": ".mp4"}',
            "Поддельные файлы не найдены.",
        ),
        (
            '{"image.jpg": ".jpg", "security.doc.dll": ".dll", "backup.zip.exe": ".exe", "user.txt": ".txt"}',
            "Поддельные файлы: security.doc.dll, backup.zip.exe",
        ),
    ],
    ids=[
        "Sample_1",
        "Sample_2",
        "Sample_3",
        "Sample_4 (нет поддельных)",
        "Sample",
    ],
)
def test_8_1_4(data, expected):
    assert m_8_1_4(data) == expected


# === Тест для задачи 8.1.5 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            '{"a1b2c3": "qwerty", "d4e5f6": "password123", "g7h8i9": "letmein"}\n'
            "a1b2c3 d4e5f6 g7h8i9",
            "qwerty password123 letmein",
        ),
        (
            '{"h1e2l3l4o": "hello", "s3e4c5r6e7t": "secret"}\n' "h1e2l3l4o s3e4c5r6e7t",
            "hello secret",
        ),
        (
            '{"pass123": "mypassword", "a1b2c3": "hiddenkey"}\n' "@pass123# *a1b2c3!",
            "mypassword hiddenkey",
        ),
        (
            '{"x1y2z3": "superpass", "m4n5o6": "welcome123"}\n'
            "x1y2z3 unknown123 m4n5o6",
            "superpass Не удалось расшифровать пароль welcome123",
        ),
        (
            '{"alpha": "admin", "beta": "root", "gamma": "securepass"}\n'
            "*alpha# @beta! $gamma",
            "admin root securepass",
        ),
        (
            '{"q1w2e3": "open123", "r4t5y6": "letmein", "u7i8o9": "securepass"}\n'
            "q1w2e3 @r4t5y6! unknownPass u7i8o9",
            "open123 letmein Не удалось расшифровать пароль securepass",
        ),
        (
            '{"a1b2": "hunter2", "c3d4": "passw0rd", "e5f6": "rootaccess"}\n'
            "@a1b2 @c3d4$ *e5f6!",
            "hunter2 passw0rd rootaccess",
        ),
        (
            '{"x123": "admin", "y456": "qwerty", "z789": "superpass"}\n'
            "abc123 xyz999 helloworld",
            "Не удалось расшифровать пароль Не удалось расшифровать пароль Не удалось расшифровать пароль",
        ),
    ],
    ids=[
        "Sample_1",
        "Sample_2",
        "Sample_3 (маскировка символы)",
        "Sample_4 (неизвестный в середине)",
        "Sample_5 (удаление спецсимволов)",
        "Test_6 (unknown перед последним)",
        "Test_7 (все с маской спецсимволы)",
        "Test_8 (все неизвестные)",
    ],
)
def test_8_1_5(data, expected):
    assert m_8_1_5(data) == expected


# === Тест для задачи 8.1.6 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            '{"192.168.1.1": {"google.com": 5, "darkweb.net": 12, "forum.xyz": 7}, '
            '"10.0.0.23": {"google.com": 2, "darkweb.net": 1, "forum.xyz": 5}}',
            "Самый активный IP: 192.168.1.1\nНаиболее посещаемый сайт: darkweb.net",
        ),
        (
            "{\n"
            '  "172.16.5.4": {"youtube.com": 8, "hackerforum.com": 3},\n'
            '  "203.0.113.5": {"youtube.com": 8, "hackerforum.com": 5}\n'
            "}",
            "Самый активный IP: 203.0.113.5\nНаиболее посещаемый сайт: youtube.com",
        ),
        (
            "{\n"
            '  "10.10.10.10": {"facebook.com": 3, "twitter.com": 7, "reddit.com": 10},\n'
            '  "192.168.100.3": {"facebook.com": 2, "twitter.com": 1, "reddit.com": 12}\n'
            "}",
            "Самый активный IP: 10.10.10.10\nНаиболее посещаемый сайт: reddit.com",
        ),
        (
            "{\n"
            '  "5.5.5.5": {"siteA.com": 4, "siteB.com": 6},\n'
            '  "6.6.6.6": {"siteA.com": 4, "siteB.com": 6}\n'
            "}",
            "Самый активный IP: 5.5.5.5\nНаиболее посещаемый сайт: siteB.com",
        ),
        (
            "{\n"
            '  "8.8.8.8": {"telegram.org": 5, "discord.com": 5, "darkmarket.com": 10},\n'
            '  "7.7.7.7": {"telegram.org": 3, "discord.com": 4, "darkmarket.com": 6}\n'
            "}",
            "Самый активный IP: 8.8.8.8\nНаиболее посещаемый сайт: darkmarket.com",
        ),
        (
            "{\n"
            '  "192.168.0.1": {"example.com": 3, "testsite.com": 8},\n'
            '  "10.1.1.1": {"example.com": 6, "testsite.com": 5, "malware.net": 2},\n'
            '  "172.16.0.2": {"example.com": 10, "testsite.com": 9}\n'
            "}",
            "Самый активный IP: 172.16.0.2\nНаиболее посещаемый сайт: example.com",
        ),
        (
            "{\n"
            '  "5.5.5.5": {"forum.net": 2, "blog.io": 1, "hacker-site.com": 15},\n'
            '  "9.9.9.9": {"forum.net": 10, "blog.io": 5, "hacker-site.com": 1}\n'
            "}",
            "Самый активный IP: 5.5.5.5\nНаиболее посещаемый сайт: hacker-site.com",
        ),
        (
            "{\n"
            '  "111.222.333.444": {"siteX.com": 4, "siteY.com": 6},\n'
            '  "555.666.777.888": {"siteX.com": 4, "siteY.com": 6}\n'
            "}",
            "Самый активный IP: 111.222.333.444\nНаиболее посещаемый сайт: siteY.com",
        ),
    ],
    ids=[
        "Sample_1 1 (обычный случай)",
        "Sample_1 2 (равная активность, выбираем по IP)",
        "Sample_1 3 (много сайтов у IP)",
        "Sample_1 4 (равная сумма, берём первый IP)",
        "Sample_1 5 (хакер и любимый сайт)",
        "Test_№6 (три IP, побеждает 172.16.0.2)",
        "Test_№7 (разные профили активности)",
        "Test_№8 (равные IP активности, первый выигрывает)",
    ],
)
def test_8_1_6(data, expected):
    assert m_8_1_6(data) == expected


# === Тест для задачи 8.1.7 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            '{"A1": "H", "B2": "E", "C3": "L", "D4": "O"}\nA1 B2 C3 C3 D4',
            "HELLO",
        ),
        (
            '{"X1": "C", "Y2": "O", "Z3": "D", "W4": "E"}\nX1 Y2 Z3 W4 A5',
            "CODE?",
        ),
        (
            '{"A1": "D", "B2": "A", "C3": "T", "D4": "A"}\nA1 B2 X9 C3 D4',
            "DA?TA",
        ),
        (
            '{"A1": "S", "B2": "A", "C3": "F", "D4": "E"}\nA1 B2 X5 C3 D4',
            "SA?FE",
        ),
        (
            '{"M1": "M", "N2": "O", "O3": "O", "P4": "N"}\nM1 N2 O3 O3 P4',
            "MOOON",
        ),
        (
            '{"G1": "P", "H2": "A", "I3": "S", "J4": "S", "K5": "W", "L6": "O", "M7": "R", "N8": "D"}\nG1 H2 I3 J4 K5 L6 M7 N8',
            "PASSWORD",
        ),
        (
            '{"X1": "H", "Y2": "A", "Z3": "C", "W4": "K", "Q5": "E", "R6": "R"}\nX1 Y2 Z3 W4 A8 B9 C7 Q5 R6',
            "HACK???ER",
        ),
        (
            '{"A1": "H", "B2": "I", "C3": "!"}\nX9 Y8 Z7',
            "???",
        ),
    ],
    ids=[
        "Sample_1",
        "Test_1 — неизвестный код в конце",
        "Test_2 — неизвестный код посередине",
        "Test_3 — ещё Sample_1 с ?",
        "Test_4 — повтор символов",
        "Test_5 — длинное слово PASSWORD",
        "Test_6 — несколько неизвестных подряд",
        "Test_7 — все коды неизвестны",
    ],
)
def test_8_1_7(data, expected):
    assert m_8_1_7(data) == expected


# === Тест для задачи 8.1.8 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            '{"GhostX": "192.168.1.10", "CyberFox": "10.0.0.15", "DarkMaster": "192.168.1.10"}',
            "Настоящий хакер: GhostX, DarkMaster (IP: 192.168.1.10)",
        ),
        (
            '{"Hacker1": "10.0.0.1", "Hacker2": "10.0.0.2", "Hacker3": "10.0.0.3"}',
            "Призрак не найден",
        ),
        (
            '{"Shadow": " 123.456.789.000 ", "GhostRider": "123.456.789.000"}',
            "Настоящий хакер: Shadow, GhostRider (IP: 123.456.789.000)",
        ),
        (
            '{"Neo": "1.1.1.1", "Trinity": "", "Smith": "2.2.2.2", "Morpheus": "1.1.1.1"}',
            "Настоящий хакер: Neo, Morpheus (IP: 1.1.1.1)",
        ),
        (
            '{"Alpha": "5.5.5.5", "Beta": "6.6.6.6", "Gamma": "5.5.5.5", "Delta": "6.6.6.6"}',
            "Настоящий хакер: Alpha, Gamma (IP: 5.5.5.5)",
        ),
    ],
    ids=[
        "Sample_1",
        "Sample_2",
        "Sample_3",
        "Sample_4",
        "Sample_5",
    ],
)
def test_8_1_8(data, expected):
    assert m_8_1_8(data) == expected


# === Тест для задачи 8.1.9 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            '{"2024-03-10": "Берлин", "2024-03-08": "Москва", "2024-03-12": "Париж"}',
            "Маршрут: Москва → Берлин → Париж",
        ),
        (
            '{"2024-03-05": "Лондон", "2024-03-07": "Берлин", "2024-03-09": "Лондон", "2024-03-11": "Париж"}',
            "Маршрут: Лондон → Берлин → Париж",
        ),
        (
            '{"2024-03-15": " Нью-Йорк ", "2024-03-12": "Лос-Анджелес ", "2024-03-10": " Вашингтон"}',
            "Маршрут: Вашингтон → Лос-Анджелес → Нью-Йорк",
        ),
        (
            '{"2024-04-01": "Токио", "2024-03-28": "Сеул", "2024-04-03": "Пекин"}',
            "Маршрут: Сеул → Токио → Пекин",
        ),
        (
            '{"2024-06-01": "Рим", "2024-06-03": "Мадрид", "2024-06-05": "Рим", "2024-06-07": "Лиссабон", "2024-06-09": "Мадрид"}',
            "Маршрут: Рим → Мадрид → Лиссабон",
        ),
        (
            '{"2024-05-01": "Дубай", "2024-05-03": "Лондон", "2024-05-05": "Дубай", "2024-05-07": "Берлин", "2024-05-10": "Лондон"}',
            "Маршрут: Дубай → Лондон → Берлин",
        ),
        (
            '{"2024-09-20": "Вашингтон", "2024-09-18": "Нью-Йорк", "2024-09-25": "Лос-Анджелес", "2024-09-22": "Чикаго"}',
            "Маршрут: Нью-Йорк → Вашингтон → Чикаго → Лос-Анджелес",
        ),
        (
            '{"2024-07-14": " Бангкок", "2024-07-16": " Сингапур", "2024-07-18": "Куала-Лумпур", "2024-07-20": " Сингапур"}',
            "Маршрут: Бангкок → Сингапур → Куала-Лумпур",
        ),
    ],
    ids=[
        "Sample_1 1 — обычный порядок",
        "Sample_1 2 — убираем дубликаты",
        "Sample_1 3 — убираем пробелы",
        "Sample_1 4 — сортировка дат",
        "Sample_1 5 — повторные города",
        "Sample_1 6 — Дубай, Лондон, Берлин",
        "Sample_1 7 — Нью-Йорк → Лос-Анджелес",
        "Sample_1 8 — Бангкок → Сингапур → Куала-Лумпур",
    ],
)
def test_8_1_9(data, expected):
    assert m_8_1_9(data) == expected


# === Тест для задачи 8.1.10 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            '{"2024-03-10": "Берлин", "2024-03-08": "Москва", "2024-03-12": "Париж"}\n'
            '{"2024-03-10": "Берлин", "2024-03-08": "Рим", "2024-03-12": "Париж"}',
            "🔥 Призрак пойман в городе: Москва!",
        ),
        (
            '{"2024-04-01": "Токио", "2024-04-03": "Пекин", "2024-04-05": "Сеул"}\n'
            '{"2024-04-01": "Токио", "2024-04-03": "Пекин", "2024-04-05": "Сеул"}',
            "👻 Призрак снова скрылся...",
        ),
        (
            '{"2024-05-02": "Лондон", "2024-05-04": "Берлин", "2024-05-06": "Нью-Йорк"}\n'
            '{"2024-05-02": "Лондон", "2024-05-04": "Берлин", "2024-05-06": "Рим"}',
            "🔥 Призрак пойман в городе: Нью-Йорк!",
        ),
        (
            '{"2024-06-10": "Вашингтон", "2024-06-12": "Лос-Анджелес", "2024-06-15": "Майами"}\n'
            '{"2024-06-10": "Нью-Йорк", "2024-06-12": "Лос-Анджелес", "2024-06-15": "Майами"}',
            "🔥 Призрак пойман в городе: Вашингтон!",
        ),
        (
            '{"2024-07-01": "Париж", "2024-07-05": "Рим", "2024-07-10": "Лиссабон"}\n'
            '{"2024-07-01": "Париж", "2024-07-05": "Рим", "2024-07-10": "Барселона"}',
            "🔥 Призрак пойман в городе: Лиссабон!",
        ),
    ],
    ids=[
        "Sample_1 1 — Москва vs Рим",
        "Sample_1 2 — маршруты совпадают",
        "Sample_1 3 — Нью-Йорк vs Рим",
        "Sample_1 4 — Вашингтон vs Нью-Йорк",
        "Sample_1 5 — Лиссабон vs Барселона",
    ],
)
def test_8_1_0(data, expected):
    assert m_8_1_10(data) == expected
