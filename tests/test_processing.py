import pytest

from src.processing import filter_by_state, sort_by_date

list_date = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 939719572, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

list_date_empty: list = []

list_date_executed = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 939719572, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]

list_date_canceled = [
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

list_date_sort_up: list = [
    {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
    {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
    {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
    {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
    {"date": "2018-06-30T02:08:58.425572", "id": 939719572, "state": "EXECUTED"},
]

list_date_sort_down: list = [
    {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
    {"date": "2018-06-30T02:08:58.425572", "id": 939719572, "state": "EXECUTED"},
    {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
    {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
    {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
]


@pytest.mark.parametrize(
    "date_list, state, expected",
    [
        (list_date, "EXECUTED", list_date_executed),
        (list_date, "CANCELED", list_date_canceled),
        (list_date, "CALED", list_date_empty),
        ([], "CANCELED", list_date_empty),
    ],
)
def test_filter_by_state(date_list: list, state: str, expected: list) -> None:
    """
    Тестируем функцию filter_by_state

    :param date_list:
    :param state:
    :param expected:
    :return:
    """
    assert filter_by_state(date_list, state) == expected


@pytest.mark.parametrize(
    "date_list, ascending, expected",
    [
        (list_date, True, list_date_sort_up),
        (list_date, False, list_date_sort_down),
        ([], False, []),
        ([], True, []),
        ([], None, []),
    ],
)
def test_sort_by_date(date_list: list, ascending: bool, expected: list) -> None:
    """
    Проверяем функцию sort_by_date, которая сортирует списки по датам
    как вверх по списку так и вниз
    так же проверяется как ведет себя функция если список пустой

    :param date_list:
    :param ascending:
    :param expected:
    :return:
    """
    assert sort_by_date(date_list, ascending) == expected
