from src.transactions_finder import filter_by_status, sort_by_date
from src.transactions_loader import csv_loader, excel_loader
from src.utils import transaction_loader


def main():
    operations = {1: "JSON", 2: "СSV", 3: "XLSX"}
    comment_1 = "Получить информацию о транзакциях из "
    comment_1_2 = "-файла"
    #status_select: str = ""
    print("Привет!\nДобро пожаловать в программу работы с банковскими транзакциями. ")
    #print("Выберите необходимый пункт меню:")
    print(f"1. {comment_1}JSON{comment_1_2}")
    print(f"2. {comment_1}CSV{comment_1_2}")
    print(f"3. {comment_1}XLSX{comment_1_2}")
    try:
        select = int(input(f"\nВыберите необходимый пункт меню: "))
        if not select in range(1, 4):
            select = 1
    except ValueError:
        select = 1

    if select == 1:
        json = transaction_loader("..\\data\\operations.json")
    elif select == 2:
        csv = csv_loader("..\\data\\transactions.csv")
    else:
        excel = excel_loader("..\\data\\transactions_excel.xlsx")

    print(f"\nДля обработки выбран {operations[select]}-файл.\n")

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status_select = str(input().lower())
        if status_select == "executed" or status_select == "canceled" or status_select == "pending":
            break
        else:
            print(f"Статус операции \"{status_select.upper()}\" недоступен.\n")
    print(f"Операции отфильтрованы по статусу \"{status_select.upper()}\"")
    if select == 1:
        result = filter_by_status(json, status_select.upper())
    elif select == 2:
        result = filter_by_status(csv, status_select.upper())
    else:
        result = filter_by_status(excel, status_select.upper())

    while True:
        print("Отсортировать операции по дате? Да/Нет")
        date_sort = str(input().lower())
        if date_sort == "да" or date_sort == "нет":
            break
    if date_sort == "да":
        while True:
            print("Отсортировать по возрастанию или по убыванию?")
            date_ascending = str(input().lower())
            if date_ascending == "по возрастанию" or date_ascending == "по убыванию":
                break
        if date_ascending == "по возрастанию":
            result2 = sort_by_date(result, True)
        else:
            result2 = sort_by_date(result, False)
    else:
        result2 = result

    print(result2)

main()