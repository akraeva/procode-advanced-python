import json
import os
import pytest
from src.module_14 import (
    m_14_3_1,
    m_14_3_2,
    m_14_3_3,
    m_14_3_4,
)

# для запуска pytest -k "test_14_3_" -q -x --tb=short


# === Тест для задачи 14.3.1 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            '{"status": "danger", "source": "Alpha-3", "timestamp": "2403-07-21T22:15Z"}',
            "🚨 Обнаружена угроза! Немедленно прими меры!",
        ),
        (
            '{"status": "ok", "source": "Beta-9", "timestamp": "2403-07-21T22:18Z"}',
            "✅ Передача безопасна. Продолжай наблюдение.",
        ),
        (
            '{"status": "unknown", "signal": "weak"}',
            "✅ Передача безопасна. Продолжай наблюдение.",
        ),
        (
            '{"status": "danger", "source": "Orion-5", "priority": "high"}',
            "🚨 Обнаружена угроза! Немедленно прими меры!",
        ),
        (
            '{"status": "ok", "source": "Nova-1", "timestamp": "2403-12-01T08:00Z"}',
            "✅ Передача безопасна. Продолжай наблюдение.",
        ),
        (
            '{"status": "standby", "module": "Scanner-7", "battery": "80%"}',
            "✅ Передача безопасна. Продолжай наблюдение.",
        ),
    ],
)
def test_14_3_1(data, expected):
    assert m_14_3_1(data) == expected


# === Тест для задачи 14.3.2 ===


@pytest.mark.parametrize(
    "data, expected_output",
    [
        (
            '{"жизнеобеспечение": 2, "панели": 5, "инструменты": 3}',
            "Модуль: жизнеобеспечение, количество: 2\n"
            "Модуль: панели, количество: 5\n"
            "Модуль: инструменты, количество: 3\n"
            "Всего модулей: 10",
        ),
        (
            '{"топливо": 4, "датчики": 1}',
            "Модуль: топливо, количество: 4\n"
            "Модуль: датчики, количество: 1\n"
            "Всего модулей: 5",
        ),
        (
            '{"защита": 1, "питание": 2, "связь": 2}',
            "Модуль: защита, количество: 1\n"
            "Модуль: питание, количество: 2\n"
            "Модуль: связь, количество: 2\n"
            "Всего модулей: 5",
        ),
        (
            '{"кабели": 10, "панели": 10, "мониторы": 5}',
            "Модуль: кабели, количество: 10\n"
            "Модуль: панели, количество: 10\n"
            "Модуль: мониторы, количество: 5\n"
            "Всего модулей: 25",
        ),
        (
            '{"ресиверы": 7}',
            "Модуль: ресиверы, количество: 7\n" "Всего модулей: 7",
        ),
        (
            '{"зарядные станции": 3, "системы охлаждения": 2}',
            "Модуль: зарядные станции, количество: 3\n"
            "Модуль: системы охлаждения, количество: 2\n"
            "Всего модулей: 5",
        ),
        (
            '{"кислород": 3, "инструменты": 4, "анализаторы": 2}',
            "Модуль: кислород, количество: 3\n"
            "Модуль: инструменты, количество: 4\n"
            "Модуль: анализаторы, количество: 2\n"
            "Всего модулей: 9",
        ),
    ],
)
def test_14_3_2(data, expected_output):
    assert m_14_3_2(data) == expected_output


# === Тест для задачи 14.3.3 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            "Orion-7\nTrue\nsoil, ice, microorganisms\n124\n",
            {
                "mission": "Orion-7",
                "success": True,
                "samples": ["soil", "ice", "microorganisms"],
                "duration": 124,
            },
        ),
        (
            "Luna-3\nTrue\nrock, dust\n77\n",
            {
                "mission": "Luna-3",
                "success": True,
                "samples": ["rock", "dust"],
                "duration": 77,
            },
        ),
        (
            "Mars-X\nFalse\nsand, gas\n310\n",
            {
                "mission": "Mars-X",
                "success": False,
                "samples": ["sand", "gas"],
                "duration": 310,
            },
        ),
    ],
)
def test_14_3_3(tmp_path, data, expected, monkeypatch):
    os.chdir(tmp_path)
    output = m_14_3_3(data)
    parsed_output = json.loads(output)
    assert parsed_output == expected

    report_path = tmp_path / "report.json"
    assert report_path.exists(), "Файл report.json не был создан"
    with open(report_path, encoding="utf-8") as f:
        file_data = json.load(f)
    assert file_data == expected


# === Тест для задачи 14.3.4 ===


@pytest.mark.parametrize(
    "data, expected_summary, expected",
    [
        (
            '{"id": "XZ-91", "mass": 4.7, "radioactive": true, "components": ["crystal", "metal", "unknown"]}',
            "Артефакт XZ-91 содержит 3 компонента(ов).",
            {
                "id": "XZ-91",
                "mass": 4.7,
                "radioactive": True,
                "components": ["crystal", "metal", "unknown"],
            },
        ),
        (
            '{"id": "AL-23", "mass": 12.5, "radioactive": false, "components": ["carbon", "silicon"]}',
            "Артефакт AL-23 содержит 2 компонента(ов).",
            {
                "id": "AL-23",
                "mass": 12.5,
                "radioactive": False,
                "components": ["carbon", "silicon"],
            },
        ),
        (
            '{"id": "BT-00", "mass": 0.9, "radioactive": false, "components": []}',
            "Артефакт BT-00 содержит 0 компонента(ов).",
            {
                "id": "BT-00",
                "mass": 0.9,
                "radioactive": False,
                "components": [],
            },
        ),
    ],
)
def test_14_3_4(tmp_path, data, expected_summary, expected):
    os.chdir(tmp_path)
    lines = m_14_3_4(data).strip().split("\n", 1)
    assert lines[0] == expected_summary
    assert json.loads(lines[1]) == expected

    file_path = tmp_path / "artifact.json"
    assert file_path.exists(), "Файл artifact.json не создан"
    with open(file_path, encoding="utf-8") as file:
        saved = json.load(file)
    assert saved == expected
