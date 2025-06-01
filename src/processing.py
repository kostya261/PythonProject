def filter_by_state(data_list: list, state: str = "EXECUTED") -> list:
    """
    Функция возвращает новый список словарей, содержащий только те словари, у которых
    ключ state соответствует указанному значению.

    :param data_list:
    :param state:
    :return:
    PS - Я понимаю, что список можно итерировать не по индексу как у меня в примере,
    а непосредственна по значениям списка.
    Просто я так пытаюсь разобраться, как это хозяйство всё работает
    Конструкции Python мне ломают мои привычки типа:

    for (int i = 0; i < 100; i++)
        {ваш код}

    for i = 1 to 100
        ваш код
    next

    но я обещаю в будущем исправиться
    """

    length_list = len(data_list)
    temp_list = list()

    for current_index in range(length_list):
        temp_list.append(data_list[current_index]) if data_list[current_index].get("state", 0) == state else temp_list

    return temp_list


def sort_by_date(date_list: list, ascending: bool = True) -> list:
    """
    Функция возвращает новый список, отсортированный по дате (date)

    :param date_list:
    :param ascending:
    :return:
    """
    if not date_list:
        print("Empty")
        return []
    sorted_list = sorted(date_list, key=lambda x: x.get("date", 0), reverse=ascending)

    return sorted_list
