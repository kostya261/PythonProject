# Проект домашнего задания на SkyEng
## Описание:
Проект домашнего задания по созданию виджета для работы с банковскими картами.

## Установка:

1. Клонируйте репозиторий:
   [ссылка](https://github.com/kostya261/PythonProject/pull/3)
   
3. Зависимости указанные в файле: *pyproject.toml*
```
[tool.poetry.dependencies]
python = "^3.13"
poetry-core = "^2.1.3"
shell = "^1.0.1"
python-dotenv = "^1.1.1"


[tool.poetry.group.dev.dependencies]
requests = "^2.32.3"
pytest = "^8.3.5"
pytest-cov = "^6.1.1"


[tool.poetry.group.lint.dependencies]
flake8 = "^7.2.0"
mypy = "^1.15.0"
black = "^25.1.0"
isort = "^6.0.1"


[tool.black]
# Максимальная длина строки
line-length = 119
# Файлы, которые не нужно форматировать
exclude = """ \\.git """


[tool.isort]
# максимальная длина строки
line_length = 119


[tool.mypy]
disallow_untyped_defs = true
warn_return_any = true
exclude = 'venv'


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

```

## Использование:

Откройте проект например в PyCharm, найдите PythonPackage\test, откройте файл main.py и запустите его.
По желанию можно его всячески модифицировать в рамках тестирования написанных функций.

В PythonPackage\src описаны три модуля:
**masks.py, widget.py, processing.py**, которые и реализуют весь скромный функционал домашнего задания.

### masks.py
В модуле masks.py описаны функции *get_mask_card_number* и *get_mask_account*
обе функции выполняют маскировку реквизитов:

*get_mask_card_number* - маскирует номера карт
Принимает на входе строку с номером карты.
На выходе строка с маскированым номером

*get_mask_account* - маскирует номер счёта
Принимает на входе строку с номером счёта.
На выходе строка с маскированым номером

Примеры использования:
```
temp_result = get_mask_card_number("4365592421228764")
print(temp_result)
```
Результат:
```
4365 59** **** 8764
```

```
temp_result = get_mask_account("12345678910111213145")
print(temp_result)
```
 
Результат:
```
**3145
```
14.04.2025  00:15
Добавлено логирование работы функций


### widget.py
В данном модуле описаны функции: 

*mask_account_ card* - которая принимает на вход строку с наименованием карты и её номером после чего определяет что это за карта
и вызывает необходимую функцию из модуля masks.py и возвращает строку с маскированным номером карты

*get_date* - конвертирует строку формата **"2024-03-11T02:26:18.671407"** в строку где указана дата в формате **ДД.ММ.ГГГ**

Пример использования:
```
print(mask_account_card("Счет 73654108430535874307"))
print(mask_account_card("Visa Platinum 7000712289606361"))
print(mask_account_card("Maestro 7000792108106361"))
```

Результат:
```
Счет **4307
Visa Platinum 7000 71** **** 6361
Maestro 7000 79** **** 6361
```

```
print(get_date("2024-03-11T02:26:18.671407"))
```

Результат:
```
11.03.2024
```


### processing.py
processing.py так же содержит две функции как и предыдущие модули:

*filter_by_state* - Функция возвращает новый список словарей, содержащий только те словари, у которых
ключ state соответствует указанному значению.

Принимает на входе два параметра: 
*список с данными карт
*строка с параметром state по которому происходит отбор карт в новый список

На выходе функции новый список с отобранными по заданному параметру картами


*sort_by_date* - Функция возвращает новый список, отсортированный по дате (date)

Принимает на входе два параметра: 
*список с данными карт
*Булевое значение которое указывает тип сортировки (возрастающи/ убывающий)

На выходе функции новый список с отсортированными по дате значениями.

Пример использования:
```
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
        "sort ",
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            True,
        ),
    )
```

Результат:
```
state  [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
sort  [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```


## generators.py
generatrors.py - добавлены новые функции

filter_by_currency(date_list: list, currency: str)
transaction_descriptions(date_list: list)
card_number_generator(start_value: int, end_value: int)

filter_by_currency - фильтрует выводимые данные по коду валюты
transaction_descriptions - выводит поочереди все транзакции из списка
card_number_generator - генерирует номера кредитных карт в указанном диапазоне


## utils.py
transaction_loader(file_path: str = "")

transaction_loader - загружает JSON файл содержащий данные о транзакциях и конвертирует в список


14.04.2025  00:15
Добавлено логирование работы функций

## external_api.py
currency_converter(transactions: list[Dict], id_transaction: int | None = None)

currency_converter - принимает в качестве аргумента список транзакций и номер транзакции
после чего проверяет в какой валюте была произведена транзакция и если не в рублях,
тогда функция проверяет на сервисе https://api.apilayer.com/ текущий курс и конвертирует его в рубли
на выходе результат сумма в рублях

## Тесты
Добавлены тестовые файлы test_widget.py, test_masks.py, test_processing.py, test_generators.py
которые проверяют ранее написанные функции.
В них реализованы функции:
1. test_mask_account_card,
2. test_mask_account_card_parametrize,
3. test_get_date,
4. test_filter_by_state,
5. test_sort_by_date,
6. test_get_mask_card_number,
7. test_get_mask_account
8. test_filter_by_currency_valid
9. test_empty_input
10. test_transaction_descriptions
11. test_transaction_descriptions_empty
12. test_card_number_generator
13. test_transaction_loader_not_file
14. test_transaction_loader
15. test_currency_converter


Тест запускается из командной строки, командой **pytest**

## Лицензия:

В данном конкретном случае вероятно её ещё нет 8-/
