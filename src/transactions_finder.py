import re
from collections import Counter

import pandas as pd

from src.widget import get_date, mask_account_card


def sort_by_date(data: list[dict], ascend: bool = False) -> list[dict]:
    """
    Сортирует список словарей по ключу 'date' с использованием Pandas.

    - Если входные данные пусты или не содержат ключ 'date', возвращает [].


    :param data: Список словарей, где каждый содержит ключ 'date'.
    :param ascend: Если True, сортировка по возрастанию (старые записи первыми).

    return:
        Отсортированный список словарей или [] при ошибках.
    """

    if not data:
        return []

    return pd.DataFrame(data).sort_values("date", ascending=ascend).to_dict(orient="records")


def filter_by_currency_code(data: list[dict], currency_code: str, json_file: bool = False) -> list[dict]:
    """
    Фильтрует операции по коду валюты (RUB/USD/EUR и т.д.).

    :param data: Список операций (словарей).
    :param currency_code: Код валюты для фильтрации (регистронезависимый).
    :param json_file: Если True, ищет код в структуре operationAmount->currency->code.
                      Если False, ищет в поле currency_code.

    return:
        Отфильтрованный список операций или [], если:
        - входные данные пусты,
        - валюта не найдена,
        - нет нужных ключей
    """
    try:
        if not data:
            return []
        df = pd.DataFrame(data)
        if json_file is True:
            filtered_df = df[
                df["operationAmount"]
                .apply(lambda x: x["currency"]["code"])
                .str.contains(currency_code, regex=True, na=False)
            ]
        else:
            filtered_df = df[df["currency_code"].str.contains(currency_code, regex=True, na=False)]
        return filtered_df.to_dict(orient="records")
    except Exception:
        return []


def filter_by_status(data: list[dict], state_line: str = "executed") -> list[dict]:
    """
    Фильтрует операции по статусу (EXECUTED, CANCELED и т.д.).

    :param data: Список операций (словарей).
    :param state_line: Статус для фильтрации (регистронезависимый).
                   По умолчанию "EXECUTED".

    return:
        Отфильтрованный список операций или [], если:
        - входные данные пусты,
    """

    if not data:
        return []
    try:
        df = pd.DataFrame(data)
        filtered_df = df[df["state"].str.contains(state_line, regex=True, na=False)]

        return filtered_df.to_dict(orient="records")
    except Exception:
        return []


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Функция, принимает список словарей с данными о банковских операциях и строку поиска.
    Возвращает список словарей, у которых в описании есть данная строка.

    :param data:
    :param search:
    :return:
    """

    if not data:
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
