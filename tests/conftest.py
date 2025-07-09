from datetime import datetime
from typing import Any

import pytest


@pytest.fixture
def error_message() -> str:
    return "Неверный номер карты!"


@pytest.fixture
def error_data_message() -> str:
    return "Неверный формат даты!"


@pytest.fixture
def current_data() -> str:
    now_time = datetime.now()
    return str(now_time.isoformat())


@pytest.fixture(
    params=[
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (100, 103, ["0000 0000 0000 0100", "0000 0000 0000 0101", "0000 0000 0000 0102", "0000 0000 0000 0103"]),
        # Если имеются начальные значения меньше минимального
        (
            -100,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (
            1,
            -5,
            [
                "0000 0000 0000 0001",
            ],
        ),
        # Если значения находятся в пределах допуска
        (
            1432_4321_5678_7654,
            1432_4321_5678_7659,
            [
                "1432 4321 5678 7654",
                "1432 4321 5678 7655",
                "1432 4321 5678 7656",
                "1432 4321 5678 7657",
                "1432 4321 5678 7658",
                "1432 4321 5678 7659",
            ],
        ),
        # Если конечное значение выходит за предел допустимых значений
        (
            9999_9999_9999_9998,
            19999_4321_5678_7659,
            [
                "9999 9999 9999 9998",
                "9999 9999 9999 9999",
            ],
        ),
    ]
)
def valid_cards(request: Any) -> Any:
    return request.param


@pytest.fixture(
    params=[
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
    ]
)
def input_data(request: Any) -> Any:
    return request.param


@pytest.fixture(params=[(1, -2), (2.2, 10), (0, 2), (10, 1)])
def incorrect_data_for_decorator(request: Any) -> Any:
    return request.param


@pytest.fixture(params=[  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    }}])
def correct_data_for_transaction_loader(request: Any) -> Any:
    return request.param


@pytest.fixture
def test_transactions() -> Any:
    return [
    {"id": 1, "operationAmount": {"amount": "100", "currency": {"code": "USD"}}},
    {"id": 2, "operationAmount": {"amount": "500", "currency": {"code": "EUR"}}},
    {"id": 3, "operationAmount": {"amount": "200", "currency": {"code": "RUB"}}},
    {"id": 4, "operationAmount": {"invalid": "data"}},  # Неверная транзакция
]
