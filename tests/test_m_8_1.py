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
