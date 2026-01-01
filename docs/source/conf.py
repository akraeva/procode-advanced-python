project = "ProCode Advanced Python"
copyright = "2025, nia"
author = "Anna"
release = "1.0"

# Путь к модулям
import os
import sys

sys.path.insert(0, os.path.abspath("../../"))  # ← От docs/source/ к корню проекта

# расширения
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",  # ← docstring в Google/NumPy стиле
    "sphinx.ext.autosummary",  # ← Автосаммари функций
    "sphinx_copybutton",  # ← Кнопка копирования кода
]

templates_path = ["_templates"]
exclude_patterns = []
html_theme = "alabaster"

# НАСТРОЙКИ НАВИГАЦИИ
html_theme_options = {
    # Боковая навигация
    "sidebar_width": "300px",
}

# статические файлы (CSS, эмодзи)
html_static_path = ["_static"]

# AUTODOC
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",  # ← По порядку в файле
    "add_module_names": False,  # ← Без src.module_2.
    "undoc-members": True,  # ← Функции без docstring
    "show-inheritance": True,  # ← Наследование
    "ignore-module-all": True,
}

# Русский язык
language = "ru"
locale_dirs = ["locale/"]
gettext_compact = False
html_search_language = "ru"
html_search_options = {
    "type": "default",
}

# GitHub риббон + контекст
html_context = {
    "display_github": True,  # ← GitHub уголок
    "github_user": "akraeva",
    "github_repo": "procode-advanced-python",
    "github_version": "main",
    "conf_py_path": "/docs/source/",  # ← От корня репо
}

# HTML оптимизация
html_title = "PROкод: продвинутый Python"
html_js_files = ["custom.js"]  # ← Кастом JS

# Автодоксы для больших модулей
autosummary_generate = True
autodoc_preserve_defaults = True
