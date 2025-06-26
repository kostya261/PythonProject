from time import time
from functools import wraps
from typing import Any


def log(predicate: Any, error_message: str, filename: str = "") -> Any:

  def wrapper(function: Any) -> Any:

    @wraps(function)
    def inner(*args: Any, **kwargs: Any) -> Any:
      result = None
      if not predicate(*args, **kwargs):
        error_txt: str = f'{function.__name__} error: {error_message}, Inputs: {args} \n'
        if filename != "":
          with open(filename, 'a', encoding='utf-8') as file:
            file.write(error_txt)
        else:
          print(error_txt)
        return

      time_1 = time()
      result = function(*args)
      time_2 = time()
      message_ok: str = f"{function.__name__},  Ok \nWork time: {round(time_2 - time_1, 10)} \n"

      if filename != "":
        with open(filename, 'a', encoding='utf-8') as file:
          file.write(message_ok)
      else:
        print(message_ok)

      return result
    return inner
  return wrapper




def predicate_param(start: int, end: int) -> bool:
  return type(start) == int and type(end) == int and start > 0 and end > 0



def log_(predicate, error_message: str, filename: str = ""):
    """
    Данная функция делает логи на ... х.з., что она там делает.

    :param filename: - путь к файлу и имя файла, куда будет писаться лог
    :param predicate: - функция (ну не знаю как описать) которая делает предварительные проверки перед вызовом
                        логируемой функции
    :param error_message: - сообщение об ошибке
    :return:
    """

    #print (path)
    def wrapper(function):
        time_1: float = time()
        def inner(*args):
            log_data = {
                "time": round(time_2 - time_1, 10),
                "function": function.__name__,
                "args": args,
            }
            if not predicate(*args):
                if filename == "":
                    raise ValueError(error_message)
                else:
                    print(error_message)
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f"\n----------------------------------------------\n")
                        file.write(f"Ошибка функции \n")
                        file.write(f"    Имя функции: {str(log_data["function"])} \n")
                        file.write(f"    Аргументы функции: {str(log_data["args"])} \n")
                        file.write(f"    Ошибка функции: {str(error_message)} \n")

            else:
                if function.__name__ != 'inner':
                    if filename == "":
                        print(f'\nВызов функции: {function.__name__} --> Ok')
                    else:
                        print(f'\nВызов функции: {function.__name__} --> Ok ', filename)
                        with open(filename, 'a', encoding='utf-8') as file:
                            file.write(f"----------------------------------------------\n")
                            file.write(f"Успешное выполнение \n")
                            file.write(f"    Время работы функции: {str(log_data["time"])} \n")
                            file.write(f"    Имя функции: {str(log_data["function"])} \n")
                            file.write(f"    Аргументы функции: {str(log_data["args"])} \n")


            return function(*args)

        calculate_time: float = round(time_2 - time_1, 10)
        print(f'Время работы функции: {calculate_time}')
        return inner
    time_2: float = time()



    return wrapper


def predicate_int(start_value: int = None, end_value: int = None) -> bool:
    return type(start_value) == int and type(end_value) == int


def predicate_positive(start_value: int = None, end_value: int = None) -> bool:
    return start_value >= 0 and end_value >= 0


if __name__ == '__main__':

    @log(predicate_param, "Неверные входные данные!", "noname.log")
    def my_func(start_value: int = 1, end_value: int = 100):
        print(f"Hello! {start_value} {end_value}")



    my_func(1, 20)


