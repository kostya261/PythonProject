from unittest.mock import Mock, patch

from src.external_api import currency_converter


@patch("requests.get")
@patch.dict("os.environ", {"apikey": "FAKE_API_KEY"})
def test_currency_converter(mock_get: Mock, test_transactions: list) -> None:
    mock_response: Mock = Mock()
    mock_response.json.return_value = {"result": 7500.0}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result: float = currency_converter(test_transactions, 1)

    assert result == 7500.0

    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers={"apikey": "FAKE_API_KEY"},
        params={"amount": 100.0, "from": "USD", "to": "RUB"},
        timeout=10,
    )
