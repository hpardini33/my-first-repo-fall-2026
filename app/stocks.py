# app/stocks.py
import os
from dotenv import load_dotenv
from pandas import read_csv

load_dotenv()  # reads your API key from the .env file

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")


def format_usd(my_price):
    """Formats a number as US dollars. Example: 4000 becomes '$4,000.00'"""
    return f"${my_price:,.2f}"


def fetch_stocks_data(symbol):
    """Gets daily stock prices for a ticker symbol, newest first."""
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"
    df = read_csv(url)
    if "close" not in df.columns:
        # Alpha Vantage sends back an error message instead of prices
        raise ValueError(f"No data found for symbol '{symbol}'")
    return df


if __name__ == "__main__":
    symbol = input("Please input a stock symbol (default: 'NFLX'): ") or "NFLX"
    df = fetch_stocks_data(symbol)
    latest = df.iloc[0]
    print("SYMBOL:", symbol)
    print("DATE:", latest["timestamp"])
    print("LATEST CLOSE:", format_usd(latest["close"]))