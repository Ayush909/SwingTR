"""Service layer for fetching and aggregating stock data."""

from data.stock_list import (
    get_nifty50_symbols,
    get_nifty_next_50_symbols,
    get_nifty_smallcap_50_symbols,
    get_all_symbols,
)
from data.data_fetcher import fetch_stock_data
from models.stock import Stock


def fetch_all_stocks(universe="nifty50", period="5d"):
    """Fetch data for stocks from a specified universe.

    Args:
        universe: One of "nifty50", "nifty_next_50", "nifty_smallcap_50", or "all"
        period: lookback period for historical data (default "5d")

    Returns:
        list of Stock objects (skips failed fetches)
    """
    universe_map = {
        "nifty50": get_nifty50_symbols,
        "nifty_next_50": get_nifty_next_50_symbols,
        "nifty_smallcap_50": get_nifty_smallcap_50_symbols,
        "all": get_all_symbols,
    }

    if universe not in universe_map:
        raise ValueError(f"Universe must be one of: {', '.join(universe_map.keys())}")

    symbols = universe_map[universe]()
    results = []

    for i, symbol in enumerate(symbols, 1):
        print(f"[{i}/{len(symbols)}] Fetching {symbol}...")
        data = fetch_stock_data(symbol, period=period)
        if data:
            results.append(Stock.from_dict(data))

    print(f"\nFetched {len(results)}/{len(symbols)} stocks successfully.")
    return results
