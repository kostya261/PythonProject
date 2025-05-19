from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date

if __name__ == '__main__':

    print(mask_account_card("Счет 73654108430535874307"))
    print(mask_account_card("Visa Platinum 7000712289606361"))
    print(mask_account_card("Maestro 7000792089106361"))

    print()

    # Если строка будет в таком виде, как сказано в задании... "2024-03-11T02:26:18.671407"
    # тогда всё у нас будет хорошо

    print(get_date("2024-03-11T02:26:18.671407"))