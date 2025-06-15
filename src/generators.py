from typing import Dict, Generator


def filter_by_currency(date_list: list, currency: str = "USD") -> Generator[Dict, str, None]:
    """
    принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращать итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD).

    :param date_list:
    :param currency:
    :return:
    """
    if not date_list or currency is None:
        return  # если список отсутствует - выходим из функции

    normalized_currency = currency.strip().upper()
    """ currency  надлежащего вида без пробелов и в верхнем регистре """

    for transaction in date_list:
        transaction_temp = transaction.get("operationAmount").get("currency")
        """ данную переменную завел на случай, если понадобится определять валюту не по коду а по имени """
        if transaction_temp.get("code") is not None and transaction_temp.get("code") == normalized_currency:
            yield transaction


def transaction_descriptions(date_list: list) -> Generator[str]:
    """
    Принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди

    :param date_list:
    :return:
    """
    if not date_list:
        yield "Нет доступных транзакций"
        return  # если список отсутствует - выходим из функции

    for transaction in date_list:
        description = str(transaction.get("description", "")).strip()
        """ описание транзакции если она имеется """
        if description is not None:
            yield description


def card_number_generator(start_value: int = 1, end_value: int = 5) -> Generator[str]:
    """
    Генерирует номера карт
    от 0000 0000 0000 0001 до 9999 9999 9999 9999

    :param start_value: - начальное значение.
                        Если стартовое значение <= 0 тогда оно автоматом приравнивается к 1
    :param end_value: - конечное значение
    :return:
    """

    zero_card = "0" * 16
    """ исходная пустая карта """

    current_number_card_integer = start_value if start_value > 0 else 1
    """ текущий номер карты """

    while True:
        current_number_card_str = str(current_number_card_integer)
        """ текущий номер карты в строковом эквиваленте """
        current_number_card_len = len(current_number_card_str)
        """ длинна сгенерированного номера в символах """
        zero_card = zero_card[:-current_number_card_len] + current_number_card_str
        yield f"{zero_card[0:4]} {zero_card[4:8]} {zero_card[8:12]} {zero_card[12:16]}"
        current_number_card_integer += 1
        if current_number_card_integer > end_value or current_number_card_integer > 9999999999999999:
            break  # raise "Out of range!"
