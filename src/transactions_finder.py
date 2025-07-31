import re
from collections import Counter

import pandas as pd

from src.widget import get_date, mask_account_card


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Функция, принимает список словарей с данными о банковских операциях и строку поиска.
    Возвращает список словарей, у которых в описании есть данная строка.

    :param data:
    :param search:
    :return:
    """

    if not data or search == "" or search is None:
        return []

    # Проверяем, есть ли хотя бы в одном словаре ключ "description"
    if not any("description" in item for item in data):
        return []

    df = pd.DataFrame(data)
    filtered_df = df[df["description"].str.contains(search, regex=True, na=False)]

    return filtered_df.to_dict(orient="records")


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Функция, которая принимает список словарей с данными о банковских операциях и список категорий операций.
    Возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    Категории операций хранятся в поле description.

    :param data:
    :param categories:
    :return:
    """
    if not data:
        return {}
    filter_data: dict = {}
    df = pd.DataFrame(data)
    counted = Counter(df["description"])

    for trans, value in counted.items():
        if trans in categories:
            filter_data[trans] = value

    return filter_data


def print_transactions(data: list[dict], json_file: bool = False) -> None:
    """
    Выводит отформатированный список транзакций.

    :param data: Список транзакций (словарей).
    :param json_file: Если True, берёт сумму и валюту из вложенной структуры operationAmount.

    Обрабатывает:
    - Отсутствие транзакций
    - Разные форматы данных (JSON/плоский)
    """

    if not data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Всего банковских операций в выборке: {len(data)}")

    for transaction in data:
        # print(transaction)
        print()
        print(get_date(transaction["date"]), transaction["description"])

        #    print(type(transaction["from"]))
        if re.findall("перевод", transaction["description"].lower(), flags=0):
            print(f"{mask_account_card(transaction["from"])} -> {mask_account_card(transaction["to"])}")
        else:
            print(mask_account_card(transaction["to"]))

        if json_file is False:
            print(f"Сумма: {round(transaction["amount"])} {transaction["currency_name"]}")
        else:
            print(
                f"Сумма: {transaction["operationAmount"]["amount"]} "
                f"{transaction["operationAmount"]["currency"]["name"]}"
            )
