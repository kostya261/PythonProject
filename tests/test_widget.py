from datetime import datetime

import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card(account_cards: dict[str, str]) -> None:
    """
    Проверяем функцию mask_account_card которая маскирует в зависимости
    от того что подано на вход, либо счёт, либо карту.
    Данные берутся из fixture в виде словаря, в котором указаны
    как данные на входе, так и предполагаемые данные на выходе
    :param account_cards:
    :return Ничего:
    """
    assert mask_account_card(account_cards["card"]) == account_cards["result"]


@pytest.mark.parametrize(
    "card, expected",
    [
        ("Счет 73654108430535874307", "Счет **4307"),
        ("Счет 7365408430535874307", "Неверный номер карты!"),
        ("Visa Platinum 7000712289606361", "Visa Platinum 7000 71** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 715300734726758", "Неверный номер карты!"),
        ("", "Неверный номер карты!"),
    ],
)
def test_mask_account_card_parametrize(card: str, expected: str) -> None:
    """
    Данная функция проверяет функцию mask_account_card
    :param card:
    :param expected:
    :return:
    """
    assert mask_account_card(card) == expected


def test_get_date() -> None:
    """
    Тестируем функцию get_date
    Проверяется, как функция в целом фоспринимает стандарт принимаемой даты
    Затем этот же самый формат подаётся, но уже в виде готовой текстовой строки
    Также проверяем если строка будет пустой
    И если дата будет подана в неправильном формате
    :return - Ничего:
    """
    now_time = datetime.now()
    assert get_date(str(now_time.isoformat()))
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    time_data = ""
    assert get_date(str(time_data)) == "Неверный формат даты!"
    time_data = "10.13.2005"
    assert get_date(str(time_data)) == "Неверный формат даты!"
