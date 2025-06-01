from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_numbers: dict) -> None:
    """
    Тестируется функция get_mask_card_number.
    Данные для тестов берутся из Fixture
    :param card_numbers:
    :return:
    """
    assert get_mask_card_number(card_numbers["card"]) == card_numbers["result"]


def test_get_mask_account(account_numbers: dict) -> None:
    """
    Тестируется функция get_mask_account.
    Данные для тестов берутся из Fixture
    :param card_numbers:
    :return:
    """
    assert get_mask_account(account_numbers["card"]) == account_numbers["result"]
