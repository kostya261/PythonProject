from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info_sting: str = "") -> str:
    """
    Принимает на вход строку с наименованием карты и её номером

    После чего номер маскирует

    На выходе получаем наименование карты и маскированый номер

    :param card_info_sting:
    :return:

    """

    temp_card_info_sting: str = card_info_sting.lower().strip()
    # print(temp_card_info_sting)
    temp_result: str = ""
    card_error_message: str = "!!!Неверный номер карты!"
    mask_card_info: str = card_error_message
    if card_info_sting != "":
        if ("счет " in temp_card_info_sting) or ("счёт " in temp_card_info_sting):
            temp_result = get_mask_account(temp_card_info_sting[5:])
            mask_card_info = "Счет " + temp_result if temp_result != card_error_message else card_error_message
        else:
            temp_result = get_mask_card_number(temp_card_info_sting[-16:])
            mask_card_info = (
                card_info_sting[0:-16] + temp_result if temp_result != card_error_message else card_error_message
            )

    return mask_card_info


def get_date(iso_date: str) -> str:
    """
    принимает на вход строку с датой в формате

    "2024-03-11T02:26:18.671407"

    и возвращает строку с датой в формате

    "ДД.ММ.ГГГГ" ("11.03.2024")
    :param iso_date:
    :return:
    """

    return iso_date[8:8 + 2] + "." + iso_date[5:5 + 2] + "." + iso_date[:4]
