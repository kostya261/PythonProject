import pytest

from src.masks import get_mask_account, get_mask_card_number

valid_cards = [
    ("1234567890123456", "1234 56** **** 3456"),
    ("0000111122223333", "0000 11** **** 3333"),
    ("  1234 5678 9012 3456  ", "1234 56** **** 3456"),
    ("1234-5678-9012-3456", "1234 56** **** 3456"),
    ("Visa 1234 5678 9012 3456", "1234 56** **** 3456"),
    ("MC-1234-5678-9012-3456", "1234 56** **** 3456"),
    ("Карта: 1234 5678 9012 3456", "1234 56** **** 3456"),
    ("Visa Platinum 7000 7122 8960 6361", "7000 71** **** 6361"),
    ("Maestro 7000792108106361", "7000 79** **** 6361"),
    ("MasterCard 7158 3007 3472 6758", "7158 30** **** 6758"),
    ("Счет 1234567890123456", "1234 56** **** 3456"),
    ("Платежная карта № 1234-5678-9012-3456", "1234 56** **** 3456"),
]


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
]


valid_accounts = [
    ("Счет 73654108430535874307", "**4307"),
    ("Счет   73654108430535874307  ", "**4307"),
    ("Счет 7365-4108-4305-3587-4307  ", "**4307"),
    ("Счет 7365 4108 4305 3587 4307", "**4307"),
]


invalid_accounts = [
    "Счет 736541084305358874307",
    "Счет 7365410843053588747",
    "",
    "    ",
    "Счет без номера",
    "1234 2345 2345",
    "12d3 654t 3245 5678 fght",
]


@pytest.mark.parametrize("card_input, expected", valid_cards)
def test_valid_card_masking(card_input: str, expected: str) -> None:
    assert get_mask_card_number(card_input) == expected


@pytest.mark.parametrize("card_input", invalid_cards)
def test_invalid_card_errors(card_input: str, error_message: str) -> None:
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(card_input)
    assert str(exc_info.value) == error_message


@pytest.mark.parametrize("card_input, expected", valid_accounts)
def test_valid_account_masking(card_input: str, expected: str) -> None:
    assert get_mask_account(card_input) == expected


@pytest.mark.parametrize("card_input", invalid_accounts)
def test_invalid_account_errors(card_input: str, error_message: str) -> None:
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(card_input)
    assert str(exc_info.value) == error_message
