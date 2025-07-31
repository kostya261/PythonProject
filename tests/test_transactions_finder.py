import pytest

from src.transactions_finder import process_bank_operations, process_bank_search

# from tests.test_processing import list_empty

list_date = [
    {"id": 1, "description": "EXECUTED"},
    {"id": 2, "description": "PENDING"},
    {"id": 3, "description": "CANCELED"},
    {"id": 4, "description": "EXECUTED"},
    {"id": 5, "description": "CANCELED"},
    {"id": 6, "description": "EXECUTED"},
    {"id": 7, "description": "EXECUTED"},
    {"id": 8, "description": "CANCELED"},
    {"id": 9, "description": "PENDING"},
    {"id": 10, "description": "PENDING"},
]

list_empty: list = []

list_executed = [
    {"id": 1, "description": "EXECUTED"},
    #    {"id": 2, "description": "EXECUTED"},
    {"id": 4, "description": "EXECUTED"},
    {"id": 6, "description": "EXECUTED"},
    {"id": 7, "description": "EXECUTED"},
]

list_canceled = [
    {"id": 3, "description": "CANCELED"},
    {"id": 5, "description": "CANCELED"},
    {"id": 8, "description": "CANCELED"},
]


@pytest.mark.parametrize(
    "date_list, search, expected",
    [
        (list_date, "EXECUTED", list_executed),
        (list_date, "CANCELED", list_canceled),
        (list_date, "", list_empty),
        (list_date, "UNKNOW", list_empty),
        (list_date, None, list_empty),
        (list_empty, None, list_empty),
        (list_empty, "EXECUTED", list_empty),
        (list_empty, "CANCELED", list_empty),
    ],
)
def test_process_bank_search(date_list: list, search: str, expected: list) -> None:
    assert process_bank_search(date_list, search) == expected


@pytest.mark.parametrize(
    "date_list, categories, expected",
    [
        # Тест 1: Все три категории
        (
            list_date,
            ["EXECUTED", "CANCELED", "PENDING"],
            {"EXECUTED": 4, "CANCELED": 3, "PENDING": 3},
        ),
        # Тест 2: Только EXECUTED и PENDING
        (
            list_date,
            ["EXECUTED", "PENDING"],
            {"EXECUTED": 4, "PENDING": 3},
        ),
        # Тест 3: Только CANCELED
        (
            list_date,
            ["CANCELED"],
            {"CANCELED": 3},
        ),
        # Тест 4: Категория, которой нет в данных (должен вернуть {})
        (
            list_date,
            ["UNKNOWN"],
            {},
        ),
        # Тест 5: Пустые данные
        (
            [],
            ["EXECUTED", "CANCELED"],
            {},
        ),
    ],
)
def test_process_bank_operations(date_list: list, categories: list, expected: dict) -> None:
    assert process_bank_operations(date_list, categories) == expected
