import json
import logging
from pathlib import Path

# описание логера
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("..\\logs\\utils.log", "w+", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


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
        logger.error(f"\nИмя: {__name__} transaction_loader - нет имени файла!")
        return []

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            logger.info(f"\nИмя: {__name__} transaction_loader - Ok!")
            return data
        return []

    except (json.JSONDecodeError, UnicodeDecodeError):
        # Обработка ошибок: пустой файл, битый JSON или проблемы с кодировкой
        logger.debug(f"\nИмя: {__name__} transaction_loader - пустой файл, битый JSON или проблемы с кодировкой!")
        return []


if __name__ == "__main__":
    print(transaction_loader("..\\data\\operations.json"))
    # print(transaction_loader("..\\data\\operations.jsn"))
