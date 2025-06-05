import pytest

from src.widget import get_date, mask_account_card

# Параметры правильных данных карт
valid_cards = [
    ("Visa 1234 5678 9012 3456", "Visa 1234 56** **** 3456"),
    ("MC-1234-5678-9012-3456", "MC 1234 56** **** 3456"),
    ("Карта: 1234 5678 9012 3456", "Карта: 1234 56** **** 3456"),
    ("Visa Platinum 7000 7122 8960 6361", "Visa Platinum 7000 71** **** 6361"),
    ("Maestro 7000792108106361", "Maestro 7000 79** **** 6361"),
    ("MasterCard 7158 3007 3472 6758", "MasterCard 7158 30** **** 6758"),
    ("Платежная карта № 1234-5678-9012-3456", "Платежная карта № 1234 56** **** 3456"),
    ("Счет 73654108430535874307", "Счет **4307"),
    ("Счет   73654108430535874307  ", "Счет **4307"),
    ("Счет 7365-4108-4305-3587-4307  ", "Счет **4307"),
    ("Счет 7365 4108 4305 3587 4307", "Счет **4307"),
]


# Параметры неправильных данных карт
invalid_cards = [
    "1234",
    "12345678901234567890",
    "Card 1234 5678 9012",
    "Visa 1234abcd5678efgh",
    "",
    "    ",
    "Счет без номера",
    "123456789012345a",
    "1234 5678 9012 345",
    "Счет736541084305358874307",
    "Счет 7365410843053588747",
    "",
    "    ",
    "Счет без номера",
    "1234 2345 2345",
    "12d3 654t 3245 5678 fght",
]


# Параметры правильных данных
valid_dates = [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2023-12-31T23:59:59.999999", "31.12.2023"),
    ("2000-01-01T00:00:00.000000", "01.01.2000"),
    ("1999-02-28T15:30:45.123456", "28.02.1999"),
    ("2024-02-29T12:00:00.000000", "29.02.2024"),
]


# Параметры неправильных данных
invalid_dates = [
    "2024-03-32T00:00:00.000000",
    "2023-13-01T00:00:00.000000",
    "2024-03-11 ",
    "11.03.2024T02:26:18.671407",
    "2024-03-11T25:00:00.000000",
    "Hello World!",
    "2024/03/11T02:26:18.671407",
]


@pytest.mark.parametrize("card_input, expected", valid_cards)
def test_valid_card_masking(card_input: str, expected: str) -> None:
    assert mask_account_card(card_input) == expected


@pytest.mark.parametrize("card_input", invalid_cards)
def test_invalid_card_errors(card_input: str, error_message: str) -> None:
    assert mask_account_card(card_input) == error_message


# Тест для правильных данных
@pytest.mark.parametrize("iso_date, expected", valid_dates)
def test_valid_dates(iso_date: str, expected: str) -> None:
    result = get_date(iso_date)
    assert result == expected


# Тест для неправильных данных
@pytest.mark.parametrize("iso_date", invalid_dates)
def test_invalid_dates(iso_date: str, error_data_message: str) -> None:
    assert get_date(iso_date) == error_data_message


# Тест для пустой строки
@pytest.mark.parametrize("iso_date", [""])
def test_none_input(iso_date: str, error_data_message: str) -> None:

    assert get_date(iso_date) == error_data_message
