from typing import Any

import pytest

from src.generators import card_num_gen, card_num_gen_console


# Проверяем вывод лога в файл в случае некорректных данных
def test_log_to_file(incorrect_data_for_decorator: Any) -> None:
    with pytest.raises(Exception, match="Не корректные входные данные!"):
        start_value, end_value = incorrect_data_for_decorator
        card_num_gen(start_value, end_value)


def test_log_to_console(capsys: pytest.CaptureFixture) -> None:
    # Генерируем правильный тест
    list(card_num_gen_console(1, 3))

    # Проверяем вывод в консоль с помощью capsys
    capture = capsys.readouterr()

    # Проверяем сообщение об успешном окончании
    assert (
        capture.out == "card_num_gen_console,  Ok \nWork time:  0.000001 seconds \n\n"
        or "card_num_gen_console,  Ok \nWork time:  0.000000 seconds \n\n"
    )


def test_log_to_console_error(capsys: pytest.CaptureFixture) -> None:
    # Проверяем возникновение исключения
    with pytest.raises(ValueError) as exc_info:
        card_num_gen_console(-1, 2)  # Некорректные аргументы

    # Проверяем текст исключения
    assert str(exc_info.value) == "Не корректные входные данные!"

    # Проверяем вывод в консоль с помощью capsys
    captured = capsys.readouterr()
    output = captured.out

    # Проверяем сообщение об ошибке
    assert output == "card_num_gen_console error: Не корректные входные данные!, Inputs: (-1, 2)\n\n"
