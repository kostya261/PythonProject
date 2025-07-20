from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card
import requests

transactions_2 = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},

    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},

    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},

    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},

    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},

    },
]


transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)

def t_filter_by_currency_valid(transactions_d: list, expect: list) -> None:
    result = list(filter_by_currency(transactions_d, "USD"))
    result_ids = [t["id"] for t in result]

    print(result_ids)
    assert(result_ids == expect)


def t_transaction_descriptions(card_input: list, excepted: list) -> None:
    result = list(transaction_descriptions(transactions))
    #result = list(filter_by_currency(transactions, "USD"))
    print(result)
    #result_id_num = [t["id"] for t in result]
    """оставляем только id номера, что бы облегчить себе жизнь при проверке"""
    #assert result_id_num == excepted #ну и собственно проверяем



if __name__ == "__main__":
    # Проверочные вызовы
    print(mask_account_card("Счет 73654108430535874307"))
    print(mask_account_card("Visa Platinum 7000712289606361"))
    print(mask_account_card("Maestro 7000792108106361"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Счет 35383033474447895560"))
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(mask_account_card("Счет 73654108430135874305"))

    print()

    # Если строка будет в таком виде, как сказано в задании...
    # Тогда всё у нас будет хорошо
    # ну либо опять не понял задание
    print(get_date("2024-03-11T02:26:18.671407"))

    print()

    print(
        "state ",
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        ),
    )

    print(
        "state ",
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
        ),
    )

    print(
        "sort ",
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 939719572, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            False,
        ),
    )

    print(
        "sort ",
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 939719572, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        ),
    )




    print(list(card_number_generator(9999999999999995,19999999999999999)))
    print(list(card_number_generator(96, 99)))
    print(list(card_number_generator(0, 9)))


#for card_number in card_number_generator(9999_2310_0990_0000,9999_2310_0992_3200):
    for card_number in card_number_generator():
        print(mask_account_card(card_number))
    print()

    for card_number in card_number_generator(-100, 15):
        print(card_number)

    for card_number in card_number_generator(1, -15):
        print(card_number, "Ok")

    usd_transactions = filter_by_currency(transactions, "USD")
    for usd_trans in usd_transactions:
        print(usd_trans)


    descriptions = transaction_descriptions(transactions)
    for descript in descriptions:
        print(descript)


    t_filter_by_currency_valid(transactions, [939719570, 142264268, 895315941])
    t_transaction_descriptions(transactions,[939719570, 142264268, 895315941])


url = "https://api.apilayer.com/exchangerates_data/convert"

payload = {
    "amount": "1200",
    "from": "EUR",
    "to": "USD"
}
headers = {
    "apikey": "fSHSoKuZ2zVFxstaVw1stEq3GIFqPptc"
}

"""
response = requests.get(url, headers=headers, params=payload)

status_code = response.status_code
result = response.json()

print(status_code)
print(result)
"""