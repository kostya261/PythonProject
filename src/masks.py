def get_mask_card_number(number_card: str) -> str:
    """
    Данная функция маскирует номер банковской карты.

    На вход принимается строка.

    На выходе форматированная строка.
    """
    number_card = number_card.strip()
    if len(number_card) == 16 and number_card.isdigit():
        hidden_card_number: str = f"{number_card[0:4]} {number_card[4:6]}** **** {number_card[-4:]}"
        return hidden_card_number
    else:
        return "Некорректный номер карты!"


def get_mask_card_number_new(number_card: str) -> str:
    """
    Данная функция маскирует номер банковской карты.

    На вход принимается строка.

    На выходе форматированная строка.
    """
    try:
        number_card = number_card.strip()
        # Избавляепмся от пробелов в начале и конце строки

        number_of_characters_per_line = len(number_card)
        # Вычисляем длину строки

        if number_of_characters_per_line == 16 and number_card.isdigit():
            # если длина не соответствует числу символов/ символы не цифровые, выводим: номер некоректен
            hidden_card_number = [number_card[i:i + 4] for i in range(0, number_of_characters_per_line, 4)]
            hidden_card_number[1] = hidden_card_number[1][0:2] + "**"  # Маскируем часть символов
            hidden_card_number[2] = "****"
            assembled_hidden_card_number: str = " ".join(hidden_card_number)  # Собираем в строку
            return assembled_hidden_card_number
        else:
            return "Неправильный номер карты!!!"
    except Exception:
        return "Неправильный номер карты!"


def get_mask_account(account_number: str) -> str:
    """
    Данная функция маскирует номер счёта.

    На вход принимается строка.

    На выходе строка.
    """
    account_number = account_number.strip()
    return f"**{account_number[-4:]}"
