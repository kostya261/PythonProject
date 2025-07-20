from unittest.mock import patch, Mock

import pandas as pd

from src.transactions_loader import csv_loader, excel_loader


@patch("src.transactions_loader.pd.read_csv")
def test_csv_loader(mock_read_csv: Mock) -> None:
    """
    Тестируем функцию csv_loader
    :param mock_read_csv:
    :return:
    """
    # mock_read_csv.return_value = pd.DataFrame({"value": [10, 20, 30]})
    mock_read_csv.return_value = pd.DataFrame(
        [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
    )
    # Вызываем функцию
    result = csv_loader("transactions.csv")
    print("\n", str(result), "\n")
    # Проверяем реальные аргументы
    mock_read_csv.assert_called_once_with("transactions.csv", delimiter=";", encoding="utf-8")
    # Проверяем результат
    assert result == [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]


@patch("src.transactions_loader.pd.read_excel")
def test_execl_loader(mock_read_excel: Mock) -> None:
    """
    Тестируем функцию excel_loader
    :param mock_read_excel:
    :return:
    """
    mock_read_excel.return_value = pd.DataFrame(
        [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
    )
    # Вызываем функцию
    result = excel_loader("transactions_excel.xlsx")

    # Проверяем реальные аргументы
    mock_read_excel.assert_called_once_with("transactions_excel.xlsx")
    # Проверяем результат
    assert result == [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
