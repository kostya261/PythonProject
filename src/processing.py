def filter_by_state(data_list: list, state: str = "EXECUTED") -> list:
    """
    Функция возвращает новый список словарей, содержащий только те словари, у которых
    ключ state соответствует указанному значению.

    :param data_list:
    :param state:
    :return:
    """

    return [item for item in data_list if item.get("state") == state]


def sort_by_date(date_list: list, ascending: bool = True) -> list:
    """
    Функция возвращает новый список, отсортированный по дате (date)

    :param date_list:
    :param ascending:
    :return:
    """
    if not date_list:
        return []

    return sorted(date_list, key=lambda x: x.get("date", 0), reverse=ascending)
