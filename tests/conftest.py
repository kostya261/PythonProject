from datetime import datetime
from typing import Generator, Dict
import pytest


@pytest.fixture
def error_message() -> str:
    return "Неверный номер карты!"


@pytest.fixture
def error_data_message() -> str:
    return "Неверный формат даты!"


@pytest.fixture
def current_data() -> str:
    now_time = datetime.now()
    return str(now_time.isoformat())

