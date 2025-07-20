import logging
from pathlib import Path

#описание логера
logger = logging.getLogger(__name__)

log_dir = Path(__file__).parent.parent
log_dir.mkdir(exist_ok=True)

file_handler = logging.FileHandler(log_dir/"logs\\masks.log", "w+", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


INVALID_CARD_NUMBER = "Неверный номер карты!"


def get_mask_card_number(number_card: str) -> str:
    """
    Данная функция маскирует номер банковской карты.

    На вход принимается строка.

    На выходе форматированная строка.

    :param number_card:
    :return:
    """

    digits = "".join(char for char in number_card if char.isdigit())

    if len(digits) != 16:
        logger.error(f"\nИмя файла: {__name__}, имя функции get_mask_card_number - {INVALID_CARD_NUMBER}")
        raise ValueError(INVALID_CARD_NUMBER)
    logger.info(f"\nИмя файла: {__name__}, имя функции get_mask_card_number - Ок")
    return f"{digits[0:4]} {digits[4:6]}** **** {digits[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Данная функция маскирует номер счёта.

    На вход принимается строка.

    На выходе строка.

    :param account_number:
    :return:
    """
    digits = "".join(char for char in account_number if char.isdigit())
    if len(digits) != 20:
        logger.error(f"\nИмя файла: {__name__}, имя функции get_mask_account - {INVALID_CARD_NUMBER}")
        raise ValueError(INVALID_CARD_NUMBER)
    logger.info(f"\nИмя файла: {__name__}, имя функции get_mask_account - Ok")
    return f"**{digits[-4:]}"
