import pytest

from src.generators import card_number_generator

'''
def test_log_decor(input_data: tuple, capsys):
    start_value, end_value, expected = input_data
    gen_card = list()
    # пустой список для последовательной записи сгенерированных карт
    expected_card = list()
    # попутно создаем пустой список, куда будем последовательно класть варианты из expected

    for i in card_number_generator(start_value, end_value):
        gen_card.append(i)
        expected_card.append(expected)

    # после того как оба списка созданы, сравниваем их
    assert gen_card == expected




    captured = capsys.readouterr()
    assert captured.out == expected

'''
def test_log(capsys):
    card_number_generator(1, 5)
    out, err = capsys.readouterr()
    assert out == '\nВызов функции: card_number_generator --> Ok\n'
    assert err == ''


def test_log_under_zero():
    with pytest.raises(ValueError, match="Число меньше нуля!"):
        card_number_generator(-1, 0)


def test_log_float():
    with pytest.raises(ValueError, match="Число не целое!"):
        card_number_generator(1.0, 0)