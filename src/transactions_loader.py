from typing import Dict

import pandas as pd


def csv_loader(file_path: str = "", delimit: str = ";") -> list[Dict]:
    """
    Функция читает файл формата csv и возвращает список со словарями
    :param file_path: - путь к файлу
    :param delimit: - Разделитель столбцов (по умолчанию ";")
    :return: - Список словарей с данными.
    """
    try:
        result = pd.read_csv(file_path, delimiter=delimit, encoding="utf-8").to_dict(orient="records")
        return result
    except FileNotFoundError:
        raise ValueError("Ошибка!")
    except pd.errors.ParserError:
        raise ValueError("Неверный CSV формат")


def excel_loader(file_path: str = "") -> list[Dict]:
    """
    Функция читает файл формата xlsx и возвращает список со словарями

    :param file_path: - путь к файлу
    :return: - Список словарей с данными.
    """
    try:
        result = pd.read_excel(file_path).to_dict(orient="records")
        return result
    except FileNotFoundError:
        raise ValueError("Ошибка!")
    except pd.errors.ParserError:
        raise ValueError("Неверный XLSX формат")


if __name__ == "__main__":
    var = csv_loader("..\\data\\transactions.csv")
    print(var)
    print()
    var = excel_loader("..\\data\\transactions_excel.xlsx")
    print(var[0]["from"])
