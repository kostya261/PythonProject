import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

transactions_2 = [
    {
        "id": 342264269,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Вывод средств со счёта",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 773106921,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет злоумышленника",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 194226722,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод кому то в организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

transactions_3 = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
    },
]


@pytest.mark.parametrize(
    "trans, currency, excepted",
    [
        (transactions, "USD", [939719570, 142264268, 895315941]),
        (transactions, "RUB", [873106923, 594226727]),
        (transactions, "UsD", [939719570, 142264268, 895315941]),
        (transactions, "usd", [939719570, 142264268, 895315941]),
        (transactions, "", []),
        (transactions, "набор неподходящих символов", []),
        (transactions, None, []),
    ],
)
def test_filter_by_currency_valid(trans: list, currency: str, excepted: list) -> None:
    """
    Проверяем filter_by_currency на работу с корректными значениями
    :param trans: - данные на входе, которые нужно обработать
    :param currency: - валюта
    :param excepted: - данные для проверки
    :return:
    """
    result = list(filter_by_currency(trans, currency))
    """список с отфильтрованными данными"""
    result_id_num = [transactions_id["id"] for transactions_id in result]
    """оставляем только id номера, что бы облегчить себе жизнь при проверке"""
    assert result_id_num == excepted  # ну и собственно проверяем


def test_empty_input() -> None:
    """
    Проверяем filter_by_currency на работу с пустым списком транзакций
    """
    result = list(filter_by_currency([]))
    assert result == []


@pytest.mark.parametrize(
    "trans, excepted",
    [
        (
            transactions,
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод со счета на счет",
                "Перевод с карты на карту",
                "Перевод организации",
            ],
        ),
        (
            transactions_2,
            [
                "Вывод средств со счёта",
                "Перевод со счета на счет злоумышленника",
                "Перевод кому то в организации",
            ],
        ),
    ],
)
def test_transaction_descriptions(trans: list, excepted: list) -> None:
    """
    Проверяем функцию с корректными данными на входе
    :param trans: - список транзакций
    :param excepted: - список данных на выходе
    """
    result = list(transaction_descriptions(trans))
    assert result == excepted  # ну и собственно проверяем


@pytest.mark.parametrize(
    "trans, excepted", [([], ["Нет доступных транзакций"]), (transactions_3, ["", "", "", "", ""])]
)
def test_transaction_descriptions_empty(trans: list, excepted: list) -> None:
    """
    Проверка функции при некорректных входных данных
    :param trans: - список транзакций
    :param excepted: - варианты проверочных данных
    :return:
    """
    result = list(transaction_descriptions(trans))
    assert result == excepted  # ну и собственно проверяем


def test_card_number_generator(valid_cards: tuple) -> None:
    """
    Проверяем функцию, которая генерирует новые номера карт в заданном диапазоне
    :param start_value: - начальное значение
    :param end_value: - конечное значение
    :param expected: - список для проверки сгенерированных значений
    :return:
    """
    start_value, end_value, expected = valid_cards
    gen_card = list()
    # пустой список для последовательной записи сгенерированных карт
    expected_card = list()
    # попутно создаем пустой список, куда будем последовательно класть варианты из expected

    for i in card_number_generator(start_value, end_value):
        gen_card.append(i)
        expected_card.append(expected)

    # после того как оба списка созданы, сравниваем их
    assert gen_card == expected
