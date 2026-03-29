"""Fetch stock data from Yahoo Finance."""

import yfinance as yf


def fetch_stock_data(symbol, period="5d"):
    """Fetch latest stock data for a given symbol.

    Args:
        symbol: NSE ticker with .NS suffix (e.g. "RELIANCE.NS")
        period: lookback period for historical data (default "5d")

    Returns:
        dict with keys: symbol, price, change_percent, volume
        None if fetch fails
    """
    try:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period=period)

        if hist.empty or len(hist) < 2:
            print(f"[WARN] No sufficient data for {symbol}")
            return None

        latest = hist.iloc[-1]
        previous = hist.iloc[-2]

        price = round(float(latest["Close"]), 2)
        change_percent = round(float((latest["Close"] - previous["Close"]) / previous["Close"]) * 100, 2)
        volume = int(latest["Volume"])

        return {
            "symbol": symbol.replace(".NS", ""),
            "price": price,
            "change_percent": change_percent,
            "volume": volume,
        }

    except Exception as e:
        print(f"[ERROR] Failed to fetch {symbol}: {e}")
        return None
