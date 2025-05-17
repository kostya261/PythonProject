from src.masks import get_mask_account, get_mask_card_number, get_mask_card_number_new

if __name__ == '__main__':
    print(get_mask_card_number("4276480025876163"))
    print(get_mask_account("4276480025876602"))
    print()
    print(get_mask_card_number_new("  4276480025876163"))
    print(get_mask_card_number_new("  42S6480025876163"))
    print(get_mask_card_number_new("427648002 5876163"))
    print(get_mask_card_number("4276480025876163"))
