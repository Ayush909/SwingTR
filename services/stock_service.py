"""Service layer for fetching and aggregating stock data."""

from data.stock_list import get_nifty50_symbols
from data.data_fetcher import fetch_stock_data
from models.stock import Stock


def fetch_all_stocks(period="5d"):
    """Fetch data for all NIFTY 50 stocks.

    Returns:
        list of Stock objects (skips failed fetches)
    """
    symbols = get_nifty50_symbols()
    results = []

    for i, symbol in enumerate(symbols, 1):
        print(f"[{i}/{len(symbols)}] Fetching {symbol}...")
        data = fetch_stock_data(symbol, period=period)
        if data:
            results.append(Stock.from_dict(data))

    print(f"\nFetched {len(results)}/{len(symbols)} stocks successfully.")
    return results
