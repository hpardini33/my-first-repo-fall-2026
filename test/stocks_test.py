# test/stocks_test.py
from app.stocks import format_usd, fetch_stocks_data

def test_format_usd():
    assert format_usd(4000) == "$4,000.00"
    assert format_usd(3.5) == "$3.50"
    assert format_usd(1234567.891) == "$1,234,567.89"

def test_fetch_stocks_data():
    df = fetch_stocks_data("IBM")
    assert "close" in df.columns
    assert len(df) > 0