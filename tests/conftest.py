import pytest

card_invalid_string = "Неверный номер карты!"

card_numbers_for_test = [
    {"card": "6347551021023605", "result": "6347 55** **** 3605"},
    {"card": "6347551021023605  ", "result": "6347 55** **** 3605"},
    {"card": "  6347551021023605", "result": "6347 55** **** 3605"},
    {"card": "x347551021023605", "result": card_invalid_string},
    {"card": "34755102c1023605", "result": card_invalid_string},
    {"card": "634755102102365", "result": card_invalid_string},
    {"card": "63475510210236052", "result": card_invalid_string},
    {"card": "634755 102102 3605", "result": card_invalid_string},
]

account_numbers_for_test = [
    {"card": "63475526471021023605", "result": "**3605"},
    {"card": "63475510210236026475  ", "result": "**6475"},
    {"card": "  63475510210226473605", "result": "**3605"},
    {"card": "x347551021023605", "result": card_invalid_string},
    {"card": "34755102c1023605", "result": card_invalid_string},
    {"card": "634755102102365", "result": card_invalid_string},
    {"card": "63475510210236052", "result": card_invalid_string},
    {"card": "634755 102102 3605", "result": card_invalid_string},
]


account_card_for_test = [
    {"card": "Счет 73654108430535874307", "result": "Счет **4307"},
    {"card": "Счет 7365408430535874307", "result": card_invalid_string},
    {"card": "Visa Platinum 7000712289606361", "result": "Visa Platinum 7000 71** **** 6361"},
    {"card": "Maestro 7000792108106361", "result": "Maestro 7000 79** **** 6361"},
    {"card": "MasterCard 7158300734726758", "result": "MasterCard 7158 30** **** 6758"},
    {"card": "Maestro 1596837868705199", "result": "Maestro 1596 83** **** 5199"},
    {"card": "Счет 64686473678894779589", "result": "Счет **9589"},
    {"card": "Счет 646864736788947795589", "result": card_invalid_string},
    {"card": "MasterCard 715300734726758", "result": card_invalid_string},
    {"card": "Счет 35383033474447895560", "result": "Счет **5560"},
    {"card": "Счет 3538303347с447895560", "result": card_invalid_string},
    {"card": "Visa Classic 6831982476737658", "result": "Visa Classic 6831 98** **** 7658"},
    {"card": "Visa Classic 683198247637658", "result": card_invalid_string},
    {"card": "Visa Classic 683198247637652448", "result": card_invalid_string},
    {"card": "Visa Platinum 8990922113665229", "result": "Visa Platinum 8990 92** **** 5229"},
    {"card": "Visa Platinum ", "result": card_invalid_string},
    {"card": "", "result": card_invalid_string},
    {"card": "Visa Gold 5999414228426353", "result": "Visa Gold 5999 41** **** 6353"},
    {"card": "счет 73654108430135874305", "result": "Счет **4305"},
    {"card": "сет 73654108430135874305", "result": card_invalid_string},
    {"card": "сЧет 73654108430135874305", "result": "Счет **4305"},
]


@pytest.fixture(params=card_numbers_for_test)
def card_numbers(request):
    return request.param


@pytest.fixture(params=account_numbers_for_test)
def account_numbers(request):
    return request.param


@pytest.fixture(params=account_card_for_test)
def account_cards(request):
    return request.param
