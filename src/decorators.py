from functools import wraps
from time import time
from typing import Any, Optional


def log(predicate: Any, error_message: str, filename: Optional[str] = None) -> Any:
    """
    Декоратор для логирования функций!
    :param predicate:
    :param error_message:
    :param filename:
    :return:
    """

    def wrapper(function: Any) -> Any:

        @wraps(function)
        def inner(*args: Any) -> Any:

            if not predicate(*args):
                error_txt: str = f"{function.__name__} error: {error_message}, Inputs: {args}\n"
                """Переменная выводит сообщение о некорректной работе функции!"""
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(error_txt)
                else:
                    print(error_txt)
                raise ValueError(error_message)

            time_start = time()
            """Начало работы функции"""

            result = function(*args)
            """Результат работы функции"""

            time_end = time()
            """Конец работы функции"""

            exec_time = time_end - time_start
            """Рассчитанное время работы функции"""

            success_message: str = f"{function.__name__},  Ok \nWork time: {exec_time: 4f} seconds \n"
            """Переменная выводит сообщение о корректной работе функции!"""

            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(success_message)
            else:
                print(success_message)

            return result

        return inner

    return wrapper


def predicate_param(start: int, end: int) -> bool:
    # return type(start) == int and type(end) == int and start > 0 and end > 0 and start <= end
    return isinstance(start, int) and isinstance(end, int) and start > 0 and end > 0 and start <= end
