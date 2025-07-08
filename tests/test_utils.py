from unittest.mock import Mock, patch

from src.utils import transaction_loader


def test_transaction_loader_not_file() -> None:

    mock_path = Mock()
    mock_path.is_file.return_value = False  # Файла нет

    with patch("src.utils.Path", return_value=mock_path) as mocked_path:
        # Вызываем функцию с тестовым путём
        path_to_file = "..\\data\\operations.jsn"
        result = transaction_loader(path_to_file)

        # Проверяем, что результат пустой список
        assert result == []

        # Проверяем, что Path вызывался с аргументом
        mocked_path.assert_called_once_with(path_to_file)

        # Проверяем, что is_file() вызывался хотя бы раз
        mock_path.is_file.assert_called_once()


def test_transaction_loader() -> None:
    mock_transaction_loader = Mock(
        return_value=[
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            }
        ]
    )
    path_to_file = "..\\data\\operations.jsn"
    result = mock_transaction_loader(path_to_file)
    assert result == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        }
    ]
    mock_transaction_loader.assert_called_once()
