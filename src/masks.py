def get_mask_card_number(number_card: str) -> str:
    '''
    Данная функция маскирует номер банковской карты.

    На вход принимается строка.

    На выходе форматированная строка.

    :param number_card:
    :return:
    '''
    number_card = number_card.strip()
    if len(number_card) == 16 and number_card.isdigit():
        hidden_card_number: str = f"{number_card[0:4]} {number_card[4:6]}** **** {number_card[-4:]}"
        return hidden_card_number
    else:
        return "Неверный номер карты!"


def get_mask_account(account_number: str) -> str:
    '''
    Данная функция маскирует номер счёта.

    На вход принимается строка.

    На выходе строка.

    :param account_number:
    :return:
    '''
    if account_number.isdigit() and len(account_number) == 20:
        account_number = account_number.strip()
        return f"**{account_number[-4:]}"
    else:
        return "Неверный номер карты!"
