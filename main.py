#!/usr/bin/env python3
"""Main CLI entry point for SwingTR stock analysis tool."""

import sys
from services.stock_service import fetch_all_stocks


def display_stocks(stocks, universe_name):
    """Display stock data in a formatted table."""
    header = f"{'SYMBOL':<15} {'PRICE':>10} {'CHANGE %':>10} {'VOLUME':>15}"
    separator = "-" * len(header)

    title = f"SwingTR - {universe_name} Stock Scanner"
    print(f"\n{title:^{len(header)}}")
    print(separator)
    print(header)
    print(separator)

    for stock in stocks:
        change_str = f"{stock.change_percent:+.2f}%"
        volume_str = f"{stock.volume:,}"
        print(f"{stock.symbol:<15} {stock.price:>10.2f} {change_str:>10} {volume_str:>15}")

    print(separator)
    print(f"Total: {len(stocks)} stocks")


def main():
    print("SwingTR - Stock Analysis CLI for Swing Trading")

    # Default to NIFTY 50, but allow command-line argument
    universe = "nifty50"
    universe_names = {
        "nifty50": "NIFTY 50",
        "nifty_next_50": "NIFTY Next 50",
        "nifty_smallcap_50": "NIFTY Smallcap 50",
        "all": "All Stocks (NIFTY 50 + Next 50 + Smallcap 50)",
    }

    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg in universe_names:
            universe = arg
        else:
            print(f"\nUsage: python3 main.py [{' | '.join(universe_names.keys())}]")
            print(f"Unknown universe: {arg}")
            sys.exit(1)

    print(f"\nFetching {universe_names[universe]}...\n")
    stocks = fetch_all_stocks(universe=universe)

    if stocks:
        display_stocks(stocks, universe_names[universe])
    else:
        print("No stock data available.")


if __name__ == "__main__":
    main()
