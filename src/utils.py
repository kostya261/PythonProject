import json
from pathlib import Path


# currency_converter
def transaction_loader(file_path: str = "") -> list:
    """
    Загружает список транзакций из JSON-файла.

    Параметры:
    file_path (str): Путь к JSON-файлу

    Возвращает:
    list: Список транзакций (словарей) или пустой список при:
        - Файл не найден
        - Файл пустой
        - JSON не содержит список
        - Ошибка декодирования
    """
    path = Path(file_path)
    # Проверка существования файла
    if not path.is_file():
        return []

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data
        return []

    except (json.JSONDecodeError, UnicodeDecodeError):
        # Обработка ошибок: пустой файл, битый JSON или проблемы с кодировкой
        return []


if __name__ == "__main__":
    print(transaction_loader("..\\data\\operations.json"))
