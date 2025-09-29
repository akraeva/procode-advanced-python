import pytest
from src.module_9 import (
    m_9_3_1,
    m_9_3_2,
    m_9_3_3,
    m_9_3_4,
)


# === Тест для задачи 9.3.1 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            "3\n1 2 3 4\n3 4 5 6\n1 7 8",
            8,
        ),
        (
            "2\n1 3 5 6 7 8 9\n1 2 3",
            8,
        ),
        (
            "3\n1 2 3\n1 2 3\n1 2 3",
            3,
        ),
        (
            "1\n1 3 5 5 5",
            3,
        ),
        (
            "2\n12 34 56\n12 45 67 89",
            6,
        ),
        (
            "5\n1 7 9 0 8 7 6\n1 3 5 6 7\n9 0 7 4 3\n1 2\n1 3",
            10,
        ),
    ],
    ids=[
        "Example_1 (three sets, some overlap)",
        "Test_2 (two sets, partial overlap)",
        "Test_3 (all identical sets)",
        "Test_4 (duplicates inside one set)",
        "Test_5 (different sets with overlap)",
        "Sample (five sets, more complex union)",
    ],
)
def test_9_3_1(data, expected):
    assert m_9_3_1(data) == expected


# === Тест для задачи 9.3.2 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            "6 7 8 9\n3\n7",
            "После добавления участников: {1, 2, 3, 4, 5, 6, 7, 8, 9}\n"
            "После удаления участника с номером 3: {1, 2, 4, 5, 6, 7, 8, 9}\n"
            "После удаления участника с номером 7 (метод discard): {1, 2, 4, 5, 6, 8, 9}\n"
            "Удалён случайный участник с номером 1.\n"
            "Оставшиеся участники: {2, 4, 5, 6, 8, 9}\n"
            "После очистки списка участников: set()",
        ),
        (
            "1 2 3 4\n2\n1",
            "После добавления участников: {1, 2, 3, 4, 5}\n"
            "После удаления участника с номером 2: {1, 3, 4, 5}\n"
            "После удаления участника с номером 1 (метод discard): {3, 4, 5}\n"
            "Удалён случайный участник с номером 3.\n"
            "Оставшиеся участники: {4, 5}\n"
            "После очистки списка участников: set()",
        ),
        (
            "9 8 7 6\n7\n1",
            "После добавления участников: {1, 2, 3, 4, 5, 6, 7, 8, 9}\n"
            "После удаления участника с номером 7: {1, 2, 3, 4, 5, 6, 8, 9}\n"
            "После удаления участника с номером 1 (метод discard): {2, 3, 4, 5, 6, 8, 9}\n"
            "Удалён случайный участник с номером 2.\n"
            "Оставшиеся участники: {3, 4, 5, 6, 8, 9}\n"
            "После очистки списка участников: set()",
        ),
        (
            "4 5 6 7 10 11 13\n1\n1",
            "После добавления участников: {1, 2, 3, 4, 5, 6, 7, 10, 11, 13}\n"
            "После удаления участника с номером 1: {2, 3, 4, 5, 6, 7, 10, 11, 13}\n"
            "После удаления участника с номером 1 (метод discard): {2, 3, 4, 5, 6, 7, 10, 11, 13}\n"
            "Удалён случайный участник с номером 2.\n"
            "Оставшиеся участники: {3, 4, 5, 6, 7, 10, 11, 13}\n"
            "После очистки списка участников: set()",
        ),
        (
            "11 12 13 14\n13\n4",
            "После добавления участников: {1, 2, 3, 4, 5, 11, 12, 13, 14}\n"
            "После удаления участника с номером 13: {1, 2, 3, 4, 5, 11, 12, 14}\n"
            "После удаления участника с номером 4 (метод discard): {1, 2, 3, 5, 11, 12, 14}\n"
            "Удалён случайный участник с номером 1.\n"
            "Оставшиеся участники: {2, 3, 5, 11, 12, 14}\n"
            "После очистки списка участников: set()",
        ),
    ],
    ids=[
        "Example_1 (basic case)",
        "Test_2 (removal with discard and random)",
        "Test_3 (initial set with reverse order)",
        "Test_4 (bigger set with 10, 11, 13)",
        "Sample (with 11,12,13,14 input)",
    ],
)
def test_9_3_2(data, expected):
    assert m_9_3_2(data) == expected


# === Тест для задачи 9.3.3 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            "5\nadd AB1234\nadd CD5678\nremove AB1234\ndiscard EF9999\npop",
            "Множество пустое",
        ),
        (
            "4\nadd M500KM\nadd M500KM\nremove M500KM\nadd N700TT",
            "N700TT",
        ),
        (
            "6\nadd A123BC\nadd B456DE\nremove A123BC\nadd C789FG\npop\nclear",
            "Множество пустое",
        ),
        (
            "5\nadd AA111AA\nadd BB222BB\nadd CC333CC\ndiscard BB222BB\nremove AA111AA",
            "CC333CC",
        ),
        (
            "6\nadd Z999ZZ\nadd Y888YY\nadd X777XX\nadd FF888OP\nremove X777XX\nclear",
            "Множество пустое",
        ),
        (
            "5\nadd AB1234\nadd CD5678\nremove AB1234\ndiscard EF9999\npop",
            "Множество пустое",
        ),
        (
            "5\nadd X777XX\nadd Y888YY\nadd W666WW\nremove W666WW\ndiscard X777XX",
            "Y888YY",
        ),
        (
            "5\nadd X100YZ\nadd A555AA\ndiscard X100YZ\nadd B777BB\nadd C999CC",
            "A555AA B777BB C999CC",
        ),
    ],
    ids=[
        "Example_1 (basic add/remove/discard/pop)",
        "Test_2 (duplicate add and remove)",
        "Test_3 (pop and clear leads to empty)",
        "Test_4 (multiple adds, remove and discard)",
        "Test_5 (clear wipes set)",
        "Test_6 (same as Example_1, repeated)",
        "Test_7 (remove + discard leaves one element)",
        "Sample (mix of add/discard/add)",
    ],
)
def test_9_3_3(data, expected):
    assert m_9_3_3(data) == expected


# === Тест для задачи 9.3.4 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            "7\nremove apple\npop\ndiscard avocado\nadd apricot\npop\n"
            "add coconut\nclear",
            "Фруктовый сад пуст",
        ),
        (
            "6\nadd durian\nadd persimmon\npop\ndiscard plum\n" "discard cherry\nclear",
            "Фруктовый сад пуст",
        ),
        (
            "3\nadd mango\nadd fig\nadd date",
            "apple banana blueberry cherry date fig grape grapefruit kiwi "
            "lemon lime mango melon orange papaya peach pear pineapple plum "
            "raspberry strawberry watermelon",
        ),
        (
            "4\nremove apple\nremove banana\nremove grape\nremove pear",
            "blueberry cherry grapefruit kiwi lemon lime mango melon orange "
            "papaya peach pineapple plum raspberry strawberry watermelon",
        ),
        (
            "5\ndiscard lemon\ndiscard cherry\ndiscard orange\ndiscard plum\n"
            "discard lime",
            "apple banana blueberry grape grapefruit kiwi mango melon papaya "
            "peach pear pineapple raspberry strawberry watermelon",
        ),
        (
            "3\npop\npop\nclear",
            "Фруктовый сад пуст",
        ),
        (
            "4\nadd coconut\nadd fig\nremove lemon\ndiscard banana",
            "apple blueberry cherry coconut fig grape grapefruit kiwi lime "
            "mango melon orange papaya peach pear pineapple plum raspberry "
            "strawberry watermelon",
        ),
    ],
    ids=[
        "Example_1 (remove, pop, add, clear = empty)",
        "Test_2 (add, pop, discard, clear = empty)",
        "Test_3 (additions extend garden)",
        "Test_4 (removals shrink garden)",
        "Test_5 (multiple discards shrink garden)",
        "Test_6 (pop twice and clear = empty)",
        "Sample (add coconut and fig, remove lemon, discard banana)",
    ],
)
def test_9_3_4(data, expected):
    assert m_9_3_4(data) == expected
