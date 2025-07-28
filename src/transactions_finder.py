import re
from collections import Counter

import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

from src.transactions_loader import csv_loader, excel_loader
from src.utils import transaction_loader


def sort_by_date(data: list[dict], ascend: bool = False) -> list[dict]:
    df = pd.DataFrame(data)
    df_sorted = df.sort_values('date', ascending=ascend)
    #print(df_sorted)
    return df_sorted.to_dict(orient="records")


def filter_by_currency_code(data: list[dict], currency_code: str, json_file: bool = True) -> list[dict]:
    df = pd.DataFrame(data)
    if json_file == True:
        filtered_df = df[
            df['operationAmount'].apply(lambda x: x['currency']['code']).str.contains(currency_code, regex=True,
                                                                                      na=False)]
    else:
        filtered_df = df[df['currency_code'].str.contains(currency_code, regex=True, na=False)]
    return filtered_df.to_dict(orient="records")


def filter_by_status(data: list[dict], state_line: str = "executed"):
    df = pd.DataFrame(data)
    #temp = df.to_dict(orient="records")
    filtered_df = df[df['state'].str.contains(state_line, regex=True, na=False)]

    return filtered_df.to_dict(orient="records")


def process_bank_search(data:list[dict], search:str)->list[dict]:
    """
    Функция, принимает список словарей с данными о банковских операциях и строку поиска.
    Возвращает список словарей, у которых в описании есть данная строка.

    При реализации этой функции используйте библиотеку re для работы с регулярными выражениями.

    :param data:
    :param search:
    :return:
    """



    df = pd.DataFrame(data)
    #temp = df.to_dict(orient="records")

    filtered_df = df[df['description'].str.contains(search, regex=True, na=False)]


    return filtered_df.to_dict(orient="records")



def process_bank_operations(data:list[dict], categories:list)->dict:
    """
    Функция, которая принимает список словарей с данными о банковских операциях и список категорий операций.
    Возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    Категории операций хранятся в поле description.

    :param data:
    :param categories:
    :return:
    """
    filter: dict = {}
    df = pd.DataFrame(data)
    counted = Counter(df["description"])

    for trans, value in counted.items():
        if trans in categories:
            filter[trans] = value

    return filter



if __name__ == "__main__":
    print()
    #json = transaction_loader("..\\data\\operations.json")
    csv = csv_loader("..\\data\\transactions.csv")
    #excel = excel_loader("..\\data\\transactions_excel.xlsx")
    #print(process_bank_operations(json, ["Открытие вклада", "Перевод со счета на счет"]))
    #print(process_bank_operations(csv, ["Открытие вклада", "Перевод со счета на счет"]))
    #print(process_bank_operations(excel,["Открытие вклада", "Перевод со счета на счет"]))

    #result = process_bank_search(csv, r"Открытие вклада")
    #print()
    #result2 = sort_by_date(result, True)
    #print(result2)
    #result3 = filter_by_currency_code(result2, "RUB")
    #print(result3)

    result1 = process_bank_search(csv, r"Открытие вклада")
    result12 = sort_by_date(result1, True)
    #print(result12)
    result13 = filter_by_currency_code(result12, "RUB", False)
    print(result13)