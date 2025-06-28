from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info_sting: str = "") -> str:
    """
    Принимает на вход строку с наименованием карты и её номером

    После чего номер маскирует

    На выходе получаем наименование карты и маскированный номер

    :param card_info_sting:
    :return:

    """
    card_error_message: str = "Неверный номер карты!"
    if not card_info_sting.strip():
        return card_error_message

    # приводим строку к требуемому виду
    normalized_card_sting: str = card_info_sting.lower().strip()
    # Извлечение цифр из строки
    all_digits: str = "".join(char for char in normalized_card_sting if char.isdigit())
    # Извлекаю имя карты
    card_name: str = "".join(char for char in card_info_sting if not char.isdigit() and char not in ("-", "/")).strip()

    # На всякий случай в переменной сообщение об ошибке.
    # Если маскировка карты пройдёт успешно, то в этой переменной будет результат
    mask_card_info: str = card_error_message

    # Проверяю счёт у нас на входе или иная невидаль
    if ("счет " in normalized_card_sting) or ("счёт " in normalized_card_sting):
        # если счёт, то смотрим, 20ть ли цифирь, если да, то маскируем
        if len(all_digits) == 20:
            mask_card_info = card_name + " " + get_mask_account(all_digits)
    else:
        # если не счёт, то возможно карта, тогда смотрим 16ть ли цифирь
        # и если 16ть, маскируем, если нет, то просто выходим
        if len(all_digits) == 16:
            mask_card_info = card_name + " " + get_mask_card_number(all_digits)

    # если хотя бы одна функция в условии выше отработала, тогда возвращаем результат
    # если же нет, то записанное ранее сообщение об ошибке
    return mask_card_info


def get_date(iso_date: str) -> str:
    """
    принимает на вход строку с датой в ISO 8601 формате

    "2024-03-11T02:26:18.671407"

    и возвращает строку с датой в формате

    "ДД.ММ.ГГГГ" ("11.03.2024")
    :param iso_date:
    :return:
    """
    error_message: str = "Неверный формат даты!"
    if not iso_date:
        return error_message
    try:
        return datetime.fromisoformat(iso_date).strftime("%d.%m.%Y")
    except (ValueError, TypeError):
        return error_message
