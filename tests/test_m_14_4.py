import os
import io
import pytest
from src.module_14 import (
    m_14_4_1,
)

# для запуска pytest -k "test_14_4_" -q -x --tb=short


# === Тест для задачи 14.4.1 ===


@pytest.mark.parametrize(
    "setup_case, expected",
    [
        # Файла нет
        (
            "missing",
            "Архивный файл не найден! Немедленно сообщи директору!\nОперация завершена.",
        ),
        # Нет доступа (PermissionError)
        (
            "no_access",
            "Нет доступа к файлу! Запроси права у отдела безопасности!\nОперация завершена.",
        ),
        # Передана папка вместо файла (IsADirectoryError)
        (
            "is_dir",
            "Ошибка: вместо файла указана папка! Проверь правильность пути!\nОперация завершена.",
        ),
        # Файл пуст
        (
            "empty",
            "Архивный файл пуст! Проверь правильность сохранения данных!\nОперация завершена.",
        ),
        # Файл содержит текст
        (
            "ok",
            "Последнее задание агента Эллиота: Исследование дома №13 на улице Вязов.\nОперация завершена.",
        ),
    ],
)
def test_14_4_1(tmp_path, setup_case, expected):
    os.chdir(tmp_path)
    file_path = tmp_path / "case_247.txt"

    if setup_case == "missing":
        pass
    elif setup_case == "no_access":
        file_path.write_text("секретные данные", encoding="utf-8")
        file_path.chmod(0o000)  # убираем все права доступа
    elif setup_case == "is_dir":
        file_path.mkdir()
    elif setup_case == "empty":
        file_path.write_text("", encoding="utf-8")
    else:
        file_path.write_text(
            "Последнее задание агента Эллиота: Исследование дома №13 на улице Вязов.",
            encoding="utf-8",
        )
    result = m_14_4_1()
    if setup_case == "no_access":
        file_path.chmod(0o666)

    assert result.strip() == expected.strip()
