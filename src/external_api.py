import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

from src.utils import transaction_loader

load_dotenv()


def currency_converter(transactions: list[Dict], id_transaction: int | None = None) -> float | Any:
    """
    Данная функция просматривает список транзакций и по номеру транзакции
    определяет тип текущий валюты
    Если он не в рублях, тогда обращаемся к https://api.apilayer.com/
    и узнаем текущий курс, конвертируя при этом полученную из транзакции сумму в рубли

    :param transactions: - список транзакций
    :param id_transaction: - номер транзакции
    :return: - сумма в рублях
    """

    # Проверка API ключа
    api_key = os.getenv("apikey")
    if not api_key:
        raise ValueError("Отсутствует API ключ!")

    # Находим нужную транзакцию
    transaction = next((t for t in transactions if t.get("id") == id_transaction), None)
    if not transaction:
        return 0.0

    # Извлекаем данные о сумме и валюте из текущей транзакции
    try:
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]
    except (KeyError, TypeError, ValueError):
        return 0.0

    # Если валюта уже в рублях - просто возвращаем сумму
    if currency == "RUB":
        return amount

    # Если же нет, то конвертируем через API
    url = "https://api.apilayer.com/exchangerates_data/convert"
    headers = {"apikey": api_key}
    params = {"amount": amount, "from": currency, "to": "RUB"}

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()  # Проверка HTTP ошибок
        return round(response.json()["result"], 2)
    except (requests.RequestException, KeyError, ValueError):
        return 0.0  # Возвращаем 0 при ошибке конвертации


if __name__ == "__main__":
    variable = transaction_loader("..\\data\\operations.json")
    print(currency_converter(variable, 207126257))
    print(currency_converter(variable, 667307132))
    print(currency_converter(variable, 41428829))
