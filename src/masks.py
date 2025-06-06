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
        raise ValueError(INVALID_CARD_NUMBER)

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
        raise ValueError(INVALID_CARD_NUMBER)
    return f"**{digits[-4:]}"
